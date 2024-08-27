from nextcord.ext import commands
from settings import DISCORD_TOKEN, intents
import os

bot = commands.Bot(intents=intents)


# load events
def load_events(bot: commands.Bot):
    events_dir = os.path.join(os.path.dirname(__file__), "events")

    for filename in os.listdir(events_dir):
        if filename.endswith(".py") and not filename.startswith("_"):
            event_name = filename[:-3]  # Remove the .py extension
            bot.load_extension(f"events.{event_name}")


# Load the cogs
load_events(bot)

# Run the bot
bot.run(DISCORD_TOKEN)
