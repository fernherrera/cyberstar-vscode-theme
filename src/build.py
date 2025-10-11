import argparse
from pathlib import Path

from vscode_themes.theme import ThemeBuilder

def main(args: argparse.Namespace):
    try:
        builder = ThemeBuilder()
        builder.build(args.config, args.output)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        "--config",
        default=Path("config.json"),
        help="Configuration file to be used (config.json)",
        type=Path,
    )
    parser.add_argument(
        "-o",
        "--output",
        default=Path("../themes/"),
        help="The file to output the generated theme to (output.json)",
        type=Path,
    )

    args = parser.parse_args()
    main(args)
