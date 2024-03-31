from discord import app_commands, Interaction
from discord.ext import commands

import logging

logger = logging.getLogger("cyan") # Logger

class PingCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='ping', description='Requests ping of the bot!')
    async def ping(self, interaction : Interaction):
        latency : int= self.bot.latency * 1000

        logger.info(f"Command: Ping | User: {interaction.user.name}")
        logger.debug(f"Latency: {latency}ms")

        await interaction.response.send_message(f"Pong! Latency: {round(latency)}ms")

async def setup(bot):
    await bot.add_cog(PingCmd(bot))
