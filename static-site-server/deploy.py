import paramiko
import os
from scp import SCPClient

def ssh_connect(host, username, password=None, key_file=None):
    """원격 서버에 SSH 연결을 생성합니다."""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        if key_file:
            client.connect(hostname=host, username=username, key_filename=key_file)
        else:
            client.connect(hostname=host, username=username, password=password)
        print("SSH 연결 성공!")
        return client
    except Exception as e:
        print(f"SSH 연결 실패: {e}")
        return None

def upload_files(ssh_client, local_dir, remote_dir):
    """로컬 디렉토리의 파일을 원격 서버로 업로드합니다."""
    try:
        with SCPClient(ssh_client.get_transport()) as scp:
            scp.put(local_dir, remote_path=remote_dir, recursive=True)
        print(f"파일 업로드 성공: {local_dir} -> {remote_dir}")
    except Exception as e:
        print(f"파일 업로드 실패: {e}")

def configure_nginx(ssh_client, remote_dir):
    """Nginx 설정을 수정하고 서비스를 재시작합니다."""
    commands = [
        f"sudo sed -i 's|root .*;|root {remote_dir};|g' /etc/nginx/sites-available/default",
        "sudo sed -i 's|index .*;|index index.html;|g' /etc/nginx/sites-available/default",
        "sudo nginx -t",  # 설정 파일 테스트
        "sudo systemctl restart nginx"  # Nginx 서비스 재시작
    ]

    try:
        for command in commands:
            stdin, stdout, stderr = ssh_client.exec_command(command)
            print(stdout.read().decode())
            error = stderr.read().decode()
            if error:
                print(f"명령 실행 중 오류 발생: {error}")
        print("Nginx 설정 완료 및 서비스 재시작!")
    except Exception as e:
        print(f"Nginx 설정 실패: {e}")

def main():
    # 사용자 입력
    host = input("원격 서버 IP 또는 호스트명: ")
    username = input("SSH 사용자 이름: ")
    password = input("SSH 비밀번호 (키 파일 사용 시 생략): ")
    key_file = input("키 파일 경로 (없으면 생략): ") or None
    local_dir = input("로컬 정적 파일 경로 (예: ./static_site): ")
    remote_dir = input("원격 서버 업로드 경로 (예: /var/www/html): ")

    # SSH 연결
    ssh_client = ssh_connect(host, username, password=password, key_file=key_file)
    if not ssh_client:
        return

    # 파일 업로드
    upload_files(ssh_client, local_dir, remote_dir)

    # Nginx 설정 및 재시작
    configure_nginx(ssh_client, remote_dir)

    # SSH 연결 종료
    ssh_client.close()
    print("배포 완료!")

if __name__ == "__main__":
    main()
