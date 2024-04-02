import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
  azure_endpoint=os.getenv("AZURE_ENDPOINT"),
  api_key=os.getenv("AZURE_KEY"),
  api_version="2023-05-15"
)

def gpt(a):
    print(a)
    response = client.chat.completions.create(
        model="firstdep",
        messages=[
            {"role": "system", "content": a},
        ]
    )
    assistant_response = response.choices[0].message.content
    print("Assistant:", assistant_response)
    # speak.speak(assistant_response)
    return assistant_response

