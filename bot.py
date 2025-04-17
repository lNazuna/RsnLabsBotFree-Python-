import discord
from discord.ext import commands
import json
import asyncio
from utils.logger import setup_logger
from utils.database import DatabaseHandler
from rsnchat import RsnChat

logger = setup_logger()

with open('config.json') as f:
    config = json.load(f)

intents = discord.Intents.all()

rsn_chat = RsnChat(config["rsnchat_key"])

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or(config["prefix"]),
            intents=intents,
            application_id=None,
            owner_ids=set(config["owner_ids"])
        )
        self.initial_extensions = [
            'cogs.general',
            'cogs.moderation',
            'cogs.rsnchat',
            'cogs.settings'
        ]
        self.synced = False
        self.db = DatabaseHandler()

    async def setup_hook(self):
        for ext in self.initial_extensions:
            try:
                await self.load_extension(ext)
                logger.info(f"Extension {ext} loaded successfully")
            except Exception as e:
                logger.error(f"Failed to load extension {ext}: {e}")
        await self.sync_commands()

    async def sync_commands(self):
        try:
            if config["guild_only"]:
                guild_id = int(config["guild_id"])
                guild = discord.Object(id=guild_id)
                self.tree.copy_global_to(guild=guild)
                await self.tree.sync(guild=guild)
                logger.info(f"Commands synced for guild {guild_id}")
            else:
                await self.tree.sync()
                logger.info("Commands synced globally")
            self.synced = True
        except Exception as e:
            logger.error(f"Error syncing commands: {e}")
            logger.info("Retrying sync in 5 seconds...")
            await asyncio.sleep(5)
            await self.sync_commands()

    async def on_ready(self):
        logger.info(f'Bot connected as {self.user} (ID: {self.user.id})')
        if not self.synced:
            logger.info("Syncing commands...")
            await self.sync_commands()

    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        await self.process_commands(message)
        
        channel_id_str = str(message.channel.id)
        
        channels_data = self.db.list_channels()
        
        if channel_id_str not in channels_data:
            return
        
        model = self.db.get_channel_model(message.channel.id)
        if not model:
            logger.warning(f"Channel {channel_id_str} found in database but has no model configured")
            return
        
        try:
            async with message.channel.typing():
                response = rsn_chat.generate_chat_response(model, message.content)
                reply = response.get('message', '')

                if reply:
                    await message.channel.send(reply)
                else:
                    logger.warning("Empty response from the API.")
        except Exception as e:
            logger.error(f"Error generating RsnChat response: {e}")

bot = MyBot()
bot.run(config["token"])