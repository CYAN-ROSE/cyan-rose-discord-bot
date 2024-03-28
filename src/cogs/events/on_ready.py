from discord.ext import commands
import logging

logger = logging.getLogger("cyan")

class OnReady(commands.Cog):
    """Cog for the on_ready event."""
    
    def __init__(self, client: commands.Bot):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        """Event that triggers when the bot is ready."""
        
        logger.info(f"Logged in as {self.client.user} ({self.client.user.id})")

        await self.client.tree.sync() # Sync the tree

async def setup(client: commands.Bot):
    """Setup function for the on_ready cog."""
    client.add_cog(OnReady(client))