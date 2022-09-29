# Some ANSI escape sequences for colors and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u00b1[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def color_print(text: str, *effects: str) -> None:
    """Print "text" using the ANSI sequences to change color, etc

    Args:
        text: The text to print.
        effects: The effect we want. One of the constants defined at the start of this module.
    """
    effect_string = "".join(effects)
    output_string = f"{effect_string}{text}{RESET}"
    print(output_string)
    
color_print("Hello, Red", RED)
color_print("Hello, Red, in BOLD",BOLD, RED)
print("This should be in the default terminal color")
color_print("Hello, Blue", BLUE)
color_print("Hello, Yellow", YELLOW)
color_print("Hello, Bold", BOLD)
color_print("Hello, Underline", UNDERLINE)
color_print("Hello, Reverse", REVERSE)
color_print("Hello, Black", BLACK)
