# .env file에서 환경변수(API key)가져와서 로드하기 
from dotenv import load_dotenv
load_dotenv() 


# 실습9 - Q&A: Visual + Audio Q&A
from openai import OpenAI 
from C04_Summary_Video import base64Frames
from C05_Summary_Audio import transcription

client = OpenAI()
MODEL="gpt-4o"
QUESTION = "Question: Why do you emphasise the importance of demonstrating to really understand the capabilities of the Macintosh?"

qa_both_response = client.chat.completions.create(
    model=MODEL,
    messages=[
    {"role": "system", "content":"""Use the video and transcription to answer the provided question."""},
    {"role": "user", "content": [
        "These are the frames from the video.",
        *map(lambda x: {"type": "image_url", 
                        "image_url": {"url": f'data:image/jpg;base64,{x}', "detail": "low"}}, base64Frames),
                        {"type": "text", "text": f"The audio transcription is: {transcription.text}"},
        QUESTION
        ],
    }
    ],
    temperature=0,
)
print("\n\nBoth QA:\n" + qa_both_response.choices[0].message.content)