from discord.ui import Button, View, Modal, TextInput
from discord import Embed, ButtonStyle, Interaction
from database.tables import Introduction

from . import question2_ask_birth

import logging

logger = logging.getLogger("cyan")

name_embed = Embed(title="What's your name?", 
                   description="Hint: Click the button below and enter your name(s) or nickname(s)!",
                   color=0x00ffff,)
name_embed.set_thumbnail(url="src/assets/cyan-rose.png")

class name_modal(Modal):
    def __init__(self):
        super().__init__(timeout=None, title="Enter your name(s) or nickname(s)!")

        self.add_item(TextInput(label="Enter your name here:", placeholder="Ron Swanson", min_length=2, max_length=50, required=True))
    
    async def interaction_check(self, interaction: Interaction):
        
        Introduction.create(user_id=interaction.user.id, name=self.items[0].value)
        await interaction.response.edit_message(embed=question2_ask_birth.birth_embed, view=question2_ask_birth.birth_view())

class name_view(View):
    def __init__(self):
        super().__init__(timeout=None)

    @Button(label="Enter your name", style=ButtonStyle.primary)
    async def get_name_button(self, interaction : Interaction, button : Button):
        logger.debug(f"Button: Get Name | User: {interaction.user}")
        interaction.response.send_modal(name_modal())