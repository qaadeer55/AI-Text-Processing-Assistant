from services.ai_client import ask_ai
from utils.prompt_loader import load_prompt


def generate_summary(text: str):

    prompt = load_prompt("summary_prompt.txt")

    prompt = prompt.replace("{text}", text)

    return ask_ai(prompt)