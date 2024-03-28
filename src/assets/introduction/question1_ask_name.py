from discord.ui import Button, View, Modal, TextInput
from discord import Embed, ButtonStyle, Interaction
from discord.ext import commands
from database.tables import Introduction

from . import question2_ask_birth

import logging

logger = logging.getLogger("cyan")

name_embed = Embed(title="What's your name?", description="Hint: Click the button below and enter your name!s")

class name_modal(Modal):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(TextInput(label="Enter your name here:", placeholder="Ron Swanson", min_length=2, max_length=50, required=True))
    
    async def interaction_check(self, interaction: Interaction):
        if interaction.user.id != self.message.author.id:
            return
        
        Introduction.create(user_id=interaction.user.id, name=self.items[0].value)
        await interaction.message.edit(embed=question2_ask_birth.birth_embed, view=question2_ask_birth.birth_view())

class name_view(View):
    def __init__(self):
        super().__init__(timeout=None)

    @Button(label="Enter your name", style=ButtonStyle.primary)
    async def get_name_button(self, interaction : Interaction, button : Button):
        logger.debug(f"Button: Get Name | User: {interaction.user}")