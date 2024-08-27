import nextcord
from nextcord.ext import commands
from settings import TESTING_GUILD_ID


class SizeCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        description="Command for changing sizes!",
        guild_ids=[TESTING_GUILD_ID],
    )
    async def size(self, interaction: nextcord.Interaction):
        await interaction.send("hello!! time to change sizes~")


# Add the cog to the bot
def setup(bot: commands.Bot):
    bot.add_cog(SizeCommand(bot))
