from pathlib import Path


def validate_input_file(file_path: str):

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Input file '{file_path}' does not exist."
        )

    if not path.is_file():
        raise ValueError(
            f"'{file_path}' is not a valid file."
        )

    if path.stat().st_size == 0:
        raise ValueError(
            f"Input file '{file_path}' is empty."
        )

    return True


def validate_output_folder(folder: str):

    path = Path(folder)

    if not path.exists():
        path.mkdir(parents=True)

    return True


def validate_prompt(prompt: str):

    if not prompt.strip():
        raise ValueError(
            "Prompt is empty."
        )

    return True


def validate_json(data):

    if not isinstance(data, dict):
        raise TypeError(
            "Generated JSON must be a dictionary."
        )

    required_keys = [
        "summary",
        "key_points",
        "action_items",
    ]

    for key in required_keys:

        if key not in data:

            raise ValueError(
                f"Missing required key: {key}"
            )

    if not isinstance(data["summary"], str):
        raise TypeError(
            "summary must be a string."
        )

    if not isinstance(data["key_points"], list):
        raise TypeError(
            "key_points must be a list."
        )

    if not isinstance(data["action_items"], list):
        raise TypeError(
            "action_items must be a list."
        )

    return True