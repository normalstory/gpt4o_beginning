# .env file에서 환경변수(API key)가져와서 로드하기 
from dotenv import load_dotenv
load_dotenv() 

# 필요한 라이브러리 로드, OpenAI API와 상호 작용을 위한 클라이언트 라이브러리
from openai import OpenAI  
# 이전에 사용했던 코드 재사용, transcription - 오디오를 텍스트로 변환하는 함수
from C05_Summary_Audio import transcription 

client = OpenAI()  # OpenAI API에 연결하기 위해 클라이언트를 초기화
MODEL="gpt-4o"  # 응답을 생성할 모델을 지정

# 답변받고자 하는 질문을 정의
QUESTION = "Question: Why do you emphasise the importance of demonstrating to really understand the capabilities of the Macintosh?"

# OpenAI 클라이언트 라이브러리(chat.completions.create() 메서드)를 사용하여 채팅 응답 생성
qa_audio_response = client.chat.completions.create(
    # 이 요청에 대한 모델과 시스템, 사용자 메시지 지정
    model=MODEL,
    messages=[
    {"role": "system", "content":"""Use the transcription to answer the provided question. Respond in Markdown."""},
    {"role": "user", "content": f"The audio transcription is: {transcription.text}. \n\n {QUESTION}"},
    ],
    temperature=0,
)

# 생성된 채팅 응답의 내용 출력
print("\n\nAudio QA:\n" + qa_audio_response.choices[0].message.content)