# src/cogs/load_scripts/load_events.py
# version: 1.1
# last updated: 29-03-24

from discord.ext import commands
from os import listdir

import logging

logger = logging.getLogger("cyan")

async def load_events(client: commands.Bot, reload: bool = False):
    """Load all events from the events directory."""
    for file in listdir("src/cogs/events"):
        if file.endswith(".py"):
            try:
                if reload:
                    client.reload_extension(f"src.cogs.events.{file[:-3]}")
                    logger.info(f"Reloaded event: {file[:-3]}")
                else:
                    await client.load_extension(f"src.cogs.events.{file[:-3]}")
                    logger.info(f"Loaded event: {file[:-3]}")
            except Exception as e:
                logger.error(f"Failed to load event: {file[:-3]}. {e}")