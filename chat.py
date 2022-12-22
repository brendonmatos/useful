import os
import openai
from dotenv import load_dotenv
import yaml
import sys

load_dotenv()

input = sys.argv[1]
openai.api_key = os.getenv("OPEN_AI_TOKEN")

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"""

Human:

{input}

AI:
  """,
    temperature=0.9,
    max_tokens=500,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"],
)

result = response.choices[0].text
print(result)
