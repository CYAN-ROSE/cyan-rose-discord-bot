from discord import app_commands, Interaction, File
from discord.ext import commands

import logging

logger = logging.getLogger("cyan") # Logger

class DebugSuite(app_commands.Group):

    @app_commands.command(name='help', description='Debug command suite.')
    async def debug(self, interaction : Interaction):
        logger.info(f"Command: Debug | User: {interaction.user.name}")

        await interaction.response.send_message('Debug command suite.')

    @app_commands.command(name='ping', description='Debug ping command.')
    async def debugping(self, interaction : Interaction):
        latency : int= self.bot.latency * 1000

        logger.info(f"Command: DebugPing | User: {interaction.user.name}")
        logger.debug(f"Latency: {latency}ms")

        await interaction.response.send_message(f"Pong! Latency: {round(latency)}ms")

    @app_commands.command(name='logfile', description='Debug log command.')
    async def debuglog(self, interaction : Interaction):
        logger.info(f"Command: DebugLog | User: {interaction.user.name}")
        await interaction.response.send_message("Here is the log file.", file=File("cyan.log"))

    @app_commands.command(name='loglast', description='Debug last 10 lines of log command.')
    async def debuglastlog(self, interaction : Interaction):
        logger.info(f"Command: DebugLastLog | User: {interaction.user.name}")
        with open("cyan.log", "r") as f:
            lines = f.readlines()
            last_lines = ''
            for line in lines[-10:]:
                last_lines += line
            if len(last_lines) < 10:
                last_lines = lines
            if len(last_lines) > 1800:
                await interaction.response.send_message("The log file is too large to send. Please use the showfulllog command.")
                return
            logger.debug(last_lines)
            await interaction.response.send_message("Here are the last 10 lines of the log file.\n```arduino\n" + last_lines + "\n```")

async def setup(bot : commands.Bot):
    bot.tree.add_command(DebugSuite(name='debug', description='Debug command suite.'))