from discord.ui import Select, View
from discord import Embed, Interaction, SelectOption
from database.tables import Introduction

from . import question3_ask_reason

import logging

logger = logging.getLogger("cyan")

birth_embed = Embed(title="Roughly how old are you?", 
                    description="Hint: Click the dropdown menu below and pick the range that fits you!\n\nPlease do note we don't accept applicants under the age of 13 due to Discord's Terms of Service.",
                    color=0x00ffff,)
birth_embed.set_thumbnail(url="https://raw.githubusercontent.com/Society-of-the-Cyan-Rose/cyan-rose-discord-bot/main/src/assets/cyan-rose.png")

class birth_view(View):
    def __init__(self):
        super().__init__(timeout=None)

        logger.debug("Dropdown: Birth - quesiton2.5 - introductions | initialization")

        self.birth_ranges = [
            SelectOption(label="13-17", value="13-17"),
            SelectOption(label="18-22", value="18-22"),
            SelectOption(label="23-27", value="23-27"),
            SelectOption(label="28-32", value="28-32"),
            SelectOption(label="33-37", value="33-37"),
            SelectOption(label="38-42", value="38-42"),
            SelectOption(label="43-47", value="43-47"),
            SelectOption(label="48-52", value="48-52"),
            SelectOption(label="52+", value="52+"),
        ]
        self.dropdown : Select = Select(custom_id="birth", placeholder="Select your birth year range", options=self.birth_ranges)
        self.add_item(self.dropdown)

        logger.debug("Dropdown: Birth - quesiton2.5 - introductions | initialized")

    async def interaction_check(self, interaction: Interaction):
        logger.debug(f"Dropdown: Birth | User: {interaction.user}")

        if Introduction.select().where(Introduction.user_id == interaction.user.id, Introduction.part == 1).exists():
            Introduction.update(introduction=self.dropdown.values[0]).where(Introduction.user_id == interaction.user.id, Introduction.part == 1).execute()
            logger.debug("Updated user's birth year range in the database.")
        else:
            Introduction.create(user_id=interaction.user.id, part=1, introduction=f"age range = {self.dropdown.values[0]}")
            logger.debug("Added user's birth year range to the database.")
        logger.debug(f"Passing to: question3_ask_reason")
        await interaction.response.edit_message(embed=question3_ask_reason.reason_embed, view=question3_ask_reason.reason_view())

    