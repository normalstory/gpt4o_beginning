# .env file에서 환경변수(API key)가져와서 로드하기 
from dotenv import load_dotenv
load_dotenv() 


# 실습8 - Q&A: Audio Q&A
from openai import OpenAI 
from C05_Summary_Audio import transcription

client = OpenAI()
MODEL="gpt-4o"

QUESTION = "Question: Why do you emphasise the importance of demonstrating to really understand the capabilities of the Macintosh?"

qa_audio_response = client.chat.completions.create(
    model=MODEL,
    messages=[
    {"role": "system", "content":"""Use the transcription to answer the provided question. Respond in Markdown."""},
    {"role": "user", "content": f"The audio transcription is: {transcription.text}. \n\n {QUESTION}"},
    ],
    temperature=0,
)
print("\n\nAudio QA:\n" + qa_audio_response.choices[0].message.content)