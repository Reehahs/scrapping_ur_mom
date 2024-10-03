#Good that was a test
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


client = OpenAI(
  organization='org-Nu55tA122JzGHG1tYY8zY2es',
  project='proj_DStd6BYBAgVqBAWQMvILVSEg',
  api_key=os.environ.get("OPENAI_PROJECT_API_KEY"),
)

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user", 
            "content": "Tell me the stock of the week to buy, just say the ticker name not the reason"
        }
               ],
    stream = True
)

for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")


