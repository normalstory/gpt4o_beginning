# .env file에서 환경변수(API key)가져와서 로드하기 
from dotenv import load_dotenv
load_dotenv() 


# 실습3 - Image Processing: URL
from openai import OpenAI 

client = OpenAI()
MODEL="gpt-4o"

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant that responds in Markdown. Help me with my math homework!"},
        {"role": "user", "content": [
            {"type": "text", "text": "What's the area of the triangle?"},
            {"type": "image_url", "image_url": {"url": "https://github.com/normalstory/gpt4o_beginning/blob/main/resource/triangle_note.png?raw=true"}
            }
        ]}
    ],
    temperature=0.0,
)

print(response.choices[0].message.content)
