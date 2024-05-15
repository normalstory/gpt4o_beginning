# .env file에서 환경변수(API key)가져와서 로드하기 
from dotenv import load_dotenv
load_dotenv() 

# 필요한 라이브러리 로드, OpenAI API와 상호 작용을 위한 클라이언트 라이브러리
from openai import OpenAI 
# 이전에 사용했던 코드 재사용, *base64Frames 리스트는 비디오 프레임을 Base64 문자열로 변환한 값 
from C04_Summary_Video import base64Frames

client = OpenAI()  # OpenAI API에 연결하기 위해 클라이언트를 초기화합니다.
MODEL="gpt-4o"  # 응답을 생성할 모델을 지정합니다 (실제 모델 이름이나 ID로 교체하세요).

# 답변받고자 하는 질문을 정의
QUESTION = "Question: Why do you emphasise the importance of demonstrating to really understand the capabilities of the Macintosh?"

# OpenAI 클라이언트 라이브러리(chat.completions.create() 메서드)를 사용하여 채팅 응답 생성
qa_visual_response = client.chat.completions.create(
    # 이 요청에 대한 모델과 시스템, 사용자 메시지 지정
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
    # 사실적인 응답으로 설정
    temperature=0,
)

# 생성된 채팅 응답의 내용(message.content 속성)을 마크다운 텍스트(system content)로 출력
print("\n\nVideo QA:\n" + qa_visual_response.choices[0].message.content)

