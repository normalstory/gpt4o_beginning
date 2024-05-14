# .env file에서 환경변수(API key)가져와서 로드하기 
from dotenv import load_dotenv
load_dotenv() 


# 실습7 - Q&A: Visual Q&A
from openai import OpenAI 
from C04_Summary_Video import base64Frames

client = OpenAI()
MODEL="gpt-4o"

QUESTION = "Question: Why do you emphasise the importance of demonstrating to really understand the capabilities of the Macintosh?"

qa_visual_response = client.chat.completions.create(
    model=MODEL,
    messages=[
    {"role": "system", "content": "Use the video to answer the provided question. Respond in Markdown."},
    {"role": "user", "content": [
        "These are the frames from the video.",
        *map(lambda x: {"type": "image_url", "image_url": {"url": f'data:image/jpg;base64,{x}', "detail": "low"}}, base64Frames),
        QUESTION
        ],
    }
    ],
    temperature=0,
)
print("\n\nVisual QA:\n" + qa_visual_response.choices[0].message.content)
