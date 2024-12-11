// 환경 변수 로드
// `.env` 파일에서 환경 변수를 `process.env`로 로드하여 비밀번호와 같은 민감한 정보를 안전하게 저장할 수 있도록 합니다.
require('dotenv').config();

// Express 모듈 로드
// Express는 Node.js에서 간단하고 유연한 웹 서버를 구축할 수 있도록 도와주는 프레임워크입니다.
const express = require('express');
const app = express();

// 환경 변수에서 값 가져오기
// SECRET_MESSAGE: /secret 경로에서 반환할 비밀 메시지
// USERNAME: Basic Auth에서 사용할 사용자 이름
// PASSWORD: Basic Auth에서 사용할 비밀번호
const SECRET_MESSAGE = process.env.SECRET_MESSAGE || "Default Secret Message";
const USERNAME = process.env.USERNAME || "defaultUser";
const PASSWORD = process.env.PASSWORD || "defaultPass";

// Basic Auth 미들웨어
// 이 미들웨어는 요청에 포함된 Authorization 헤더를 확인하여
// 사용자 이름과 비밀번호를 검증합니다.
const basicAuth = (req, res, next) => {
    const authHeader = req.headers['authorization'];

    if (!authHeader) {
        // 인증 헤더가 없으면 인증을 요청합니다.
        res.setHeader('WWW-Authenticate', 'Basic realm="Restricted Area"');
        return res.status(401).send('Authentication required.');
    }

    // Authorization 헤더에서 Base64로 인코딩된 자격 증명을 추출합니다.
    const base64Credentials = authHeader.split(' ')[1];
    const credentials = Buffer.from(base64Credentials, 'base64').toString('ascii');
    const [username, password] = credentials.split(':');

    // 사용자 이름과 비밀번호를 검증합니다.
    if (username === USERNAME && password === PASSWORD) {
        next(); // 인증이 성공하면 다음 미들웨어로 이동합니다.
    } else {
        // 자격 증명이 잘못되었을 경우 인증을 다시 요청합니다.
        res.setHeader('WWW-Authenticate', 'Basic realm="Restricted Area"');
        res.status(401).send('Invalid credentials.');
    }
};

// / route - 간단한 Hello, world! 메시지 반환
// 기본 경로로 접근했을 때 "Hello, world!" 메시지를 반환합니다.
app.get('/', (req, res) => {
    res.send('Hello, world!');
});

// /secret route - Basic Auth로 보호
// 이 경로는 Basic Auth를 통해 보호되며, 인증이 성공하면 비밀 메시지를 반환합니다.
app.get('/secret', basicAuth, (req, res) => {
    res.send(`Secret message: ${SECRET_MESSAGE}`);
});

// 서버 실행
// 서버를 설정된 포트에서 실행합니다. 기본값은 3000번 포트입니다.
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});