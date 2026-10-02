import os

from openai import OpenAI



api_key = os.environ.get("OPENAI_API_KEY")

if api_key is None:

    raise SystemExit("OPENAI_API_KEY is not set")

client = OpenAI(api_key=api_key)
