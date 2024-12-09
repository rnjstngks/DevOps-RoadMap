# Ansible을 사용하여 구성 관리

**1. 노트북(window 11의 WSL 환경)에서 ansible 설치**

명령 프롬프트에서 아래 명령어 입력
```sh
wsl install
wsl -d Ubuntu
apt update
apt install -y software-properties-common
add-apt-repository --yes --update ppa:ansible/ansible
apt install -y ansible
```

**2. Inventory 생성 및 생성한 Inventory를 기본으로 지정**
```sh
mkdir my-ansible
cd my-ansible
vim inventory.ini
-------
[base]
<생성한 가상머신의 IP>

[nginx]
<생성한 가상머신의 IP>

[app]
<생성한 가상머신의 IP>

[ssh]
<생성한 가상머신의 IP>
-------

vi /etc/ansible/ansible.cfg
-------
[defaults]
inventory = my-ansible/inventory.ini
remote_user = root
ask_pass = false # SSH 암호를 묻는 메시지 여부를 지정, 기본값은 false
-------
```

**3. 역할에 따라 roles/{app,base,nginx,ssh}/tasks/main.yml 파일 작성**

**4. setup.yml 파일에 각 roles에 대한 tag 지정**

**5. 이후 playbook 실행**
ex)
```sh
ansible-playbook setup.yml --tags "base" or ansible-playbook setup.yml
```
