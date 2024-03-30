from discord.ui import Button, View, Modal, TextInput, button
from discord import Embed, ButtonStyle, Interaction
from database.tables import Introduction

from . import question2_ask_birth

import logging

logger = logging.getLogger("cyan")

name_embed = Embed(title="What's your name?", 
                   description="Hint: Click the button below and enter your name(s) or nickname(s)!",
                   color=0x00ffff,)
name_embed.set_thumbnail(url="https://raw.githubusercontent.com/Society-of-the-Cyan-Rose/cyan-rose-discord-bot/main/src/assets/cyan-rose.png")

class name_modal(Modal):
    def __init__(self):
        super().__init__(timeout=None, title="Enter your name(s) or nickname(s)!")

        self.name_input = TextInput(label="Enter your name here:", placeholder="Ron Swanson", min_length=2, max_length=50, required=True)
        self.add_item(self.name_input)
    
    async def interaction_check(self, interaction: Interaction):

        if Introduction.select().where(Introduction.user_id == interaction.user.id, Introduction.part == 0).exists():
            Introduction.update(introduction=self.name_input.value).where(Introduction.user_id == interaction.user.id, Introduction.part == 0).execute()
        else:
            Introduction.create(user_id=interaction.user.id, part=0, introduction=self.name_input.value)
        await interaction.response.edit_message(embed=question2_ask_birth.birth_embed, view=question2_ask_birth.birth_view())

class name_view(View):
    def __init__(self):
        super().__init__(timeout=None)

    @button(label="Enter your name", style=ButtonStyle.primary)
    async def get_name_button(self, interaction : Interaction, button : Button):
        logger.debug(f"Button: Get Name | User: {interaction.user}")
        await interaction.response.send_modal(name_modal())