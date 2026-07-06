import json
import re

from services.ai_client import ask_ai
from utils.prompt_loader import load_prompt
from utils.logger import logger


def extract_json(response: str):

    # Remove markdown fences
    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    # Find first JSON object
    match = re.search(r"\{.*\}", response, re.DOTALL)

    if not match:
        return None

    return match.group()


def generate_json(text: str):

    prompt = load_prompt("json_prompt.txt")

    prompt = prompt.replace("{text}", text)

    # Try up to 3 times
    for attempt in range(3):

        response = ask_ai(prompt)
        logger.debug(f"Raw AI Response:\n{response}")

        json_string = extract_json(response)

        if json_string is None:
            continue

        try:
            return json.loads(json_string)

        except json.JSONDecodeError:
            continue

    raise RuntimeError(
    "Unable to generate valid JSON after 3 attempts."
    )