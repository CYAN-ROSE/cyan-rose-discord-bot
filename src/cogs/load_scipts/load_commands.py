# src/cogs/load_scripts/load_commands.py
# version: 1.1
# last updated: 29-03-24

from discord.ext import commands
from os import listdir

import logging

logger = logging.getLogger("cyan")

async def load_commands(client: commands.Bot, reload: bool = False):
    """Load all commands from the commands directory."""
    for file in listdir("src/cogs/commands"):
        if file.endswith(".py"):
            try:
                if reload:
                    client.reload_extension(f"cogs.commands.{file[:-3]}")
                    logger.info(f"Reloaded command: {file[:-3]}")
                else:
                    await client.load_extension(f"cogs.commands.{file[:-3]}")
                    logger.info(f"Loaded command: {file[:-3]}")
            except Exception as e:
                logger.error(f"Failed to load command: {file[:-3]}. {e}")
