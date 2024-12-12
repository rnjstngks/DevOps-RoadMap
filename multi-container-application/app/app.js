// Express와 mongoose 모듈을 가져옵니다.
const express = require('express'); // 웹 서버를 만들기 위한 프레임워크
const mongoose = require('mongoose'); // MongoDB와 연결하기 위한 ODM(Object Data Modeling) 라이브러리
const bodyParser = require('body-parser'); // 요청 본문을 파싱하기 위한 미들웨어

// Express 애플리케이션을 초기화합니다.
const app = express(); 

// JSON 형식의 요청 데이터를 파싱하기 위해 body-parser를 사용합니다.
app.use(bodyParser.json()); 

// MongoDB 데이터베이스에 연결합니다.
// mongo는 docker-compose에서 정의된 MongoDB 서비스 이름이고, todo는 데이터베이스 이름입니다.
mongoose.connect('mongodb://mongo:27017/todo', {
    useNewUrlParser: true, // 새 URL 파서 사용
    useUnifiedTopology: true // 최신 MongoDB 드라이버의 통합 토폴로지 사용
});

// MongoDB 스키마 정의
// title: To-Do 항목의 제목, completed: 작업 완료 여부
const TodoSchema = new mongoose.Schema({
    title: String, // To-Do 항목의 제목
    completed: Boolean // 완료 여부 (true 또는 false)
});

// 정의한 스키마를 기반으로 MongoDB 모델을 생성합니다.
const Todo = mongoose.model('Todo', TodoSchema);

// HTTP GET 요청을 처리하여 모든 To-Do 항목을 반환합니다.
app.get('/todos', async (req, res) => {
    const todos = await Todo.find(); // MongoDB에서 모든 To-Do 항목 검색
    res.json(todos); // 검색 결과를 JSON 형식으로 반환
});

// HTTP POST 요청을 처리하여 새로운 To-Do 항목을 생성합니다.
app.post('/todos', async (req, res) => {
    // 요청 본문에서 title을 가져와 새 To-Do 항목을 생성합니다.
    const todo = new Todo({
        title: req.body.title,
        completed: false // 기본값으로 완료되지 않은 상태로 설정
    });
    await todo.save(); // 데이터베이스에 저장
    res.json(todo); // 생성된 항목을 클라이언트에 반환
});

// HTTP PUT 요청을 처리하여 특정 ID의 To-Do 항목을 수정합니다.
app.put('/todos/:id', async (req, res) => {
    // 요청된 ID에 해당하는 To-Do 항목을 요청 본문 데이터로 업데이트합니다.
    const todo = await Todo.findByIdAndUpdate(req.params.id, req.body, { new: true });
    res.json(todo); // 업데이트된 항목을 반환
});

// HTTP DELETE 요청을 처리하여 특정 ID의 To-Do 항목을 삭제합니다.
app.delete('/todos/:id', async (req, res) => {
    // 요청된 ID에 해당하는 To-Do 항목을 데이터베이스에서 삭제합니다.
    await Todo.findByIdAndDelete(req.params.id);
    res.json({ message: 'Todo deleted' }); // 삭제 완료 메시지를 반환
});

// 서버를 4000번 포트에서 실행합니다.
app.listen(4000, () => console.log('API running on http://localhost:4000'));
