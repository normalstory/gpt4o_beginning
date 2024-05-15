# .env file에서 환경변수(API key)가져와서 로드하기 
from dotenv import load_dotenv
load_dotenv() 

# 필요한 라이브러리들 로드 
from openai import OpenAI 

client = OpenAI()
MODEL="gpt-4o"

audio_path = "resource/Macintosh_Team_Interview.mp3"

# 'whisper-1' 모델을 사용해서 음성 파일을 텍스트로 변환합니다.
transcription = client.audio.transcriptions.create(
    model="whisper-1",
    file=open(audio_path, "rb"),
)

# 변환된 텍스트를 기반으로 요약문을 생성합니다.
# 사용자 메시지와 시스템 메시지를 함께 제공하여, 시스템 메시지가 어떤 행동을 해야하는지 AI에 지시하고, 사용자 메시지를 기반으로 그 행동을 수행합니다.
# 이 경우, 시스템 메시지는 AI에게 텍스트를 요약하라고 지시하고, 사용자 메시지는 요약할 텍스트를 제공합니다.
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": """You are generating a transcript summary. Create a summary of the provided transcription. Respond in Markdown."""},
        {"role": "user", "content": [
            {"type": "text", "text": f"The audio transcription is: {transcription.text}"}
        ],
    }
    ],
    temperature=0,  
)

# AI가 생성한 요약문을 출력합니다.
# temperature 매개변수가 0으로 설정되어 있으므로, 생성된 출력은 결정론적입니다.
print(response.choices[0].message.content)
