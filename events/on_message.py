import re
import nextcord
from nextcord.ext import commands

# Define a list of dictionaries for solo Units
units = [
    {
        "imperic_names": ("inch", "inches", '"', "''", "´´", "``"),
        "metric_names": ("centimeter", "centimeters", "cm"),
        "conversion_factor": 2.54,
        "regex": r"(\d*\.?\d+)\s*(inches|inch|''|\"|``|´´)",
    },
    {
        "imperic_names": ("foot", "feet", "ft", "'"),
        "metric_names": ("meter", "meters", "m"),
        "conversion_factor": 0.3048,
        "regex": r"(\d*\.?\d+)\s*(feet|foot|ft|')(?!')",
    },
    {
        "imperic_names": ("yard", "yards", "yd"),
        "metric_names": ("meter", "meters", "m"),
        "conversion_factor": 91.44,
        "regex": r"(\d*\.?\d+)\s*(yards|yard|yd)",
    },
    {
        "imperic_names": ("mile", "miles", "mi"),
        "metric_names": ("kilometer", "kilometers", "km"),
        "conversion_factor": 1.60934,
        "regex": r"(\d*\.?\d+)\s*(miles|mile|mi)",
    },
    {
        "imperic_names": ("ounce", "ounces", "oz"),
        "metric_names": ("gram", "grams", "g"),
        "conversion_factor": 28.3495,
        "regex": r"(\d*\.?\d+)\s*(ounces|ounce|oz)",
    },
    {
        "imperic_names": ("pound", "pounds", "lb"),
        "metric_names": ("kilogram", "kilograms", "kg"),
        "conversion_factor": 0.453592,
        "regex": r"(\d*\.?\d+)\s*(pounds|pound|lb)",
    },
    {
        "imperic_names": ("stone", "stones", "st"),
        "metric_names": ("kilogram", "kilograms", "kg"),
        "conversion_factor": 6.35029,
        "regex": r"(\d*\.?\d+)\s*(stones|stone|st)",
    },
    {
        "imperic_names": ("fahrenheit", "fahrenheit", "f"),
        "metric_names": ("degree celsius", "degrees celsius", "°C"),
        "conversion_factor": 5 / 9,
        "regex": r"(\d*\.?\d+)\s*(?:degrees|degree|°)\s*(fahrenheit|f)",
    },
]

# Define a list of dictionaries for combined Units
combined_patterns = [
    {
        "regex": re.compile(
            r"(\d*\.?\d+)\s*(feet|foot|ft|')\s*(?:and\s*)?(\d*\.?\d+)\s*(inches|inch|''|\"|``|´´)",
            re.IGNORECASE,
        ),
        "first_unit_factor": 0.3048,
        "second_unit_factor": 2.54,
        "first_to_second_unit_factor": 100,
        "unit_name": "m",
    },
    {
        "regex": re.compile(
            r"(\d*\.?\d+)\s*(stones|stone|st)\s*(?:and\s*)?(\d*\.?\d+)\s*(ounces|ounce|oz)",
            re.IGNORECASE,
        ),
        "first_unit_factor": 6.35029,
        "second_unit_factor": 28.3495,
        "first_to_second_unit_factor": 1000,
        "unit_name": "kg",
    },
    {
        "regex": re.compile(
            r"(\d*\.?\d+)\s*(miles|mile|mi)\s*(?:and\s*)?(\d*\.?\d+)\s*(yards|yard|yd)",
            re.IGNORECASE,
        ),
        "first_unit_factor": 1.60934,
        "second_unit_factor": 0.9144,
        "first_to_second_unit_factor": 1000,
        "unit_name": "km",
    },
]


def convert_combined_units(
    match, unit1_factor, unit2_factor, unit2_to_unit1_factor, unit_name
):
    value1 = float(match.group(1))
    value2 = float(match.group(3))

    # Convert both units to the metric system
    metric_value1 = value1 * unit1_factor
    metric_value2 = value2 * unit2_factor

    # Combine the results into a single metric value
    combined_metric_value = metric_value1 + (
        metric_value2 / unit2_to_unit1_factor
    )

    # Return the combined metric value as a string
    return f"{combined_metric_value:.2f} {unit_name}"


def replace_with_metric(sentence: str) -> str:
    # Handle combined units first
    for combined_pattern in combined_patterns:
        sentence = combined_pattern["regex"].sub(
            lambda match: convert_combined_units(
                match,
                combined_pattern["first_unit_factor"],
                combined_pattern["second_unit_factor"],
                combined_pattern["first_to_second_unit_factor"],
                combined_pattern["unit_name"],
            ),
            sentence,
        )

    # Iterate over the units
    for unit in units:
        # Find all matches of the regex pattern in the sentence
        pattern = re.compile(unit["regex"], re.IGNORECASE)

        def replace_match(match):
            number = match.group(1)
            unit_name = match.group(2).lower()

            # Check if unit is recognized
            if not (unit_name in unit["imperic_names"]):
                return "Couldnt convert unit: " + number + " " + unit_name

            # Convert the number to metric
            if unit_name in ("fahrenheit", "f"):
                number = round(
                    (float(number) - 32) * unit["conversion_factor"], 2
                )
            else:
                number = round(float(number) * unit["conversion_factor"], 2)

            # Convert unit to metric
            unit_index = unit["imperic_names"].index(unit_name)
            if unit_index >= 2:
                unit_name = unit["metric_names"][2]
            else:
                if number == 1:  # Singular
                    unit_name = unit["metric_names"][0]
                else:  # Plural
                    unit_name = unit["metric_names"][1]

            return f"{number:.2f} {unit_name}"

        sentence = pattern.sub(replace_match, sentence)
    return sentence


class OnMessageEvent(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if message.author == self.bot.user:
            return

        msg = replace_with_metric(message.content)
        if msg == message.content:
            return

        await message.channel.send("```" + msg + "```")


def setup(bot: commands.Bot):
    bot.add_cog(OnMessageEvent(bot))
