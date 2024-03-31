from discord import Embed, Interaction
from database.tables import Introduction

import logging

logger = logging.getLogger("cyan")

def build(interaction : Interaction) -> Embed:
    embed = Embed(title=f"Introduction from {interaction.user.name}", 
                  color=0x00ffff,)
    embed.set_thumbnail(url="https://raw.githubusercontent.com/Society-of-the-Cyan-Rose/cyan-rose-discord-bot/main/src/assets/cyan-rose.png")
    introduction = Introduction.select().where(Introduction.user_id == interaction.user.id).execute()
    logger.debug("Building Embed for Introduction")
    for intro in introduction:
        logger.debug("Building Layer")
        if intro.part == 0:
            embed.add_field(name=f"Name or Nickname", value=intro.introduction, inline=False)
        elif intro.part == 1:
            embed.add_field(name=f"Date of Birth / Age Range", value=f"{intro.introduction}", inline=False)
        elif intro.part == 2:
            embed.add_field(name=f"Reason For Joining", value=intro.introduction, inline=False)
        elif intro.part == 3:
            embed.add_field(name=f"Political Stance", value=intro.introduction, inline=False)
    logger.debug("Built Embed for Introduction")
    return embed