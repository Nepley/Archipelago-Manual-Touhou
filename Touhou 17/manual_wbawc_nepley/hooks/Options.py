# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, SpecialRange

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value

####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world. 
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#

class NumberLifeMid(Range):
    """Number of life the randomizer expect you to have before facing Kutaka and Yachie"""
    display_name = "Number of life expected in order to face Kutaka and Yachie"
    range_start = 0
    range_end = 8
    default = 3

class NumberBombsMid(Range):
    """Number of bombs the randomizer expect you to have before facing Kutaka and Yachie"""
    display_name = "Number of bombs expected in order to face Kutaka and Yachie"
    range_start = 0
    range_end = 8
    default = 2

class DifficultyMid(Choice):
    """The difficulty expected in order to face Kutaka and Yachie (Starting from Lunatic and got to Easy)"""
    display_name = "Difficulty in order to face Kutaka and Yachie"
    option_lunatic = 0
    option_hard = 1
    option_normal = 2
    option_easy = 3
    default = 1

class NumberLifeEnd(Range):
    """Number of life the randomizer expect you to have before facing Mayumi and Keiki"""
    display_name = "Number of life expected in order to face Mayumi and Keiki"
    range_start = 0
    range_end = 8
    default = 3

class NumberBombsEnd(Range):
    """Number of bombs the randomizer expect you to have before facing Mayumi and Keiki"""
    display_name = "Number of bombs expected in order to face Mayumi and Keiki"
    range_start = 0
    range_end = 8
    default = 2

class DifficultyEnd(Choice):
    """The difficulty expected in order to face Mayumi and Keiki (Starting from Lunatic and got to Easy)"""
    display_name = "Difficulty in order to face Mayumi and Keiki"
    option_lunatic = 0
    option_hard = 1
    option_normal = 2
    option_easy = 3
    default = 1

class EndingRequired(Range):
    """How many ending is required to finish the game"""
    display_name = "How many ending is required to finish the game"
    range_start = 1
    range_end = 3
    default = 3

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["number_life_mid"] = NumberLifeMid
    options["number_bomb_mid"] = NumberBombsMid
    options["difficulty_mid"] = DifficultyMid
    options["number_life_end"] = NumberLifeEnd
    options["number_bomb_end"] = NumberBombsEnd
    options["difficulty_end"] = DifficultyEnd
    options["ending_required"] = EndingRequired
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    return options