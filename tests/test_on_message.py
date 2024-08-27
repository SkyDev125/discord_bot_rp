from tools.unit_conversion import replace_with_metric


class TestReplaceWithMetric:
    # Handles sentences with no units gracefully
    def test_handles_sentences_with_no_units(self):
        sentence = "This is a simple sentence with no units."
        expected = "This is a simple sentence with no units."
        result = replace_with_metric(sentence)
        assert result == expected

    # Converts feet and inches to meters correctly
    def test_converts_feet_and_inches_to_meters2(self):
        sentence = "The table is 5'5'' long."
        expected = "The table is 1.65 m long."
        result = replace_with_metric(sentence)
        assert result == expected

    # Converts "5 feet 10 inches" to meters correctly
    def test_converts_feet_and_inches_to_meters1(self):
        sentence = "5 feet 10 inches"
        expected = "1.78 m"
        result = replace_with_metric(sentence)
        assert result == expected

    # Converts "6ft 2in" to meters correctly
    def test_converts_feet_and_inches_to_meters_correctly(self):
        sentence = "6ft 2in"
        expected = "1.88 m"
        result = replace_with_metric(sentence)
        assert result == expected

    # Converts "0 feet 0 inches" to meters correctly
    def test_converts_zero_feet_zero_inches_to_meters(self):
        sentence = "0 feet 0 inches"
        expected = "0.00 m"
        result = replace_with_metric(sentence)
        assert result == expected

    # Converts negative feet and inches to meters correctly
    def test_converts_negative_feet_and_inches_to_meters(self):
        sentence = "The room is -6'3'' in height."
        expected = "The room is -1.91 m in height."
        result = replace_with_metric(sentence)
        assert result == expected

    # Converts "12 inches" to centimeters correctly
    def test_converts_inches_to_centimeters_correctly(self):
        sentence = "12 inches"
        expected = "30.48 centimeters"
        result = replace_with_metric(sentence)
        assert result == expected

    # Converts inches to centimeters correctly
    def test_converts_inches_to_centimeters(self):
        sentence = "The rope is 10 inches long."
        expected = "The rope is 25.40 centimeters long."
        result = replace_with_metric(sentence)
        assert result == expected

    # Converts "0 inches" to centimeters correctly
    def test_converts_zero_inches_to_centimeters(self):
        sentence = "0 inches"
        expected = "0.00 centimeters"
        result = replace_with_metric(sentence)
        assert result == expected

    # Converts negative inches to centimeters correctly
    def test_converts_negative_inches_to_centimeters_correctly(self):
        sentence = "The height is -12 inches."
        expected = "The height is -30.48 centimeters."
        result = replace_with_metric(sentence)
        assert result == expected

    # Converts large values of inches to centimeters correctly
    def test_large_inches_to_centimeters(self):
        sentence = "The pole is 100 inches tall."
        expected = "The pole is 254.00 centimeters tall."
        result = replace_with_metric(sentence)
        assert result == expected

    # Handles different casing for units (e.g., "Inch" vs "inch")
    def test_handles_different_casing_for_units(self):
        sentence = "The table is 5'5'' long and weighs 20 Pounds. The height is 12 Inches."
        expected = "The table is 1.65 m long and weighs 9.07 kilograms. The height is 30.48 centimeters."
        result = replace_with_metric(sentence)
        assert result == expected

    # Handles plural and singular forms of units
    def test_handles_plural_and_singular_units(self):
        sentence = "The table is 5'5'' long and weighs 20 pounds. The height is 12 inches."
        expected = "The table is 1.65 m long and weighs 9.07 kilograms. The height is 30.48 centimeters."
        result = replace_with_metric(sentence)
        assert result == expected

    # test 3 feet and 4 inches
    def test_3_feet_and_4_inches(self):
        sentence = "3'4''"
        expected = "1.02 m"
        result = replace_with_metric(sentence)
        assert result == expected

    # Converts miles to kilometers correctly
    def test_converts_miles_to_kilometers(self):
        sentence = "The marathon is 26 miles."
        expected = "The marathon is 41.84 kilometers."
        result = replace_with_metric(sentence)
        assert result == expected

    # Converts ounces to grams correctly
    def test_converts_ounces_to_grams(self):
        sentence = "The weight is 8 ounces."
        expected = "The weight is 226.80 grams."
        result = replace_with_metric(sentence)
        assert result == expected

    # Converts pounds to kilograms correctly
    def test_converts_pounds_to_kilograms(self):
        sentence = "The package weighs 10 pounds."
        expected = "The package weighs 4.54 kilograms."
        result = replace_with_metric(sentence)
        assert result == expected

    # Converts stones to kilograms correctly
    def test_converts_stones_to_kilograms(self):
        sentence = "The person weighs 5 stones."
        expected = "The person weighs 31.75 kilograms."
        result = replace_with_metric(sentence)
        assert result == expected

    # Converts Fahrenheit to Celsius correctly
    def test_converts_fahrenheit_to_celsius(self):
        sentence = "The temperature is 100 degrees Fahrenheit."
        expected = "The temperature is 37.78 degrees celsius."
        result = replace_with_metric(sentence)
        assert result == expected

    # Handles mixed units in a sentence
    def test_handles_mixed_units(self):
        sentence = (
            "The height is 5 feet 10 inches and the weight is 150 pounds."
        )
        expected = "The height is 1.78 m and the weight is 68.04 kilograms."
        result = replace_with_metric(sentence)
        assert result == expected

    # Handles invalid units gracefully
    def test_handles_invalid_units(self):
        sentence = "The length is 10 parsecs."
        expected = "The length is 10 parsecs."
        result = replace_with_metric(sentence)
        assert result == expected

    # Handles zero values correctly
    def test_handles_zero_values(self):
        sentence = "The length is 0 inches."
        expected = "The length is 0.00 centimeters."
        result = replace_with_metric(sentence)
        assert result == expected
