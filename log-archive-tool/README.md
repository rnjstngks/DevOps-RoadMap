# Log 압축 Tool 생성

Ubuntu 20.04에서 Python으로 Log가 있는 디렉터리를 날짜 별로 압축 시킬 수 있는 코드 입니다.

# 사용법

1. log-archive 파일을 bin 폴더로 복사
```sh
cp log-archive /usr/local/bin/
```

2. 실행 권한 추가
```sh
chmod +x log-archive
```

3. 기본 사용법
```sh
./log-archive <원하는 Log 디렉터리>
```