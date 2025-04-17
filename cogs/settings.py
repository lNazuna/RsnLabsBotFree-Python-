import discord
from discord.ext import commands
from discord import app_commands
from utils.database import DatabaseHandler
from utils.permissions import is_admin

class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = DatabaseHandler()
    
    setup_group = app_commands.Group(name="setup", description="Channel AI setup commands")
    
    @setup_group.command(name="setchannel", 
                         description="Set a channel to use a specific AI chat model")
    @app_commands.choices(model=[
        app_commands.Choice(name="Gemini", value="gemini"),
        app_commands.Choice(name="Claude", value="claude"),
        app_commands.Choice(name="Deepseek V3", value="deepseek-v3"),
        app_commands.Choice(name="GPT", value="gpt"),
        app_commands.Choice(name="Deepseek R1", value="deepseek-r1"),
        app_commands.Choice(name="Llama", value="llama"),
        app_commands.Choice(name="Grok 3", value="grok-3"),
        app_commands.Choice(name="Grok 3 R1", value="grok-3-r1"),
        app_commands.Choice(name="GPT-4", value="gpt4")
    ])
    async def set_channel(
        self,
        interaction: discord.Interaction,
        channel: discord.TextChannel,
        model: app_commands.Choice[str]
    ):
        if not await is_admin(interaction):
            return
            
        try:
            current_model = self.db.get_channel_model(channel.id)
            if current_model == model.value:
                await interaction.response.send_message(
                    f"⚠️ Channel {channel.mention} is already set to use the {model.name} model.",
                    ephemeral=True
                )
                return
            
            if current_model:
                await interaction.response.send_message(
                    f"❌ Channel {channel.mention} is already configured to use the **{current_model}** model.\n"
                    f"Please use `/setup updatemodel` to change the model.",
                    ephemeral=True
                )
                return
                
            self.db.set_channel_model(channel.id, model.value)
            
            embed = discord.Embed(
                title="✅ Channel Configured",
                description=f"Channel {channel.mention} is now set to use the **{model.name}** model for AI responses.",
                color=discord.Color.green(),
                timestamp=interaction.created_at
            )
            
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(
                f"❌ Error: {str(e)}",
                ephemeral=True
            )
    
    @setup_group.command(name="updatemodel", 
                         description="Update a channel's AI model (only if already configured)")
    @app_commands.choices(model=[
        app_commands.Choice(name="Gemini", value="gemini"),
        app_commands.Choice(name="Claude", value="claude"),
        app_commands.Choice(name="Deepseek V3", value="deepseek-v3"),
        app_commands.Choice(name="GPT", value="gpt"),
        app_commands.Choice(name="Deepseek R1", value="deepseek-r1"),
        app_commands.Choice(name="Llama", value="llama"),
        app_commands.Choice(name="Grok 3", value="grok-3"),
        app_commands.Choice(name="Grok 3 R1", value="grok-3-r1"),
        app_commands.Choice(name="GPT-4", value="gpt4")
    ])
    async def update_model(
        self,
        interaction: discord.Interaction,
        channel: discord.TextChannel,
        model: app_commands.Choice[str]
    ):
        if not await is_admin(interaction):
            return
            
        try:
            channels_data = self.db.list_channels()
            if str(channel.id) not in channels_data:
                await interaction.response.send_message(
                    f"❌ Error: Channel {channel.mention} is not registered in the database.\n"
                    f"Please use `/setup setchannel` first to configure this channel.",
                    ephemeral=True
                )
                return
            
            current_model = self.db.get_channel_model(channel.id)
            
            if current_model == model.value:
                await interaction.response.send_message(
                    f"⚠️ Channel {channel.mention} is already set to use the {model.name} model.",
                    ephemeral=True
                )
                return
                
            self.db.set_channel_model(channel.id, model.value)
            
            embed = discord.Embed(
                title="✅ Model Updated",
                description=f"Channel {channel.mention} has been updated from **{current_model}** to **{model.name}** model.",
                color=discord.Color.blue(),
                timestamp=interaction.created_at
            )
            
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(
                f"❌ Error: {str(e)}",
                ephemeral=True
            )
    
    @setup_group.command(name="removechannel", 
                         description="Remove a channel from AI chat processing")
    async def remove_channel(
        self,
        interaction: discord.Interaction,
        channel: discord.TextChannel
    ):
        if not await is_admin(interaction):
            return
            
        if self.db.remove_channel(channel.id):
            embed = discord.Embed(
                title="✅ Channel Removed",
                description=f"Channel {channel.mention} has been removed from AI chat processing.",
                color=discord.Color.red(),
                timestamp=interaction.created_at
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message(
                f"❓ Channel {channel.mention} was not configured for AI chat processing.",
                ephemeral=True
            )
    
    @setup_group.command(name="listchannels", 
                         description="List all channels configured for AI chat")
    async def list_channels(self, interaction: discord.Interaction):
        if not await is_admin(interaction):
            return
            
        channels_data = self.db.list_channels()
        
        if not channels_data:
            await interaction.response.send_message(
                "No channels are currently configured for AI chat.",
                ephemeral=True
            )
            return
        
        embed = discord.Embed(
            title="AI Chat Channels Configuration",
            color=discord.Color.blue(),
            description="List of all channels configured for AI chat responses:",
            timestamp=interaction.created_at
        )
        
        for channel_id, settings in channels_data.items():
            try:
                channel = self.bot.get_channel(int(channel_id))
                channel_name = channel.mention if channel else f"Unknown Channel ({channel_id})"
                model_name = settings.get("model", "Unknown")
                embed.add_field(
                    name=channel_name,
                    value=f"Model: **{model_name}**",
                    inline=False
                )
            except Exception as e:
                embed.add_field(
                    name=f"Channel ID: {channel_id}",
                    value=f"Model: **{settings.get('model', 'Unknown')}**\nError: {str(e)}",
                    inline=False
                )
        
        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(Settings(bot))