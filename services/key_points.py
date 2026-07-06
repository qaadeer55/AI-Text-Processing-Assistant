from services.ai_client import ask_ai
from utils.prompt_loader import load_prompt


def extract_key_points(text: str):

    prompt = load_prompt("key_points_prompt.txt")

    prompt = prompt.replace("{text}", text)

    return ask_ai(prompt)