from pathlib import Path

import typer

from ._service import promptfy

app = typer.Typer()


@app.command()
def main(paths: list[Path]):
    prompt = promptfy(paths)

    print(prompt, end="")


if __name__ == "__main__":
    app()
