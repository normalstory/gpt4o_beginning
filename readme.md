# GPT-4o API 실습

### 01 - api key 및 깃헙 설정 
* .env 작성 
* .gitignore 작성 

### 02 - 가상환경 설정 및 실행 
* python -m venv gpt4o  
* source gpt4o/bin/activate

### 03 - 의존 패키지 설치 
* pip install -U openai opencv-python moviepy python-dotenv

### 04 - 예제 실행 
* python3 01_BasicChat.py
* python3 02_Image_Base64.py (로컬에 저장된 이미지)
* python3 03_image_Url.py (손으로 그린 그림을 사진찍어서 깃헙에 업로드한 이미지)
* python3 04_Summary_Video.py (로컬에 저장된 mp4)
* python3 05_Summary_Audio.py (로컬에 저장된 mp3)


reference
--------------------------------------------------------
- GPT-4o(@openai): https://platform.openai.com/docs/models/gpt-4o 
- Code(@Mervin Praison): https://mer.vin/2024/05/gpt-4o-api/
- Generate shorts(@ssemble) : https://www.ssemble.com/
- Video(@AndyHertzfeld): https://www.youtube.com/watch?v=oTtQ0l0ukvQ
