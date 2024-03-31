from discord.ui import Button, View, Modal, TextInput, button
from discord import Embed, ButtonStyle, Interaction, TextStyle
from database.tables import Introduction
from engines import introduction as intro_engine

from bot import client

import logging

logger = logging.getLogger("cyan")

politic_embed = Embed(title="Finally, what's your political leaning?",
                    description=(
                      "You should talk about what you actually "
                      "believe, not just a party you support. "
                      "If you do not know the technical terms, you "
                      "can just use normal sentences. In fact, it's "
                      "good to clarify, since labels mean slightly "
                      "different things to different people."
                    ),
                    color=0x00ffff,)
politic_embed.set_thumbnail(url="https://raw.githubusercontent.com/Society-of-the-Cyan-Rose/cyan-rose-discord-bot/main/src/assets/cyan-rose.png")

class politic_modal(Modal):
    def __init__(self):
        super().__init__(timeout=None, title="What's your political leaning?")
        
        self.politic_input = TextInput(label="Explain it here:", placeholder="I am a...", min_length=10, max_length=500, style=TextStyle.paragraph, required=True)
        self.add_item(self.politic_input)
    
    async def interaction_check(self, interaction: Interaction):
        
        if Introduction.select().where(Introduction.user_id == interaction.user.id, Introduction.part == 3).exists():
            Introduction.update(introduction=self.politic_input.value).where(Introduction.user_id == interaction.user.id, Introduction.part == 3).execute()
            logger.debug(f"Updated political stance for user: {interaction.user}")
        else:
            Introduction.create(user_id=interaction.user.id, part=3, introduction=self.politic_input.value)
            logger.debug(f"Created political stance for user: {interaction.user}")
        await interaction.response.edit_message(content="Thank you for your response! Your application has been submitted and will be reviewed by our staff team. We will get back to you as soon as possible!", embed=None, view=None)

        logger.debug(f"Passing to: introduction engine")
        channel = await client.fetch_channel(1222036326019498005) # Fetch Moderation Channel
        await channel.send(embed=intro_engine.build(interaction))

class politic_view(View):
    def __init__(self):
        super().__init__(timeout=None)

    @button(label="i think...", style=ButtonStyle.primary)
    async def get_politic_button(self, interaction : Interaction, button : Button):
        logger.debug(f"Button: Get Politic - question4 - introduction | User: {interaction.user}")
        await interaction.response.send_modal(politic_modal())
