# dotenv 패키지에서 load_dotenv 함수 로드 
from dotenv import load_dotenv
# .env라는 파일로부터 환경변수를 불러오는 함수 실행
load_dotenv() 

# OpenAI 패키지 추가 
from openai import OpenAI
# OpenAI 클라이언트 생성
client = OpenAI()
# 사용할 채팅 모델 지정
MODEL="gpt-4o"

# OpenAI API를 사용하여 반환된 채팅 응답을 저장하기 위한 'completion' 객체를 생성
completion = client.chat.completions.create(
  model=MODEL,  # 사용할 모델
  messages=[    # 시간순으로 메시지 객체를 배열로 전달
    {"role": "system", "content": "You are a helpful assistant. Help me with my math homework!"},
    {"role": "user", "content": "Hello! Could you solve 2+2?"}
  ]
)

# 채팅봇의 응답을'choices' 속성에서 첫 번째 선택사항을 가져와 출력
print("Assistant: " + completion.choices[0].message.content)