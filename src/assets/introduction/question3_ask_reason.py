from discord.ui import Button, View, Modal, TextInput
from discord import Embed, ButtonStyle, Interaction
from database.tables import Introduction

from . import question2_ask_birth

import logging

logger = logging.getLogger("cyan")

reason_embed = Embed(title="Why do you want to join Cyan Rose?", 
                    description="Hint: Click the button below to explain in short why you want you join us!",
                    color=0x00ffff,)
reason_embed.set_thumbnail(url="src/assets/cyan-rose.png")

class reason_modal(Modal):
    def __init__(self):
        super().__init__(timeout=None, title="Explain why you want to join Cyan Rose!")
        
        self.add_item(TextInput(label="Explain why you want to join Cyan Rose here:", placeholder="I want to join because...", min_length=10, max_length=250, required=True))
    
    async def interaction_check(self, interaction: Interaction):
        
        Introduction.create(user_id=interaction.user.id, type=2, introduction=self.items[0].value)
        await interaction.response.edit_message(embed=question2_ask_birth.birth_embed, view=question2_ask_birth.birth_view())

class reason_view(View):
    def __init__(self):
        super().__init__(timeout=None)

    @Button(label="Explain why you want to join", style=ButtonStyle.primary)
    async def get_reason_button(self, interaction : Interaction, button : Button):
        logger.debug(f"Button: Get Reason | User: {interaction.user}")
        interaction.response.send_modal(reason_modal())