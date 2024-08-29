import nextcord
from tools.modals import SimpleRefSheetModal

REF_SHEET_EMBEDS = {
    "Simple": nextcord.Embed(
        title="Building Reference Sheet",
        description=(
            "Click the buttons and submit the information for your new ref! :pencil:\n\n"
            "**Button Colours:**\n"
            "- Blue -> Not Opened\n"
            "- Grey -> Opened but not submitted.\n"
            "- Green -> Successfully submitted\n"
            "- Red -> Failed to submit"
        ),
    )
}


class PaginationView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.current_page = 0
        self.button_states = {
            "general_info": nextcord.ButtonStyle.primary,
            "cock_info": nextcord.ButtonStyle.primary,
            "powers_abilities_skills": nextcord.ButtonStyle.primary,
            "personality_lore_background": nextcord.ButtonStyle.primary,
            "sexual_pref": nextcord.ButtonStyle.primary,
        }



    # Add button for General Information modal
    @nextcord.ui.button(
        label="========== General Information ==========",
        style=nextcord.ButtonStyle.primary,
        row=0,
    )
    async def general_info(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        modal = SimpleRefSheetModal()
        await interaction.response.send_modal(modal)

    # Add button for Cock Information
    @nextcord.ui.button(
        label="=========== Cock Information ===========",
        style=nextcord.ButtonStyle.primary,
        row=1,
    )
    async def cock_info(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        modal = SimpleRefSheetModal()
        await modal.start(interaction)

    # Add button for Powers/Abilities/Skills
    @nextcord.ui.button(
        label="========= Powers/Abilities/Skills =========",
        style=nextcord.ButtonStyle.primary,
        row=2,
    )
    async def powers_abilities_skills(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        modal = SimpleRefSheetModal()
        await modal.start(interaction)

    # Add button for Personality/Lore/Background
    @nextcord.ui.button(
        label="====== Personality/Lore/Background ======",
        style=nextcord.ButtonStyle.primary,
        row=3,
    )
    async def personality_lore_background(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        modal = SimpleRefSheetModal()
        await modal.start(interaction)

    # Add button for Sexual Preferences
    @nextcord.ui.button(
        label="========== Sexual Preferences ===========",
        style=nextcord.ButtonStyle.primary,
        row=4,
    )
    async def sexual_pref(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        modal = SimpleRefSheetModal()
        await modal.start(interaction)
