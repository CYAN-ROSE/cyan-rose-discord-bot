from discord.ui import Button, View, button
from discord import Embed, ButtonStyle, Interaction

from . import question1_ask_name

import logging

logger = logging.getLogger("cyan")

disclosure_embed = Embed(title="The Interview Process", 
                    description="We are going to ask you a few important questions that will help us determine if you would be a good fit. ",
                    color=0x00ffff,)
disclosure_embed.set_thumbnail(url="https://raw.githubusercontent.com/Society-of-the-Cyan-Rose/cyan-rose-discord-bot/main/src/assets/cyan-rose.png")
disclosure_embed.add_field(name="What do we do with your information?", value="Any information here is stored in a database that is uploaded to the publically accessable GitHub repo for our in-house, Cyan Rose bot. The answers to your questions will go to the moderators of the server, and once they approve, you will be added to the server, and this will act as your introduction message! (the entire server will be able to see it.)", inline=False)
disclosure_embed.add_field(name="What if I don't want to answer a question?", value="You are able to input text as an answer to each question, if you don't feel like answering something, put that into your message. An example is, for political view, you may say, 'I would rather not say.'. just do keep in mind that this will affect the mods decision.", inline=False)
disclosure_embed.add_field(name="To continue...", value="Click the button below to continue to the first question.", inline=False)

class disclosure_view(View):
    def __init__(self):
        super().__init__(timeout=None, title="The Interview Process")
        
    @button(label="Continue", style=ButtonStyle.primary)
    async def continue_button(self, interaction : Interaction, button : Button):
        logger.debug(f"Button: Continue | User: {interaction.user}")
        await interaction.response.edit_message(embed=question1_ask_name.name_embed, view=question1_ask_name.name_view())