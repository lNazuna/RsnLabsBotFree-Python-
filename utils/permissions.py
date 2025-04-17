import discord

async def is_admin(interaction: discord.Interaction) -> bool:
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message(
            "❌ This command is restricted to server administrators only.",
            ephemeral=True
        )
        return False
    return True