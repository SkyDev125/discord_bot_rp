import nextcord
from tools.modals import SimpleRefSheetModal


class SimpleRefView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.current_page = 0
        self.button_names = [
            "general_info",
            "cock_info",
            "powers_abilities_skills",
            "personality_lore_background",
            "sexual_pref",
        ]
        self.button_states = {
            name: nextcord.ButtonStyle.primary for name in self.button_names
        }
        self.button_disabled = {name: False for name in self.button_names}
        self.default_values = {name: {} for name in self.button_names}

    def update_button_styles(self):
        for name in self.button_names:
            button = getattr(self, name)
            button.style = self.button_states[name]
            button.disabled = self.button_disabled[name]

    # Add button for General Information modal
    @nextcord.ui.button(
        label="========== General Information ==========",
        style=nextcord.ButtonStyle.primary,
        row=0,
    )
    async def general_info(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        self.button_states["general_info"] = nextcord.ButtonStyle.secondary
        self.update_button_styles()
        modal = SimpleRefSheetModal(
            self, "general_info", self.default_values["general_info"]
        )
        await interaction.response.send_modal(modal)
        await interaction.followup.edit_message(
            message_id=interaction.message.id, view=self
        )

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
