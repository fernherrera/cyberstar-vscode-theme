import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from .ui import UI

@dataclass
class Theme:
    """Theme configuration for theme builder

      Note: All colors are to be privided as strings instandard hex-format (i.e. #FFFFFF)

    Attributes:
        name: Name of the generated theme
        slug: 
        foreground: Primary text color
        foreground_darker: Darker primary text color
        background: Primary editor background
        background_darker: Secondary panel background
        accent_primary: Primary UI theme color
        accent_hover: Primary UI theme highlight color
        accent_secondary: Secondary UI theme color
        accent_tertiary: Tertiary UI theme color
        light_one: Lighter base color
        light_two: Darker base color
        primary_one: Primary theme token color
        primary_two: Primary theme token color shade
        secondary_one: Secondary theme token color
        secondary_two: Secondary theme token color shade
        tertiary_one: Tertiary theme token color
        tertiary_two: Tertiary theme token color shade
        issue: Issue/Error/Removed color
        warning: Warning/Changed color
        okay: Okay/Added color
    """
    # Meta
    name: str = "Theme"
    slug: str = "themes"
    uiTheme: str = "vs-dark"

    ui: Any = None
    levels: Any = None
    syntax: Any = None

    # Base Colors
    foreground: str = "#F3F3F7"
    foreground_darker: str = "#D2D2E2"
    background: str = "#2F2F37"
    background_darker: str = "#26262C"
    accent_primary: str = "#A967CE"
    accent_hover: str = "#B490E0"
    accent_secondary: str = "#7A6ADD"
    accent_tertiary: str = "#D66FAD"

    # Token Colors
    light_one: str = "#ADB2C2"
    light_two: str = "#9090A0"
    primary_one: str = "#CF81D9"
    primary_two: str = "#B490E0"
    secondary_one: str = "#BBBBFF"
    secondary_two: str = "#A0D0F0"
    tertiary_one: str = "#B0E0FF"
    tertiary_two: str = "#B0D0FF"

    # Important Colors
    issue: str = "#FF7878"
    warning: str = "#FFA878"
    okay: str = "#78FFA8"

    def __init__(self, theme):
        for key, value in theme.items():
            setattr(self, key, value)


@dataclass
class ThemeBuilder:
    """Base Theme - the default Lucky Theme (My personal color preference)

    Note: All colors are to be privided as strings instandard hex-format (i.e. #FFFFFF)

    Attributes:
        config: The parsed theme builder configuration 
    """

    __config: Any = None

    def __load_config(self, json_file: Path) -> Any:
        """Load config from a provided JSON file

        Parameters:
            json_file: The chosen config JSON file
        """
        with open(json_file, "r") as file:
            values = json.load(file)

        # for key, value in values.items():
        #     setattr(self, key, value)

        return values

    def build(self, config: Path, output: Path=None) -> None:
        """Build theme from chosen `config` into `output`

        Warning: This will OVERWRITE any currently existing `output`!

        Parameters:
            config: Chosen JSON config file
            name: Name of the theme
            output: Output file to write resulting theme to
        """

        self.__config = self.__load_config(config)

        for item in self.__config:
            self.__make_theme(Theme(item), output)

    def __make_theme(self, theme: Theme, output_path: Path) -> None:
        print("Building theme: " + theme.name)

        theme_template = {
            "$schema": "vscode://schemas/color-theme",
            "name": theme.name,
            "colors": UI(theme).build()
        }

        file_name = theme.slug + '-color-theme.json'
        output = output_path.joinpath(file_name)
        print("output: " + output.__str__())

        with open(output, "w") as file:
            json.dump(theme_template, file, indent=4)
