from discord.ui import Button, View, Modal, TextInput, button
from discord import Embed, ButtonStyle, Interaction, TextStyle
from database.tables import Introduction

from . import question4_ask_politic

import logging

logger = logging.getLogger("cyan")

reason_embed = Embed(title="Why do you want to join Cyan Rose?", 
                    description="Hint: Click the button below to explain in short why you want you join us!",
                    color=0x00ffff,)
reason_embed.set_thumbnail(url="https://raw.githubusercontent.com/Society-of-the-Cyan-Rose/cyan-rose-discord-bot/main/src/assets/cyan-rose.png")

class reason_modal(Modal):
    def __init__(self):
        super().__init__(timeout=None, title="Explain why you want to join Cyan Rose!")
        
        self.reason_input = TextInput(label="Explain why you want to join Cyan Rose here:", placeholder="I want to join because...", min_length=10, max_length=500, style=TextStyle.paragraph, required=True)
        self.add_item(self.reason_input)
    
    async def interaction_check(self, interaction: Interaction):
        
        Introduction.create(user_id=interaction.user.id, part=2, introduction=self.reason_input.value)
        await interaction.response.edit_message(embed=question4_ask_politic.politic_embed, view=question4_ask_politic.politic_view())

class reason_view(View):
    def __init__(self):
        super().__init__(timeout=None)

    @button(label="Explain why you want to join", style=ButtonStyle.primary)
    async def get_reason_button(self, interaction : Interaction, button : Button):
        logger.debug(f"Button: Get Reason | User: {interaction.user}")
        await interaction.response.send_modal(reason_modal())