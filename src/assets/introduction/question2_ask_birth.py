from discord.ui import Button, View, Modal, TextInput, button
from discord import Embed, ButtonStyle, Interaction
from database.tables import Introduction

from datetime import datetime

from . import question2_point_5_pnts_birth, question3_ask_reason

import logging

logger = logging.getLogger("cyan")

birth_embed = Embed(title="When were you born?", 
                    description="Hint: Click the button below and enter your date of birth! If you don't feel comfortable sharing your date of birth, you can click the 'Prefer not to share' button!\n\nPlease do note we don't accept applicants under the age of 13 due to Discord's Terms of Service.",
                    color=0x00ffff,)
birth_embed.set_thumbnail(url="https://raw.githubusercontent.com/Society-of-the-Cyan-Rose/cyan-rose-discord-bot/main/src/assets/cyan-rose.png")

class birth_modal(Modal):
    def __init__(self):
        super().__init__(timeout=None, title="Enter your date of birth!")
        
        self.birth_input = TextInput(label="Enter your date of birth here:", placeholder="DD/MM/YYYY", min_length=10, max_length=10, required=True)
        self.add_item(self.birth_input)
    
    async def interaction_check(self, interaction: Interaction):
        
        # Validate Date
        try:
            day, month, year = self.birth_input.value.split("/")
            day, month, year = int(day), int(month), int(year)
        except ValueError:
            return await interaction.response.send_message("Invalid date format! Please enter your date of birth in the following format: DD/MM/YYYY")
        
        if day < 1 or day > 31:
            return await interaction.response.send_message("Invalid day! Please enter a day between 1 and 31.")
        if month < 1 or month > 12:
            return await interaction.response.send_message("Invalid month! Please enter a month between 1 and 12.")
        if year < 1900 or year > int(datetime.now().year) + 1:
            return await interaction.response.send_message(f"Invalid year! Please enter a year between 1900 and {int(datetime.now().year)}.")

        if Introduction.select().where(Introduction.user_id == interaction.user.id, Introduction.part == 1).exists():
            Introduction.update(introduction=self.birth_input.value).where(Introduction.user_id == interaction.user.id, Introduction.part == 1).execute()
        else:
            Introduction.create(user_id=interaction.user.id, part=1, introduction=f"{self.birth_input.value}")
        await interaction.response.edit_message(embed=question3_ask_reason.reason_embed, view=question3_ask_reason.reason_view())

class birth_view(View):
    def __init__(self):
        super().__init__(timeout=None)

    @button(label="Enter your date of birth", style=ButtonStyle.primary)
    async def get_birth_button(self, interaction : Interaction, button : Button):
        logger.debug(f"Button: Get Birth | User: {interaction.user}")
        await interaction.response.send_modal(birth_modal())
    
    @button(label="Prefer not to share", style=ButtonStyle.danger)
    async def prefer_not_to_share_button(self, interaction : Interaction, button : Button):
        logger.debug(f"Button: Prefer Not To Share | User: {interaction.user}")
        await interaction.response.edit_message(embed=question2_point_5_pnts_birth.birth_embed, view=question2_point_5_pnts_birth.birth_view())