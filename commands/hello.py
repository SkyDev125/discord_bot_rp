import nextcord
from nextcord.ext import commands
from settings import TESTING_GUILD_ID


class HelloCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        description="Test command to say hello!",
        guild_ids=[TESTING_GUILD_ID],
    )
    async def hello(self, interaction: nextcord.Interaction):
        await interaction.send("hello!! :P")


# Add the cog to the bot
def setup(bot: commands.Bot):
    bot.add_cog(HelloCommand(bot))
