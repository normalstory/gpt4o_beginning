# .env 파일에서 환경변수(API key) 가져와서 로드하기
from dotenv import load_dotenv
load_dotenv()  

# 필요한 라이브러리 로드
from openai import OpenAI  # OpenAI API와 상호 작용을 위한 클라이언트 라이브러리
from C04_Summary_Video import base64Frames  # 이전 코드 재사용, 비디오를 텍스트로 변환하는 함수
from C05_Summary_Audio import transcription  # 이전 코드 재사용, 오디오를 텍스트로 변환하는 함수

client = OpenAI()   # OpenAI API에 연결하기 위해 클라이언트를 초기화
MODEL="gpt-4o"  # 응답을 생성할 모델을 지정
QUESTION = "Question: Why do you emphasise the importance of demonstrating to really understand the capabilities of the Macintosh?"

qa_both_response = client.chat.completions.create(
    model=MODEL,
    # C06_Summary_VideoAudio 예제와 같이 map()을 통해 Audio, Video 관련 내용을 함께 구성
    messages=[
        {
            "role": "system", 
            "content":"""Use the video and transcription to answer the provided question."""
        },
        {
            "role": "user", 
            "content": [
                "These are the frames from the video.",
                *map(
                        lambda x: {
                            "type": "image_url", 
                            "image_url": {"url": f'data:image/jpg;base64,{x}', "detail": "low"}
                        }, 
                        base64Frames
                    ),
                    {
                        "type": "text", 
                        "text": f"The audio transcription is: {transcription.text}"
                    },
                QUESTION
            ],
        }
    ],
    temperature=0,
)
print("\n\nBoth QA:\n" + qa_both_response.choices[0].message.content)