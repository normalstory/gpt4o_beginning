# .env file에서 환경변수(API key)가져와서 로드하기 
from dotenv import load_dotenv
load_dotenv() 


# 실습1 - Basic Chat
from openai import OpenAI 
client = OpenAI()
MODEL="gpt-4o"

completion = client.chat.completions.create(
  model=MODEL,
  messages=[
    {"role": "system", "content": "You are a helpful assistant. Help me with my math homework!"},
    {"role": "user", "content": "Hello! Could you solve 2+2?"}
  ]
)

print("Assistant: " + completion.choices[0].message.content)
