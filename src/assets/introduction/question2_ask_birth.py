from discord.ui import Button, View, Modal, TextInput
from discord import Embed, ButtonStyle, Interaction
from database.tables import Introduction

from . import question2_point_5_pnts_birth

import logging

logger = logging.getLogger("cyan")

birth_embed = Embed(title="When were you born?", 
                    description="Hint: Click the button below and enter your date of birth! if you don't feel comfortable sharing your date of birth, you can click the 'Prefer not to share' button!\n\nPlease do note we do not applicants under the age of 13 due to Discord's Terms of Service.",
                    color=0x00ffff,)
birth_embed.set_thumbnail(url="src/assets/cyan-rose.png")

class birth_modal(Modal):
    def __init__(self):
        super().__init__(timeout=None, title="Enter your date of birth!")
        
        self.add_item(TextInput(label="Enter your date of birth here:", placeholder="DD/MM/YYYY", min_length=10, max_length=10, required=True))
    
    async def interaction_check(self, interaction: Interaction):
        
        Introduction.create(user_id=interaction.user.id, part=1, introduction=f"{self.items[0].value}")
        await interaction.response.edit_message(embed=None, view=None)

class birth_view(View):
    def __init__(self):
        super().__init__(timeout=None)

    @Button(label="Enter your date of birth", style=ButtonStyle.primary)
    async def get_birth_button(self, interaction : Interaction, button : Button):
        logger.debug(f"Button: Get Birth | User: {interaction.user}")
        interaction.response.send_modal(birth_modal())
    
    @Button(label="Prefer not to share", style=ButtonStyle.danger)
    async def prefer_not_to_share_button(self, interaction : Interaction, button : Button):
        logger.debug(f"Button: Prefer Not To Share | User: {interaction.user}")
        Introduction.update(birth="Prefer not to share").where(Introduction.user_id == interaction.user.id).execute()
        await interaction.message.edit(embed=question2_point_5_pnts_birth.birth_embed, view=question2_point_5_pnts_birth.birth_view())