# 파일 무결성 검사기

파일이 이전과 달라졌는 지 확인 할 수 있도록 해줍니다.

사용법

1. 원하는 파일 or 디렉터리를 지정하여 해시 값 저장
```sh
python3 integrity-check.py init test.txt
```

2. 앞서 저장한 해시 값과 현재의 해시 값을 비교하여 파일 or 디렉터리에 변경 사항이 있는 지 확인
```sh
python3 integrity-check.py check test.txt
```

3. 원하는 파일 or 디렉터리를 지정하여 해시 값을 다시 저장
```sh
python3 integrity-check.py update test.txt
```