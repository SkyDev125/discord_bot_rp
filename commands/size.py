import nextcord
from nextcord.ext import commands
from settings import TESTING_GUILD_ID
from tools.auto_complete import fuzzysearch


class SizeCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    """
    ---------------------------------------------------------------------------
    Parent Command
    ---------------------------------------------------------------------------
    """

    @nextcord.slash_command(
        description="Size related commands!",
        guild_ids=[TESTING_GUILD_ID],
    )
    async def size(self, interaction: nextcord.Interaction):
        pass  # This is the parent command, it won't be used directly.

    """  
    ---------------------------------------------------------------------------
    Subcommands 
    ---------------------------------------------------------------------------
    """

    @size.subcommand(description="Add extra size to yourself")
    async def add(
        self,
        interaction: nextcord.Interaction,
    ):
        await interaction.response.send_message(f"Adding size", ephemeral=True)

    @size.subcommand(description="Edit existing size")
    async def edit(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(
            f"Editing size", ephemeral=True
        )

    @size.subcommand(description="Steal size from another")
    async def steal(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f"Steal size", ephemeral=True)

    @size.subcommand(description="Give size to another")
    async def give(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f"Give size", ephemeral=True)

    @size.subcommand(description="Remove size from yourself")
    async def remove(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f"Remove size", ephemeral=True)

    """  
    ---------------------------------------------------------------------------
    Auto Complete Functions
    ---------------------------------------------------------------------------
    """


# Add the cog to the bot
def setup(bot: commands.Bot):
    bot.add_cog(SizeCommand(bot))
