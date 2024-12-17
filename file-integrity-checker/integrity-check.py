import hashlib  # 해시 값을 계산하기 위해 hashlib 모듈 사용
import os       # 파일 및 경로 확인을 위한 os 모듈 사용
import sys      # 명령어 인자 처리용 sys 모듈 사용
import json     # 해시 값을 저장하고 불러오기 위해 JSON 사용

# 해시 값을 저장할 파일 경로 설정
HASH_STORAGE = "file_hashes.json"

# 파일 해시 값을 계산하는 함수
def calculate_hash(file_path):
    """
    파일의 SHA-256 해시 값을 계산합니다.
    
    :param file_path: 해시 값을 계산할 파일 경로
    :return: 파일의 SHA-256 해시 값
    """
    sha256 = hashlib.sha256()  # SHA-256 해싱 객체 생성
    try:
        with open(file_path, "rb") as f:  # 파일을 바이너리 읽기 모드로 엽니다.
            while chunk := f.read(8192):  # 파일을 8KB씩 읽어들여 해싱
                sha256.update(chunk)  # 읽은 데이터를 해싱 객체에 업데이트
    except FileNotFoundError:
        print(f"Error: {file_path} 파일이 존재하지 않습니다.")
        sys.exit(1)
    
    return sha256.hexdigest()  # 최종 해시 값을 반환

# 기존 해시 값을 불러오거나 새로 초기화하는 함수
def load_hashes():
    """
    기존에 저장된 해시 값을 불러옵니다. 파일이 없으면 빈 딕셔너리를 반환합니다.
    """
    if os.path.exists(HASH_STORAGE):  # 해시 저장 파일이 존재하는지 확인
        with open(HASH_STORAGE, "r") as f:
            return json.load(f)  # JSON 파일을 불러와 딕셔너리로 반환
    return {}  # 저장 파일이 없으면 빈 딕셔너리 반환

# 해시 값을 저장하는 함수
def save_hashes(hashes):
    """
    주어진 해시 값을 JSON 파일에 저장합니다.
    
    :param hashes: 해시 값을 담은 딕셔너리
    """
    with open(HASH_STORAGE, "w") as f:
        json.dump(hashes, f, indent=4)  # 딕셔너리를 JSON 형식으로 저장

# 초기화 명령: 파일의 해시 값을 저장
def initialize(file_path):
    """
    파일의 해시 값을 계산하고 저장합니다.
    
    :param file_path: 초기화할 파일 경로
    """
    hashes = load_hashes()  # 기존 저장된 해시 값을 불러옴
    file_hash = calculate_hash(file_path)  # 파일의 해시 값 계산
    hashes[file_path] = file_hash  # 파일 경로를 키로, 해시 값을 값으로 저장
    save_hashes(hashes)  # 업데이트된 해시 값을 파일에 저장
    print(f"{file_path} 해시 초기화 완료: {file_hash}")

# 검사 명령: 파일의 무결성을 확인
def check(file_path):
    """
    파일의 현재 해시 값을 기존 해시 값과 비교해 무결성을 확인합니다.
    
    :param file_path: 검사할 파일 경로
    """
    hashes = load_hashes()  # 기존 저장된 해시 값을 불러옴
    if file_path not in hashes:  # 파일의 해시 값이 저장된 적 없는 경우
        print(f"{file_path} 해시 값이 저장된 적이 없습니다. 먼저 초기화하세요.")
        sys.exit(1)

    current_hash = calculate_hash(file_path)  # 현재 파일의 해시 값을 계산
    if current_hash == hashes[file_path]:  # 해시 값이 일치하면 무결성 유지
        print(f"{file_path} 파일은 변경되지 않았습니다.")
    else:  # 해시 값이 다르면 파일이 수정됨
        print(f"{file_path} 파일이 변경되었습니다! (해시 불일치)")

# 업데이트 명령: 기존 파일 해시 값을 재저장
def update(file_path):
    """
    파일의 해시 값을 다시 계산하고 저장된 값을 업데이트합니다.
    
    :param file_path: 업데이트할 파일 경로
    """
    hashes = load_hashes()  # 기존 저장된 해시 값을 불러옴
    file_hash = calculate_hash(file_path)  # 파일의 새 해시 값 계산
    hashes[file_path] = file_hash  # 파일 경로에 대한 해시 값을 업데이트
    save_hashes(hashes)  # 업데이트된 해시 값을 파일에 저장
    print(f"{file_path} 해시 값이 업데이트되었습니다: {file_hash}")

# 메인 함수: 명령어 인자에 따라 동작
def main():
    """
    프로그램 실행 시 명령어와 인자를 처리합니다.
    사용법:
        python script.py init <file>
        python script.py check <file>
        python script.py update <file>
    """
    if len(sys.argv) != 3:  # 명령어와 파일 경로를 정확히 입력했는지 확인
        print("사용법: python script.py [init|check|update] <file_path>")
        sys.exit(1)

    command = sys.argv[1]  # 명령어 (init, check, update)
    file_path = sys.argv[2]  # 파일 경로

    if not os.path.exists(file_path):  # 입력된 파일이 존재하는지 확인
        print(f"Error: {file_path} 파일이 존재하지 않습니다.")
        sys.exit(1)

    # 명령어에 따라 해당 함수를 호출
    if command == "init":
        initialize(file_path)
    elif command == "check":
        check(file_path)
    elif command == "update":
        update(file_path)
    else:
        print("알 수 없는 명령어입니다. 사용법: init, check, update")

if __name__ == "__main__":
    main()
