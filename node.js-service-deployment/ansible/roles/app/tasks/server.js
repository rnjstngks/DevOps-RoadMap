const http = require('http');            // HTTP 모듈 불러오기
const fs = require('fs');                // 파일 시스템 모듈 불러오기
const path = require('path');            // 경로 처리 모듈 불러오기

const port = 80;                       // 서버가 실행될 포트 번호

const server = http.createServer((req, res) => {  // HTTP 서버 생성
    const filePath = path.join(__dirname, 'index.html');  // index.html 경로
    fs.readFile(filePath, (err, data) => {                // 파일 읽기
        if (err) {                                          // 에러 발생 시
            res.writeHead(500, { 'Content-Type': 'text/plain' });  // 500 응답
            res.end('Internal Server Error');
        } else {                                            // 정상 파일 읽기
            res.writeHead(200, { 'Content-Type': 'text/html' });  // 200 응답
            res.end(data);                                    // index.html 반환
        }
    });
});

server.listen(port, () => {                             // 서버 실행
    console.log(`Server is running at http://localhost:${port}`);
});