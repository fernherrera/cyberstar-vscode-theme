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
        type:
        uiTheme: 
        ui: 
        levels: 
        syntax: 
    """
    # Meta
    name: str = "Theme"
    slug: str = "themes"
    type: str = "dark"
    uiTheme: str = "vs-dark"

    ui: Any = None
    levels: Any = None
    syntax: Any = None

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
