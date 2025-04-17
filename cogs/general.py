import discord
from discord.ext import commands
from discord import app_commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Check the bot's latency.")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"🏓 Pong! Latency: {round(self.bot.latency * 1000)}ms")

    @app_commands.command(name="say", description="Make the bot say something.")
    async def say(self, interaction: discord.Interaction, message: str):
        await interaction.response.send_message(message)

async def setup(bot):
    await bot.add_cog(General(bot))
