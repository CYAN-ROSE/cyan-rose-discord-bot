# src/cogs/load_scripts/load_tasks.py
# version: 1.1
# last updated: 29-03-24

from discord.ext import commands
from os import listdir

import logging

logger = logging.getLogger("cyan")

async def load_tasks(client: commands.Bot, reload: bool = False):
    """Load all tasks from the tasks directory."""
    for file in listdir("src/cogs/tasks"):
        if file.endswith(".py"):
            try:
                if reload:
                    client.reload_extension(f"cogs.tasks.{file[:-3]}")
                    logger.info(f"Reloaded task: {file[:-3]}")
                else:
                    await client.load_extension(f"cogs.tasks.{file[:-3]}")
                    logger.info(f"Loaded task: {file[:-3]}")
            except Exception as e:
                logger.error(f"Failed to load task: {file[:-3]}. {e}")
