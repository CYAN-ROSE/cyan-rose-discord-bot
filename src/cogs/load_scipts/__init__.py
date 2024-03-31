# src/cogs/load_scripts/__init__.py

from . import load_commands, load_events, load_tasks

async def all(client):
    """Load all scripts."""
    await load_commands.load_commands(client)
    await load_events.load_events(client)
    await load_tasks.load_tasks(client)

async def reload_all(client):
    """Reload all scripts."""
    await load_commands.load_commands(client, reload=True)
    await load_events.load_events(client, reload=True)
    await load_tasks.load_tasks(client, reload=True)
