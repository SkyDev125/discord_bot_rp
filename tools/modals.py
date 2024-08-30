from copy import deepcopy
import nextcord

from tools.embeds import REF_SHEET_EMBEDS

class SimpleRefSheetModal(nextcord.ui.Modal):
    def __init__(self, view, button_name, default_values=None):
        super().__init__(title="Reference Sheet")
        self.view = view
        self.button_name = button_name
        self.default_values = default_values or {}
        """
        -----------------------------------------------------------------------
        General Information
        -----------------------------------------------------------------------
        """

        # Adding fields to the modal with default values
        self.name = nextcord.ui.TextInput(
            label="Name",
            placeholder="Enter your character's name",
            required=True,
            max_length=40,
            default_value=self.default_values.get("name", ""),
        )
        self.add_item(self.name)

        self.age = nextcord.ui.TextInput(
            label="Age",
            placeholder="Enter your character's age",
            required=True,
            default_value=self.default_values.get("age", ""),
        )
        self.add_item(self.age)

        self.height = nextcord.ui.TextInput(
            label="Height",
            placeholder="Enter your character's height",
            required=True,
            default_value=self.default_values.get("height", ""),
        )
        self.add_item(self.height)

        self.weight = nextcord.ui.TextInput(
            label="Weight",
            placeholder="Enter your character's weight",
            required=True,
            default_value=self.default_values.get("weight", ""),
        )
        self.add_item(self.weight)

        self.species = nextcord.ui.TextInput(
            label="Species",
            placeholder="Enter your character's species",
            required=True,
            default_value=self.default_values.get("species", ""),
        )
        self.add_item(self.species)

    """
    -----------------------------------------------------------------------
    Validation Functions
    -----------------------------------------------------------------------
    """

    def validate_age(self, age: str) -> str:
        if not age.isdigit() or int(age) < 0:
            return "Age must be a positive number."
        return None

    def validate_height(self, height: str) -> str:
        if not height.isdigit() or int(height) < 0:
            return "height must be a positive number."
        return None

    def validate_weight(self, weight: str) -> str:
        if not weight.isdigit() or int(weight) < 0:
            return "weight must be a positive number."
        return None

        # self.build_type = nextcord.ui.Select(
        #     options=[
        #         nextcord.SelectOption(
        #             label="Bodybuilder", value="bodybuilder"
        #         ),
        #         nextcord.SelectOption(label="Ripped", value="ripped"),
        #         nextcord.SelectOption(label="Muscular", value="muscular"),
        #         nextcord.SelectOption(label="Athletic", value="athletic"),
        #         nextcord.SelectOption(label="Toned", value="toned"),
        #         nextcord.SelectOption(label="Fit", value="fit"),
        #         nextcord.SelectOption(label="Average", value="average"),
        #         nextcord.SelectOption(label="Lean", value="lean"),
        #         nextcord.SelectOption(label="Slim", value="slim"),
        #         nextcord.SelectOption(label="Petite", value="petite"),
        #         nextcord.SelectOption(label="Curvy", value="curvy"),
        #         nextcord.SelectOption(label="Stocky", value="stocky"),
        #         nextcord.SelectOption(label="Bulky", value="bulky"),
        #         nextcord.SelectOption(label="Heavyset", value="heavyset"),
        #         nextcord.SelectOption(label="Fat", value="fat"),
        #     ],
        # )
        # self.add_item(self.build_type)

        # """
        # -----------------------------------------------------------------------
        # Cock Information
        # -----------------------------------------------------------------------
        # """

        # self.cock_height = nextcord.ui.TextInput(
        #     label="Cock Height",
        #     placeholder="Enter your character's cock height",
        #     required=True,
        # )
        # self.add_item(self.cock_height)

        # self.ball_size = nextcord.ui.TextInput(
        #     label="Ball Size",
        #     placeholder="Enter your character's ball size",
        #     required=True,
        # )
        # self.add_item(self.ball_size)

        # """
        # -----------------------------------------------------------------------
        # Powers/Abilities/Skills
        # -----------------------------------------------------------------------
        # """

        # self.powers = nextcord.ui.TextInput(
        #     label="Powers",
        #     placeholder="Enter your character's powers",
        #     required=True,
        # )
        # self.add_item(self.powers)

        # self.abilities_skills = nextcord.ui.TextInput(
        #     label="Abilities/Skills",
        #     placeholder="Enter your character's abilities/skills",
        #     required=True,
        # )
        # self.add_item(self.abilities_skills)

        # """
        # -----------------------------------------------------------------------
        # Personality/Lore/Background
        # -----------------------------------------------------------------------
        # """

        # self.personality = nextcord.ui.TextInput(
        #     label="Personality",
        #     placeholder="Describe your character's personality",
        #     required=True,
        # )
        # self.add_item(self.personality)

        # self.lore_background = nextcord.ui.TextInput(
        #     label="Lore/Background",
        #     placeholder="Enter your character's lore/background",
        #     required=True,
        # )
        # self.add_item(self.lore_background)

        # self.likes = nextcord.ui.TextInput(
        #     label="Likes",
        #     placeholder="Enter your character's likes",
        #     required=True,
        # )
        # self.add_item(self.likes)

        # self.dislikes = nextcord.ui.TextInput(
        #     label="Dislikes",
        #     placeholder="Enter your character's dislikes",
        #     required=True,
        # )
        # self.add_item(self.dislikes)

        # """
        # -----------------------------------------------------------------------
        # Sexual Preferences
        # -----------------------------------------------------------------------
        # """

        # self.sexual_orientation = nextcord.ui.TextInput(
        #     label="Sexual Orientation",
        #     placeholder="Enter your character's sexual orientation",
        #     required=True,
        # )
        # self.add_item(self.sexual_orientation)

        # self.favorite_kinks = nextcord.ui.TextInput(
        #     label="Favorite Kinks",
        #     placeholder="Enter your character's main kinks",
        #     required=True,
        # )
        # self.add_item(self.favorite_kinks)

        # self.limits = nextcord.ui.TextInput(
        #     label="Limits",
        #     placeholder="Enter your character's main limits",
        #     required=True,
        # )
        # self.add_item(self.limits)

    async def callback(self, interaction: nextcord.Interaction):
        # Process the input data here
        print(self.default_values)
        self.default_values = {
            "name": self.name.value,
            "age": self.age.value,
            "height": self.height.value,
            "weight": self.weight.value,
            "species": self.species.value,
        }
        # build_type = self.build_type.value
        # cock_height = self.cock_height.value
        # ball_size = self.ball_size.value
        # powers = self.powers.value
        # abilities_skills = self.abilities_skills.value
        # personality = self.personality.value
        # lore_background = self.lore_background.value
        # likes = self.likes.value
        # dislikes = self.dislikes.value
        # sexual_orientation = self.sexual_orientation.value
        # favorite_kinks = self.favorite_kinks.value
        # limits = self.limits.value

        """
        -----------------------------------------------------------------------
        Validation Handling
        -----------------------------------------------------------------------
        """

        errors = {}

        # Dictionary of validation functions
        validation_functions = {
            "age": self.validate_age,
            "height": self.validate_height,
            "weight": self.validate_weight,
        }

        # Perform validations and collect errors
        for field, validate_function in validation_functions.items():
            value = getattr(self, field).value
            error = validate_function(value)
            if error:
                errors[field] = error

        if errors:
            # Update the button style to red, marking the input as invalid
            self.view.button_states[self.button_name] = (
                nextcord.ButtonStyle.danger
            )
            self.view.update_button_styles()

            # Remove the invalid fields from the default values
            for key in errors.keys():
                self.default_values.pop(key)

            # Update the error embed with the errors
            error_embed = deepcopy(REF_SHEET_EMBEDS["Errors"])
            error_embed.description += "\n\n" + "\n".join(errors.values())
            existing_embeds = interaction.message.embeds
            error_embed_exists = False

            for embed in existing_embeds:
                if embed.title == error_embed.title:
                    embed.description = error_embed.description
                    error_embed_exists = True
                    break

            if not error_embed_exists:
                existing_embeds.append(error_embed)
            print(self.default_values)

            # Send an ephemeral message to the user with the errors
            await interaction.response.send_message(
                "There were errors with your input, check above for more information.",
                ephemeral=True,
                delete_after=5,
            )
            await interaction.followup.edit_message(
                message_id=interaction.message.id,
                view=self.view,
                embeds=existing_embeds,
            )
            return

        """
        -----------------------------------------------------------------------
        Input Handling
        -----------------------------------------------------------------------
        """

        # Update the button style to success and disable it
        self.view.button_states[self.button_name] = (
            nextcord.ButtonStyle.success
        )
        self.view.button_disabled[self.button_name] = True
        self.view.update_button_styles()

        # Remove the error embed if it exists
        existing_embeds = interaction.message.embeds
        error_embed_title = REF_SHEET_EMBEDS["Errors"].title
        existing_embeds = [
            embed
            for embed in existing_embeds
            if embed.title != error_embed_title
        ]

        # Respond with the input data
        await interaction.response.send_message(
            f"Name: {self.default_values["name"]}\n"
            f"Age: {self.default_values["age"]}\n"
            f"Height: {self.default_values["height"]}\n"
            f"Weight: {self.default_values["weight"]}\n"
            f"Species: {self.default_values["species"]}"
            # f"Build Type: {build_type}\n"
            # f"Cock Height: {cock_height}\n"
            # f"Ball Size: {ball_size}\n"
            # f"Powers: {powers}\n"
            # f"Abilities/Skills: {abilities_skills}\n"
            # f"Personality: {personality}\n"
            # f"Lore/Background: {lore_background}\n"
            # f"Likes: {likes}\n"
            # f"Dislikes: {dislikes}\n"
            # f"Sexual Orientation: {sexual_orientation}\n"
            # f"Favorite Kinks: {favorite_kinks}\n"
            # f"Limits: {limits}"
            ,
            ephemeral=True,
        )
        await interaction.followup.edit_message(
            message_id=interaction.message.id,
            view=self.view,
            embeds=existing_embeds,
        )
