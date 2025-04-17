import discord
import asyncio
import json
from discord.ext import commands
from discord import app_commands
from rsnchat import RsnChat

with open('config.json') as f:
    config = json.load(f)

class RsnChatCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.rsn_chat = RsnChat(config["rsnchat_key"])

    @app_commands.command(name="imagine", description="Generate an image based on the provided description.")
    @app_commands.choices(model=[
        app_commands.Choice(name="RSNLabs", value="rsnlabs"),
        app_commands.Choice(name="Flux", value="flux"),
        app_commands.Choice(name="Anime", value="anime"),
        app_commands.Choice(name="Disney", value="disney"),
        app_commands.Choice(name="Cartoon", value="cartoon"),
        app_commands.Choice(name="Photography", value="photography"),
        app_commands.Choice(name="Icon", value="icon"),
        app_commands.Choice(name="Ghibli", value="ghibli")
    ])
    async def imagine(
        self, 
        interaction: discord.Interaction, 
        description: str, 
        model: app_commands.Choice[str]
    ):
        try:
            await interaction.response.defer(thinking=True)
            
            await interaction.followup.send("✨ Generating your image... Please wait while we create your artwork! This may take up to 5 minutes. ✨")
            
            try:
                # Generate the image using the selected RsnChat model
                response = self.rsn_chat.generate_image(description, model.value)
                
                # Check if the response contains the image URL
                image_url = response.get('image_url', None)
                if image_url:
                    # Create an embed with the image
                    embed = discord.Embed(
                        title="Generated Image",
                        description=f"**Prompt:** {description}",
                        color=discord.Color.blue()
                    )
                    embed.set_image(url=image_url)
                    embed.set_footer(text=f"Model: {model.name}")
                    
                    await interaction.followup.send(embed=embed)
                else:
                    await interaction.followup.send("Error: Could not generate the image.")
            except Exception as e:
                await interaction.followup.send(f"Error generating image: {str(e)}")
        
        except Exception as e:
            await interaction.followup.send(f"Error generating image: {str(e)}")

    @app_commands.command(name="rsn-models", description="List all available RSN models.")
    async def list_models(self, interaction: discord.Interaction):
        try:
            await interaction.response.defer(thinking=True)
            
            try:
                # Create a new RsnChat instance without key for listing models
                rsn_chat = RsnChat()
                response = rsn_chat.list_models()
                
                if response:
                    # Create an embed for the models
                    embed = discord.Embed(
                        title="Available RSN Models",
                        color=discord.Color.green()
                    )
                    
                    # Add chat models to embed
                    chat_models_text = ""
                    for chat_model in response.get('chat_models', []):
                        chat_models_text += f"• **{chat_model['name']}** (Status: {chat_model['status']})\n"
                    
                    if chat_models_text:
                        embed.add_field(name="Chat Models", value=chat_models_text, inline=False)
                    
                    # Add image models to embed
                    image_models_text = ""
                    for image_model in response.get('image_models', []):
                        image_models_text += f"• **{image_model['name']}** (Status: {image_model['status']})\n"
                    
                    if image_models_text:
                        embed.add_field(name="Image Models", value=image_models_text, inline=False)
                    
                    # Add girls character models to embed
                    girls_models_text = ""
                    for girl_model in response.get('girls_character_models', []):
                        girls_models_text += f"• **{girl_model['name']}** (Status: {girl_model['status']})\n"
                    
                    if girls_models_text:
                        embed.add_field(name="Girls Character Models", value=girls_models_text, inline=False)
                    
                    # Add powered by information
                    powered_by = response.get('powered_by', 'Unknown')
                    embed.set_footer(text=f"Powered By: {powered_by}")
                    
                    await interaction.followup.send(embed=embed)
                else:
                    await interaction.followup.send("Failed to fetch the models.")
            except Exception as e:
                await interaction.followup.send(f"Error listing models: {str(e)}")
        
        except Exception as e:
            await interaction.followup.send(f"Error: {str(e)}")

async def setup(bot):
    await bot.add_cog(RsnChatCog(bot))
