from discord.ui import Button, View, button
from discord import Embed, ButtonStyle, Interaction

from . import question1_ask_name

import logging

logger = logging.getLogger("cyan")

disclosure_embed = Embed(title="Welcome to your interview!", 
                    description=(
                      "I'll ask you some basic questions.\n"
                      "\n"
                      "Your answers will let the members know what "
                      "they need to know about you. The Society will "
                      "then review your answers to see if you're a "
                      "good fit and make sure you're not a bot or "
                      "troll. If you get accepted, **your answers "
                      "will be publicly viewable [online]"
                      "(https://github.com/Society-of-the-Cyan-Rose"
                      "/meet-the-cast) as well**.\n"
                      "\n"
                      "You can edit this information later."
                    ),
                    color=0x00ffff,)
disclosure_embed.set_thumbnail(url="https://raw.githubusercontent.com/Society-of-the-Cyan-Rose/cyan-rose-discord-bot/main/src/assets/cyan-rose.png")

class disclosure_view(View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @button(label="continue", style=ButtonStyle.primary)
    async def continue_button(self, interaction : Interaction, button : Button):
        logger.debug(f"Button: Continue - Question0 - introduction | User: {interaction.user}")
        await interaction.response.edit_message(embed=question1_ask_name.name_embed, view=question1_ask_name.name_view())
