# settings.py
import os
import logging
from dotenv import load_dotenv
import nextcord

# Load the .env file
load_dotenv()

# Access the environment variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
TESTING_GUILD_ID = int(os.getenv("TESTING_GUILD_ID"))

# Set up logging
logger = logging.getLogger("nextcord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="SkyRP.log", encoding="utf-8", mode="w")
handler.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)
logger.addHandler(handler)

# Set up Intents
intents = nextcord.Intents.default()
intents.message_content = True