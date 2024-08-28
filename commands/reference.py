import nextcord
from nextcord.ext import commands
from settings import TESTING_GUILD_ID
import difflib

# Define the options
REF_COMMANDS = ["Create", "Edit", "View", "Delete"]
REF_TYPE = ["Simple", "Detailed", "Custom"]


class RefSheetCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        description="Ref sheet related commands!",
        guild_ids=[TESTING_GUILD_ID],
    )
    async def ref(self, interaction: nextcord.Interaction):
        return

    async def ref_type(self, interaction: nextcord.Interaction, ref: str):
        if not ref:
            # send the full autocomplete list
            await interaction.response.send_autocomplete(REF_TYPE)
        else:
            get_aproximate_command = difflib.get_close_matches(
                ref, REF_TYPE, n=5, cutoff=0.1
            )
            await interaction.response.send_autocomplete(
                get_aproximate_command
            )

    @ref.subcommand(description="Create a new ref sheet")
    async def create(
        self,
        interaction: nextcord.Interaction,
        ref_type: str = nextcord.SlashOption(
            description="The type of ref sheet to create",
            autocomplete_callback=ref_type,
        ),
    ):
        return await interaction.response.send_message(
            f"Creating a new {ref_type} ref sheet!", ephemeral=True
        )

    @ref.subcommand(description="Edit an existing ref sheet")
    async def edit(self, interaction: nextcord.Interaction):
        return await interaction.response.send_message(
            f"Editing an existing ref sheet!", ephemeral=True
        )

    @ref.subcommand(description="View an existing ref sheet")
    async def view(self, interaction: nextcord.Interaction):
        return await interaction.response.send_message(
            f"Viewing an existing ref sheet!", ephemeral=True
        )

    @ref.subcommand(description="Delete an existing ref sheet")
    async def delete(self, interaction: nextcord.Interaction):
        return await interaction.response.send_message(
            f"Deleting an existing ref sheet!", ephemeral=True
        )


# Add the cog to the bot
def setup(bot: commands.Bot):
    bot.add_cog(RefSheetCommand(bot))
