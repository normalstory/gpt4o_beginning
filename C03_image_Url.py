# 환경변수 로딩
from dotenv import load_dotenv
load_dotenv() 

# 이미지 처리 라이브러리와 OpenAI 라이브러리 불러오기
from openai import OpenAI 

client = OpenAI()
MODEL="gpt-4o"

# 클라이언트를 사용하여 대화를 생성
# system과 user의 역할이 있고, 각각 메시지를 담고 있음
# 시스템의 메시지를 제공하여 챗봇의 역할을 정의
# user의 메시지에 핵심 질문과 함께 삼각형의 이미지가 있는 URL을 제공
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

# 응답 출력
print(response.choices[0].message.content)
