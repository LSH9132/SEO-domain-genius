#!/bin/bash

# 모델 디렉토리 생성
mkdir -p models

# 환경 파일이 없는 경우 생성
if [ ! -f .env ]; then
    cp .env.example .env
    echo "Please update .env file with your API keys and settings"
fi

# 실행 권한 부여
chmod +x scripts/run.sh 