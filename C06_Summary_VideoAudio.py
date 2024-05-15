# .env file에서 환경변수(API key)가져와서 로드하기 
from dotenv import load_dotenv
load_dotenv() 

# 필요한 라이브러리들 로드 
from openai import OpenAI 
from C04_Summary_Video import base64Frames
from C05_Summary_Audio import transcription

client = OpenAI()
MODEL="gpt-4o"

# client.chat.completions.create는 OpenAI API를 사용하여 AI 질의를 생성하고 결과를 반환합니다.
response = client.chat.completions.create(
    # 사용할 AI 모델 이름을 지정합니다.
    model=MODEL,
    messages=[
        # 시스템 메시지를 통해 AI에게 이 행동이 무엇인지를 설명하고 지시하게 됩니다.
        {"role": "system", "content":"""You are generating a video summary. Create a summary of the provided video and its transcript. Respond in Markdown"""},
        # 사용자 메시지는 AI에게 인풋(input)을 제공합니다.
        {"role": "user", "content": [
            # 다음 문장은 비디오 프레임에 대한 설명을 제공합니다.
            "These are the frames from the video.",
            # 이후에 사용자가 제공하는 각 프레임(image)는 'image_url' 타입의 메시지로 제공됩니다.
            # map 함수와 람다 표현식을 사용하여 각 base64Frames 항목을 이미지 URL로 변환합니다.
            *map(lambda x: {"type": "image_url", 
                            "image_url": {"url": f'data:image/jpg;base64,{x}', "detail": "low"}}, base64Frames),
            # 마지막으로, 비디오의 오디오 전사본이 'text' 타입의 메시지로 제공됩니다.
            {"type": "text", "text": f"The audio transcription is: {transcription.text}"}
        ],
    }],
    # temperature 매개변수는 생성된 출력의 다양성을 결정합니다. 낮은 값은 추론 결과가 좀 더 결정적(deterministic)이고 예측 가능하도록 만듭니다.
    temperature=0,
)
# AI에 의해 생성된 요약 (response의 첫 번째 선택 항목)을 출력합니다.
print("\n\nAudio + Visual Summary:\n" + response.choices[0].message.content)