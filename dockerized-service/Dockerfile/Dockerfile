# Node.js 기반 이미지 사용
FROM node:22

# 작업 디렉터리 생성
WORKDIR /usr/src/app

# 의존성 복사
COPY package*.json ./

# 의존성 설치
RUN npm install

# 소스 코드 복사
COPY . .

# 컨테이너 실행 시 명령어
EXPOSE 3000
CMD ["node", "app.js"]