import re

# Define the regular expression pattern
my_pattern = r"It's such a lovely day today\.|Some weather we're having today, huh\?|Maybe today's just not my day\."
my_regex = re.compile(my_pattern)

# Strings to be used in tests
FINDALL_STRING = """
It's such a lovely day today.
Some weather we're having today, huh?
Maybe today's just not my day.
"""

# Test class for regular expression
class TestRegEx:
    def test_matches_its_such_a_lovely_day(self):
        '''matches the string "It's such a lovely day today."'''
        assert my_regex.fullmatch("It's such a lovely day today.") is not None

    def test_matches_some_weather_were_having(self):
        '''matches the string "Some weather we're having today, huh?"'''
        assert my_regex.fullmatch("Some weather we're having today, huh?") is not None

    def test_matches_maybe_todays_not_my_day(self):
        '''matches the string "Maybe today's just not my day."'''
        assert my_regex.fullmatch("Maybe today's just not my day.") is not None

    def test_finds_all_matches(self):
        '''can be used to find these three strings and ONLY these three strings.'''
        assert my_regex.findall(FINDALL_STRING) == [
            "It's such a lovely day today.",
            "Some weather we're having today, huh?",
            "Maybe today's just not my day.",
        ]

