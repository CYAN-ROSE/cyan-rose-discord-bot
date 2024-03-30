# src/main.py

import logging
from rich.logging import RichHandler # RichHandler is pretty :3

import bot
import database as db

# Setup Rich Handler for logging
rh = RichHandler(show_time=False, show_level=False) # RichHandler initialization
rh.setFormatter(logging.Formatter("%(asctime)s  %(name)s  %(levelname)s  %(message)s")) # Formatter for RichHandler

# Setup file logging
fh = logging.FileHandler("cyan.log") # FileHandler initialization
fh.setFormatter(logging.Formatter("%(asctime)s  %(name)s  %(levelname)s  %(message)s")) # Formatter for FileHandler

# Setup internal logging
logger = logging.getLogger("cyan") # uses "cyan"
logger.setLevel(logging.DEBUG) # Set the level to DEBUG
logger.addHandler(rh) # Rich Handler for logs
logger.addHandler(fh) # File Handler for logs
logger.info("Logging Initialized.") # Logs initialization

# Setup discord logging
dc_logger = logging.getLogger("discord") # uses "discord"
dc_logger.setLevel(logging.INFO) # Set the level to INFO
dc_logger.addHandler(rh) # Rich Handler for logs
dc_logger.addHandler(fh) # File Handler for logs
dc_logger.info("Logging Initialized.") # Logs initialization

if __name__ == "__main__":
    logger.info("Welcome to Cyan Rose.")
    
    with open("./src/assets/ASCII.txt", "r") as f:
        print(f.read())

    # inp = input("Press Y to destroy database: ")
    # if inp.lower() == "y":
    #     db.drop_tables()  # Destroys tables if user wants to

    db.create_tables() # Creates tables if they don't exist

    bot.run() # Runs the bot