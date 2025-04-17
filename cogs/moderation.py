import discord
from discord.ext import commands
from discord import app_commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="kick", description="Kick a member from the server.")
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        reason: str = "No reason provided"
    ):
        await member.kick(reason=reason)
        await interaction.response.send_message(f"{member.mention} has been kicked. 🦶", ephemeral=True)

    @app_commands.command(name="ban", description="Ban a member from the server.")
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        reason: str = "No reason provided"
    ):
        await member.ban(reason=reason)
        await interaction.response.send_message(f"{member.mention} has been banned. 🔨", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Moderation(bot))
