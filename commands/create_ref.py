import nextcord
from nextcord.ext import commands
from settings import TESTING_GUILD_ID


class CreateRefCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        description="Create a modular ref sheet!",
        guild_ids=[TESTING_GUILD_ID],
    )
    async def create_ref(self, interaction: nextcord.Interaction):
        await interaction.send("hello!! time to create a ref sheet! :P")


# Add the cog to the bot
def setup(bot: commands.Bot):
    bot.add_cog(CreateRefCommand(bot))
