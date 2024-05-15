# 환경변수 로딩
from dotenv import load_dotenv
load_dotenv() 

# 이미지 처리 라이브러리와 OpenAI 라이브러리 불러오기
from openai import OpenAI 
import base64

client = OpenAI()   # OpenAI 클라이언트 초기화
MODEL="gpt-4o"  # 모델 지정
IMAGE_PATH = "resource/triangle.png"  # 이미지 경로 지정

# 함수 정의: 이미지 파일을 base64로 인코딩하는 함수
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# 이미지 인코딩
base64_image = encode_image(IMAGE_PATH)

# 대화형 요청(챗창과 유사) 생성.
# system과 user의 역할이 있고, 각각 메시지를 담고 있음.
# user의 메시지 중 삼각형 이미지가 첨부됨.
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant that responds in Markdown. Help me with my math homework!"},
        {"role": "user", "content": [
            {"type": "text", "text": "What's the area of the triangle?"},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}
            }
        ]}
    ],
    temperature=0.0,
)

# 응답 출력
print(response.choices[0].message.content)