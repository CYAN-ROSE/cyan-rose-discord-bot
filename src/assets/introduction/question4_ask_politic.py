from discord.ui import Button, View, Modal, TextInput, button
from discord import Embed, ButtonStyle, Interaction, TextStyle
from database.tables import Introduction
from engines import introduction as intro_engine

from bot import client

import logging

logger = logging.getLogger("cyan")

politic_embed = Embed(title="What is your political stance?",
                    description="Hint: Click the button below to explain in short what your political stance is!",
                    color=0x00ffff,)
politic_embed.set_thumbnail(url="https://raw.githubusercontent.com/Society-of-the-Cyan-Rose/cyan-rose-discord-bot/main/src/assets/cyan-rose.png")

class politic_modal(Modal):
    def __init__(self):
        super().__init__(timeout=None, title="Explain your political stance!")
        
        self.politic_input = TextInput(label="Explain your political stance here:", placeholder="I am a...", min_length=10, max_length=500, style=TextStyle.paragraph, required=True)
        self.add_item(self.politic_input)
    
    async def interaction_check(self, interaction: Interaction):
        
        if Introduction.select().where(Introduction.user_id == interaction.user.id, Introduction.part == 3).exists():
            Introduction.update(introduction=self.politic_input.value).where(Introduction.user_id == interaction.user.id, Introduction.part == 3).execute()
        else:
            Introduction.create(user_id=interaction.user.id, part=3, introduction=self.politic_input.value)
        await interaction.response.edit_message(content="Thank you for your response! Your application has been submitted and will be reviewed by our staff team. We will get back to you as soon as possible!", embed=None, view=None)

        channel = await client.fetch_channel(1222036326019498005)
        await channel.send(embed=intro_engine.build(interaction))

class politic_view(View):
    def __init__(self):
        super().__init__(timeout=None)

    @button(label="Explain your political stance", style=ButtonStyle.primary)
    async def get_politic_button(self, interaction : Interaction, button : Button):
        logger.debug(f"Button: Get Politic | User: {interaction.user}")
        await interaction.response.send_modal(politic_modal())