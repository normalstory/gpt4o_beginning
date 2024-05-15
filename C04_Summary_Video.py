# .env file에서 환경변수(API key)가져와서 로드하기 
from dotenv import load_dotenv
load_dotenv() 


# 필요한 라이브러리들 로드 
from openai import OpenAI 
import os
import cv2
from moviepy.editor import VideoFileClip
import base64

# OpenAI 클라이언트와 모델을 초기화 
client = OpenAI()
MODEL="gpt-4o"

# 비디오 경로를 설정
VIDEO_PATH = "resource/Macintosh_Team_Interview.mp4"

# 비디오를 처리하는 함수를 정의
# 비디오의 총 프레임 수를 계산하고, 
# 지정된 간격으로 프레임을 건너뛰며 이 프레임을 base64 문자열로 인코딩,
# 그리고 비디오의 오디오를 추출하여 별도의 파일로 저장.
def process_video(video_path, seconds_per_frame=2):
    base64Frames = [] # base64로 인코딩된 프레임을 저장할 List
    base_video_path, _ = os.path.splitext(video_path)

    video = cv2.VideoCapture(video_path)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video.get(cv2.CAP_PROP_FPS)
    frames_to_skip = int(fps * seconds_per_frame)
    curr_frame=0

    # 총 프레임 수를 확인하고, 정해진 간격으로 프레임을 건너뛰어 base64 문자열로 인코딩하여 저장
    while curr_frame < total_frames - 1:
        video.set(cv2.CAP_PROP_POS_FRAMES, curr_frame)
        success, frame = video.read()
        if not success:
            break
        _, buffer = cv2.imencode(".jpg", frame)
        base64Frames.append(base64.b64encode(buffer).decode("utf-8"))
        curr_frame += frames_to_skip
    video.release()

    # 비디오의 오디오를 추출하여 별도의 파일로 저장합니다.
    audio_path = f"{base_video_path}.mp3"
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path, bitrate="32k")
    clip.audio.close()
    clip.close()

    print(f"Extracted {len(base64Frames)} frames")
    print(f"Extracted audio to {audio_path}")
    return base64Frames, audio_path

# 위에서 정의한 함수를 사용하여 비디오 프로세스 처리
base64Frames, audio_path = process_video(VIDEO_PATH, seconds_per_frame=1)

# OpenAI API 클라이언트를 이용해서 채팅 시작
# 비디오 요약 생성 요청,반환 결과를 포함하는 response 객체를 반환 
response = client.chat.completions.create(
    # 응답을 생성하는데 사용될 llm모델을 지정
    model=MODEL, 
    # 모델의 동작을 설정하는 시스템 메시지(비디오 요약을 생성하라고 지시)와 사용자 메시지로 초깃값이 설정
    messages=[ 
    {"role": "system", "content": "You are generating a video summary. Please provide a summary of the video. Respond in Markdown."},
    {"role": "user", "content": [
        "These are the frames from the video.",
        *map(lambda x: {"type": "image_url", 
                        "image_url": {"url": f'data:image/jpg;base64,{x}', "detail": "low"}}, base64Frames)
        ],
    }
    ],
    # 봇의 응답의 무작위성을 0~2 값으로 제어, 값이 낮을수록 출력이 일관적, 값이 높을수록 무작위적이고 창조적
    temperature=0,
)

# 생성된 요약을 출력
print(response.choices[0].message.content)
