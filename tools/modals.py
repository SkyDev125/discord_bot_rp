import nextcord


class SimpleRefSheetModal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(title="Reference Sheet")

        """
        -----------------------------------------------------------------------
        General Information
        -----------------------------------------------------------------------
        """

        # Adding fields to the modal
        self.name = nextcord.ui.TextInput(
            label="Name",
            placeholder="Enter your character's name",
            required=True,
        )
        self.add_item(self.name)

        self.age = nextcord.ui.TextInput(
            label="Age",
            placeholder="Enter your character's age",
            required=True,
        )
        self.add_item(self.age)

        self.height = nextcord.ui.TextInput(
            label="Height",
            placeholder="Enter your character's height",
            required=True,
        )
        self.add_item(self.height)

        self.weight = nextcord.ui.TextInput(
            label="Weight",
            placeholder="Enter your character's weight",
            required=True,
        )
        self.add_item(self.weight)

        self.species = nextcord.ui.TextInput(
            label="Species",
            placeholder="Enter your character's species",
            required=True,
        )
        self.add_item(self.species)

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
        name = self.name.value
        age = self.age.value
        height = self.height.value
        weight = self.weight.value
        species = self.species.value
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

        # Respond to the user
        await interaction.response.send_message(
            f"Name: {name}\n"
            f"Age: {age}\n"
            f"Height: {height}\n"
            f"Weight: {weight}\n"
            f"Species: {species}\n"
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
        )
