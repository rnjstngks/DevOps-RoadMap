# DB 자동 백업

아래 과정을 통해 진행을 하도록 하겠습니다.

**1. 가상머신 생성**

- Terraform을 사용하여 가상머신을 생성 해줍니다.
- **main.tf** 에서는 가상머신을 생성하기 위한 사전 data를 정의 해줍니다.
- **create_vm.tf** 에서는 가상머신을 생성할 때, 원하는 스펙, 작업 등을 정의 해줍니다.

**2. ansible 사용하여 MongoDB 서비스 설치**

- mongodb, mongodb-clients 설치
```sh
# ansible-playbook -i inventory.ini setup.yml --tags "db"
``` 

- 더미 데이터 삽입
```sh
# ansible-playbook -i inventory.ini setup.yml --tags "data"
``` 

**3. DB에 더미 데이터 저장 후 백업**

