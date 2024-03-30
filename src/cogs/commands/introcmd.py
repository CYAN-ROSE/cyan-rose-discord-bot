from discord import app_commands, Interaction
from discord.ext import commands

from assets.introduction import question1_ask_name

import logging

logger = logging.getLogger("cyan") # Logger

class IntroCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='introduce', description='Starts introduction prompt')
    async def intro(self, interaction : Interaction):
        logger.info(f"Command: Intro | User: {interaction.user}")

        await interaction.user.send(embed=question1_ask_name.name_embed, view=question1_ask_name.name_view())

        await interaction.response.send_message('You have been sent a DM with the introduction interview!')

async def setup(bot):
    await bot.add_cog(IntroCmd(bot))