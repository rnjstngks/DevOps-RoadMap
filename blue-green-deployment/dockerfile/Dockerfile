# 기본 이미지를 nginx:latest 로 사용
FROM nginx:latest

# 현재 디렉터리에 있는 index.html 파일을 컨테이너 내 /usr/share/nginx/index.html 위치에 복사
COPY index.html /usr/share/nginx/html/index.html

# 80 포트를 사용하겠다는 선언
EXPOSE 80

# nginx 서비스를 forground에서 실행
CMD ["nginx", "-g", "daemon off;"]