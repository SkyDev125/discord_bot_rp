import nextcord
from nextcord.ext import commands
from settings import TESTING_GUILD_ID


class StealCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        description="Command for stealing sizes",
        guild_ids=[TESTING_GUILD_ID],
    )
    async def steal(self, interaction: nextcord.Interaction):
        await interaction.send("hello!! ready to steal?~")


# Add the cog to the bot
def setup(bot: commands.Bot):
    bot.add_cog(StealCommand(bot))
