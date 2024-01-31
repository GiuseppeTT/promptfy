import sys
from pathlib import Path


def promptfy(paths: list[Path]):
    """
    Generate a prompt from the files at the given paths.

    Args:
        paths: A list of paths to the files to include in the prompt.
    """

    file_prompts = []
    for path in paths:
        try:
            file_prompts.append(_promptfy_file(path))
        except FileNotFoundError:
            print(f"Skipping path {path} because it does not exist", file=sys.stderr)
        except IsADirectoryError:
            print(f"Skipping path {path} because it is a directory", file=sys.stderr)
        except UnicodeDecodeError:
            print(f"Skipping path {path} because it is not utf-8 encoded", file=sys.stderr)
        except Exception:
            print(f"Found an error at path {path}", file=sys.stderr)
            raise

    if len(file_prompts) == 0:
        print(f"Skipping prompt because no files were found", file=sys.stderr)
        return ""

    prompt_header = _promptfy_header()
    prompt_content = "\n".join(file_prompts)
    prompt = prompt_header + prompt_content

    return prompt


def _promptfy_header() -> str:
    prompt_header = ""
    prompt_header += "# Files\n"
    prompt_header += "\n"

    return prompt_header


def _promptfy_file(path: Path) -> str:
    extension = path.suffix.lstrip(".")
    content = path.read_text()

    prompt = ""
    prompt += f"## {path}\n"
    prompt += "\n"
    prompt += f"```{extension}\n"
    prompt += f"{content}\n"
    prompt += "```\n"
    prompt += "\n"

    return prompt
