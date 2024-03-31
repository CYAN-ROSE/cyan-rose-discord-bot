from discord import app_commands, Interaction, File
from discord.ext import commands

import logging

logger = logging.getLogger("cyan")

class LogCmd(commands.Cog):
    
    @app_commands.command(name="showfulllog", description="Shows the log file.")
    async def showfulllog(self, interaction : Interaction):
        logger.info(f"{interaction.user.name} requested the log file.")
        await interaction.response.send_message("Here is the log file.", file=File("cyan.log"))

    @app_commands.command(name="showlastlog", description="Shows the last 10 lines of the log file.")
    async def showlastlog(self, interaction : Interaction):
        logger.info(f"{interaction.user.name} requested last 10 lines of the log file.")
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

async def setup(bot):
    await bot.add_cog(LogCmd(bot))