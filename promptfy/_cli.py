from pathlib import Path
from typing import Annotated

import typer

from ._service import promptfy

app = typer.Typer()


@app.command()
def main(paths: Annotated[list[Path], typer.Argument(help="The paths to the files to include in the prompt.")]):
    """
    Generate a prompt from the files at the given paths.
    """
    prompt = promptfy(paths)

    print(prompt, end="")


if __name__ == "__main__":
    app()
