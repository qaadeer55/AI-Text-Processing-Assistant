import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    MODEL_NAME = os.getenv("MODEL_NAME")
    BASE_URL = os.getenv("OLLAMA_BASE_URL")
    USE_LOCAL_MODEL = os.getenv("USE_LOCAL_MODEL") == "True"