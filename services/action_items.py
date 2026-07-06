from services.ai_client import ask_ai
from utils.prompt_loader import load_prompt


def extract_action_items(text: str):

    prompt = load_prompt("action_items_prompt.txt")

    prompt = prompt.replace("{text}", text)

    return ask_ai(prompt)