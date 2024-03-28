# src/main.py

import logging
from rich.logging import RichHandler # RichHandler is pretty :3

import bot

# Setup Rich Handler for logging
rh = RichHandler(show_time=False, show_level=False) # RichHandler initialization
rh.setFormatter(logging.Formatter("%(asctime)s  %(name)s  %(levelname)s  %(message)s")) # Formatter for RichHandler

# Setup internal logging
logger = logging.getLogger("cyan") # uses "cyan"
logger.addHandler(rh) # Rich Handler for logs
logger.addHandler(logging.FileHandler("cyan.log", mode="w")) # File Handler for logs
logger.setLevel(logging.DEBUG)
logger.info("Logging Initialized.") # Logs initialization

# Setup discord logging
dc_logger = logging.getLogger("discord") # uses "discord"
dc_logger.setLevel(logging.INFO) # Set the level to INFO
dc_logger.addHandler(rh) # Rich Handler for logs
dc_logger.info("Logging Initialized.") # Logs initialization

if __name__ == "__main__":
    logger.info("Welcome to Cyan Rose.")
    with open("./src/assets/ASCII.txt", "r") as f:
        print(f.read())

    bot.run() # Runs the bot