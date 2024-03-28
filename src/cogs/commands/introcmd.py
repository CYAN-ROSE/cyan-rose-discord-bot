from discord import app_commands, Interaction
from discord.ext import commands

import logging

logger = logging.getLogger("cyan") # Logger

class IntroCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='introduce', description='Starts introduction prompt')
    async def intro(self, interaction : Interaction):
        logger.info(f"Command: Intro | User: {interaction.user}")

        await interaction.user.send("PLACEHOLDER")

        await interaction.response.send_message('You have been sent a DM with the introduction interview!')