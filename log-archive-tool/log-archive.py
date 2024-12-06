#!/usr/bin/env python3

# 파일과 디렉터리를 다루기 위한 모듈
import os   
# 파일 압축 및 해제를 다루는 모듈
import tarfile
# 현재 날짜와 시간을 가져오기 위한 모듈
from datetime import datetime
# 명령줄 인자를 처리하기 위한 모듈. CLI 도구로 만들기 위해 필요
import argparse

# 로그가 있는 디렉터리를 압축하기 위한 함수
def archive_logs(log_dir):
    # 현재 날짜와 시간 가져오기
    # timestamp 변수 정의
    # datetime.now() = 현재 시간
    # .strftime("%Y%m%d_%H%M%S") = "년도월일_시간분초" 형식으로 시간 지정 ex) 20241204_110223 = 2024년 12월 04일 11시 02분 23초
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # archive_name 변수 정의
    # f"logs_archive_{timestamp}.tar.gz" = 압축 시킬 파일의 이름의 형식 정의 ex) logs_archive_20241204_110223.tar.gz
    archive_name = f"logs_archive_{timestamp}.tar.gz"
    # os.path.join = 압축 시킬 로그 디렉터리 안에 archived_logs 라는 디렉터리를 하나 생성 합니다.
    # log_dir은 압축 시킬 디렉터리의 이름 입니다. ex) log-archive /var/log/ 명령어를 입력하면 /var/log가 log_dir이 됩니다.
    archive_dir = os.path.join(log_dir, "archive_logs")

    # 압축할 디렉터리 생성
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # tar.gz 파일 생성
    # archive_dir 디렉터리안에 위에서 정의한 archive_name 이름으로 tar.gz 파일을 생성
    archive_path = os.path.join(archive_dir, archive_name)
    with tarfile.open(archive_path, "w:gz") as tar:
        tar.add(log_dir, arcname=os.path.basename(log_dir))

    # 작업 기록 로그 파일
    # 압축시킬 로그 디렉터리안에 archive.log 라는 작업 기록 로그 파일을 생성하여 작업 내역을 적어두도록 설정
    log_file = os.path.join(log_dir, "archive.log")
    with open(log_file, "a") as log:
        log.write(f"[{timestamp}] Archived to {archive_path}\n")

    print(f"Logs archived to: {archive_path}")

# 명령줄 인자 처리
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Log Archive Tool")
    parser.add_argument("log_directory", help="Directory containing log files")
    args = parser.parse_args()

    if os.path.isdir(args.log_directory):
        archive_logs(args.log_directory)
    else:
        print(f"Error: {args.log_directory} is not a valid directory.")