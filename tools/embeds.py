import nextcord


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
    ),
    "Errors": nextcord.Embed(
        title="Errors",
        description=(
            "There was an error submitting the form. Please try again. :x:"
        ),
    ),
}
