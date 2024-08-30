import nextcord
from nextcord.ext import commands
from settings import TESTING_GUILD_ID
from tools.auto_complete import fuzzysearch
from tools.pages import SimpleRefView
from tools.embeds import REF_SHEET_EMBEDS

# Define the options
REF_COMMANDS = ["Create", "Edit", "View", "Delete"]
REF_TYPE = ["Simple", "Detailed", "Custom"]


class RefSheetCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    """
    ---------------------------------------------------------------------------
    Parent Command
    ---------------------------------------------------------------------------
    """

    @nextcord.slash_command(
        description="Ref sheet related commands!",
        guild_ids=[TESTING_GUILD_ID],
    )
    async def ref(self, interaction: nextcord.Interaction):
        pass  # This is the parent command, it won't be used directly.

    """  
    ---------------------------------------------------------------------------
    Subcommands 
    ---------------------------------------------------------------------------
    """

    @ref.subcommand(description="Create a new ref sheet")
    async def create(
        self,
        interaction: nextcord.Interaction,
        ref_type: str = nextcord.SlashOption(
            description="The type of ref sheet to create"
        ),
    ):
        # get uuid of person who used the command
        user_id = interaction.user.id

        match ref_type:
            case "Simple":
                # Create the embeds for different pages

                # Send the first embed with the paginator view
                view = SimpleRefView()
                await interaction.response.send_message(
                    view=view, embed=REF_SHEET_EMBEDS["Simple"], ephemeral=True
                )

            case "Detailed":
                await interaction.response.send_message(
                    f"Creating a new detailed  {ref_type} ref sheet for {user_id}!",
                    ephemeral=True,
                )
            case "Custom":
                await interaction.response.send_message(
                    f"Creating a new custom {ref_type} ref sheet for {user_id}!",
                    ephemeral=True,
                )
            case _:
                await interaction.response.send_message(
                    "Invalid ref type", ephemeral=True
                )

    @ref.subcommand(description="Edit an existing ref sheet")
    async def edit(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(
            f"Editing an existing ref sheet!", ephemeral=True
        )

    @ref.subcommand(description="View an existing ref sheet")
    async def view(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(
            f"Viewing an existing ref sheet!", ephemeral=True
        )

    @ref.subcommand(description="Delete an existing ref sheet")
    async def delete(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(
            f"Deleting an existing ref sheet!", ephemeral=True
        )

    """  
    ---------------------------------------------------------------------------
    Auto Complete Functions
    ---------------------------------------------------------------------------
    """

    @create.on_autocomplete("ref_type")
    async def ref_type_autocomplete(
        self, interaction: nextcord.Interaction, type: str
    ):
        if not type:
            await interaction.response.send_autocomplete(REF_TYPE)
        else:
            await interaction.response.send_autocomplete(
                fuzzysearch(type, REF_TYPE, 2, 0.1)
            )


# Add the cog to the bot
def setup(bot: commands.Bot):
    bot.add_cog(RefSheetCommand(bot))
