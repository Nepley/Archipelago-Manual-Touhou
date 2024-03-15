from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, SpecialRange

from .hooks.Options import before_options_defined, after_options_defined
from .Data import category_table


manual_options = before_options_defined({})

for category in category_table:
    for option_name in category_table[category].get("yaml_option", []):
        if option_name not in manual_options:
            manual_options[option_name] = type(option_name, (Toggle,), {"default": True})

manual_options = after_options_defined(manual_options)
