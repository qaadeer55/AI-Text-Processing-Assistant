from pathlib import Path

from utils.validator import validate_prompt


def load_prompt(prompt_name: str) -> str:
    """
    Load a prompt template from the prompts directory
    and validate that it is not empty.
    """

    path = Path("prompts") / prompt_name

    if not path.exists():
        raise FileNotFoundError(
            f"Prompt template '{prompt_name}' not found."
        )

    prompt = path.read_text(encoding="utf-8")

    validate_prompt(prompt)

    return prompt