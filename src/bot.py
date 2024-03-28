# src/bot.py
# version: 1.0
# last updated: 29-03-24

from discord import Intents
from discord.ext import commands
import cogs.load_scipts as load_scripts
from asyncio import run as asc_run
from dotenv import load_dotenv
from os import getenv

intents = Intents.all() # Enable all intents
client = commands.Bot(command_prefix="!", intents=intents, help_command=None) # Create a bot instance

load_dotenv() # Load the .env file

def run():
    """Async function to run the bot."""
    
    asc_run(load_scripts.all(client)) # Load all scripts
    
    client.run(getenv("TOKEN"), log_handler=None, log_level=None, log_formatter=None) # Run the bot, disable discord logging