# Node.js 기반 이미지 사용
FROM node:22

# 작업 디렉터리 생성
WORKDIR /usr/src/app

# app.js, .env 파일 복사
COPY  app.js /usr/src/app/app.js
COPY  .env /usr/src/app/.env

# 의존성 설치
RUN npm install express dotenv

# 애플리케이션 포트 노출
EXPOSE 3000

# 컨테이너 실행 시 명령어
CMD ["node", "app.js"]