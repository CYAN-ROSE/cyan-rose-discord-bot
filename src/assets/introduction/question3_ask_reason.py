from discord.ui import Button, View, Modal, TextInput, button
from discord import Embed, ButtonStyle, Interaction, TextStyle
from database.tables import Introduction

from . import question4_ask_politic

import logging

logger = logging.getLogger("cyan")

reason_embed = Embed(title="And why do you want to join?",
                    description="", # No description needed for now?
                    color=0x00ffff,)
reason_embed.set_thumbnail(url="https://raw.githubusercontent.com/Society-of-the-Cyan-Rose/cyan-rose-discord-bot/main/src/assets/cyan-rose.png")

class reason_modal(Modal):
    def __init__(self):
        super().__init__(timeout=None, title="Why do you want to join?")
        
        self.reason_input = TextInput(label="Explain it here:", placeholder="I want to join because...", min_length=10, max_length=500, style=TextStyle.paragraph, required=True)
        self.add_item(self.reason_input)
    
    async def interaction_check(self, interaction: Interaction):
        if Introduction.select().where(Introduction.user_id == interaction.user.id, Introduction.part == 2).exists():
            Introduction.update(introduction=self.reason_input.value).where(Introduction.user_id == interaction.user.id, Introduction.part == 2).execute()
            logger.debug(f"Updated reason for user: {interaction.user}")
        else:
            logger.debug(f"Created reason for user: {interaction.user}")
            Introduction.create(user_id=interaction.user.id, part=2, introduction=self.reason_input.value)
        await interaction.response.edit_message(embed=question4_ask_politic.politic_embed, view=question4_ask_politic.politic_view())

class reason_view(View):
    def __init__(self):
        super().__init__(timeout=None)

    @button(label="because...", style=ButtonStyle.primary)
    async def get_reason_button(self, interaction : Interaction, button : Button):
        logger.debug(f"Button: Get Reason - question3 - introduction | User: {interaction.user}")
        await interaction.response.send_modal(reason_modal())
