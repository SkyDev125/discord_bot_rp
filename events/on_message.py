import re
import nextcord
from nextcord.ext import commands

# Define a list of dictionaries for conversion factors and regex patterns
units = [
    {
        "imperic_names": ("inch", "inches", "in", '"', "''", "´´", "``"),
        "metric_names": ("centimeter", "centimeters", "cm"),
        "conversion_factor": 2.54,
        "regex": r"(\d+)\s*(inches|inch|in|''|\"|``|´´)",
    },
    {
        "imperic_names": ("foot", "feet", "ft", "'"),
        "metric_names": ("meter", "meters", "m"),
        "conversion_factor": 0.3048,
        "regex": r"(\d+)\s*(feet|foot|ft|')(?!')",
    },
    {
        "imperic_names": ("yard", "yards", "yd"),
        "metric_names": ("meter", "meters", "m"),
        "conversion_factor": 91.44,
        "regex": r"(\d+)\s*(yards|yard|yd)",
    },
    {
        "imperic_names": ("mile", "miles", "mi"),
        "metric_names": ("kilometer", "kilometers", "km"),
        "conversion_factor": 1.60934,
        "regex": r"(\d+)\s*(miles|mile|mi)",
    },
    {
        "imperic_names": ("ounce", "ounces", "oz"),
        "metric_names": ("gram", "grams", "g"),
        "conversion_factor": 28.3495,
        "regex": r"(\d+)\s*(ounces|ounce|oz)",
    },
    {
        "imperic_names": ("pound", "pounds", "lb"),
        "metric_names": ("kilogram", "kilograms", "kg"),
        "conversion_factor": 0.453592,
        "regex": r"(\d+)\s*(pounds|pound|lb)",
    },
    {
        "imperic_names": ("stone", "stones", "st"),
        "metric_names": ("kilogram", "kilograms", "kg"),
        "conversion_factor": 6.35029,
        "regex": r"(\d+)\s*(stones|stone|st)",
    },
    {
        "imperic_names": ("fahrenheit", "f"),
        "metric_names": ("celsius", "celsius", "°C"),
        "conversion_factor": 5 / 9,
        "regex": r"(\d+)\s*(?:degrees|degree|°)\s*(fahrenheit|f)",
    },
]

# Define regex patterns to capture combined units
combined_patterns = {
    "feet_inches": re.compile(
        r"(\d+)\s*(feet|foot|ft|')\s*(?:and\s*)?(\d+)\s*(inches|inch|in|''|\"|``|´´)",
        re.IGNORECASE,
    ),
    "stones_ounces": re.compile(
        r"(\d+)\s*(stones|stone|st)\s*(?:and\s*)?(\d+)\s*(ounces|ounce|oz)",
        re.IGNORECASE,
    ),
    "miles_yards": re.compile(
        r"(\d+)\s*(miles|mile|mi)\s*(?:and\s*)?(\d+)\s*(yards|yard|yd)",
        re.IGNORECASE,
    ),
}


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
    sentence = combined_patterns["feet_inches"].sub(
        lambda match: convert_combined_units(match, 0.3048, 2.54, 100, "m"),
        sentence,
    )
    sentence = combined_patterns["stones_ounces"].sub(
        lambda match: convert_combined_units(
            match, 6.35029, 28.3495, 1000, "kg"
        ),
        sentence,
    )
    sentence = combined_patterns["miles_yards"].sub(
        lambda match: convert_combined_units(
            match, 1.60934, 0.9144, 1000, "km"
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


# Example usage
sentence = (
    "The table is 5'5'' long and weighs 20 pounds. The height is 12 inches."
)
converted_sentence = replace_with_metric(sentence)
print(converted_sentence)


class OnMessageEvent(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if message.author == self.bot.user:
            return

        await message.channel.send(message.content)


def setup(bot: commands.Bot):
    bot.add_cog(OnMessageEvent(bot))
