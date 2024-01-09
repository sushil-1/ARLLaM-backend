from openai import OpenAI
from .config import config

print(f"{config.get('OPENAI_API_KEY')=}")

openai_client = OpenAI(api_key=config.get('OPENAI_API_KEY'))