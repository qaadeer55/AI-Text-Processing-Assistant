from openai import OpenAI

from config.config import Config

client = OpenAI(
    base_url=Config.BASE_URL,
    api_key="ollama",
)


def ask_ai(prompt: str):

    response = client.chat.completions.create(
        model=Config.MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response.choices[0].message.content