import events.on_message


class TestReplaceWithMetric:
    # Handles sentences with no units gracefully
    def test_handles_sentences_with_no_units(self):
        sentence = "This is a simple sentence with no units."
        expected = "This is a simple sentence with no units."
        result = events.on_message.replace_with_metric(sentence)
        assert result == expected

    # Converts feet and inches to meters correctly
    def test_converts_feet_and_inches_to_meters2(self):
        sentence = "The table is 5'5'' long."
        expected = "The table is 1.65 m long."
        result = events.on_message.replace_with_metric(sentence)
        assert result == expected

    # Converts "5 feet 10 inches" to meters correctly
    def test_converts_feet_and_inches_to_meters1(self):
        sentence = "5 feet 10 inches"
        expected = "1.78 m"
        result = events.on_message.replace_with_metric(sentence)
        assert result == expected

    # Converts "6ft 2in" to meters correctly
    def test_converts_feet_and_inches_to_meters_correctly(self):
        sentence = "6ft 2in"
        expected = "1.88 m"
        result = events.on_message.replace_with_metric(sentence)
        assert result == expected

    # Converts "0 feet 0 inches" to meters correctly
    def test_converts_zero_feet_zero_inches_to_meters(self):
        sentence = "0 feet 0 inches"
        expected = "0.00 m"
        result = events.on_message.replace_with_metric(sentence)
        assert result == expected

    # Converts negative feet and inches to meters correctly
    def test_converts_negative_feet_and_inches_to_meters(self):
        sentence = "The room is -6'3'' in height."
        expected = "The room is -1.91 m in height."
        result = events.on_message.replace_with_metric(sentence)
        assert result == expected

    # Converts "12 inches" to centimeters correctly
    def test_converts_inches_to_centimeters_correctly(self):
        sentence = "12 inches"
        expected = "30.48 centimeters"
        result = events.on_message.replace_with_metric(sentence)
        assert result == expected

    # Converts inches to centimeters correctly
    def test_converts_inches_to_centimeters(self):
        sentence = "The rope is 10 inches long."
        expected = "The rope is 25.40 centimeters long."
        result = events.on_message.replace_with_metric(sentence)
        assert result == expected

    # Converts "0 inches" to centimeters correctly
    def test_converts_zero_inches_to_centimeters(self):
        sentence = "0 inches"
        expected = "0.00 centimeters"
        result = events.on_message.replace_with_metric(sentence)
        assert result == expected

    # Converts negative inches to centimeters correctly
    def test_converts_negative_inches_to_centimeters_correctly(self):
        sentence = "The height is -12 inches."
        expected = "The height is -30.48 centimeters."
        result = events.on_message.replace_with_metric(sentence)
        assert result == expected

    # Converts large values of inches to centimeters correctly
    def test_large_inches_to_centimeters(self):
        sentence = "The pole is 100 inches tall."
        expected = "The pole is 254.00 centimeters tall."
        result = events.on_message.replace_with_metric(sentence)
        assert result == expected

    # Handles different casing for units (e.g., "Inch" vs "inch")
    def test_handles_different_casing_for_units(self):
        sentence = "The table is 5'5'' long and weighs 20 Pounds. The height is 12 Inches."
        expected = "The table is 1.65 m long and weighs 9.07 kilograms. The height is 30.48 centimeters."
        result = events.on_message.replace_with_metric(sentence)
        assert result == expected

    # Handles plural and singular forms of units
    def test_handles_plural_and_singular_units(self):
        sentence = "The table is 5'5'' long and weighs 20 pounds. The height is 12 inches."
        expected = "The table is 1.65 m long and weighs 9.07 kilograms. The height is 30.48 centimeters."
        result = events.on_message.replace_with_metric(sentence)
        assert result == expected

    # test 3 feet and 4 inches
    def test_3_feet_and_4_inches(self):
        sentence = "3'4''"
        expected = "1.02 m"
        result = events.on_message.replace_with_metric(sentence)
        assert result == expected


