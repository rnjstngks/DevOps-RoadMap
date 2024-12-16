# DB 자동 백업

아래 과정을 통해 진행을 하도록 하겠습니다.

**1. 가상머신 생성**

- Terraform을 사용하여 가상머신을 생성 해줍니다.
- Terraform을 통해 가상머신을 생성해주는 방법은 이전에 진행했던 iac-on-vmware 폴더의 내용을 참고하면 됩니다.

**2. ansible 사용하여 MongoDB 서비스 설치**


**3. DB에 더미 데이터 저장 후 백업**

위의 모든 과정은 Github Action을 통해 진행을 하도록 하겠습니다.

=> Github Action Yaml 파일은 ./github/ 디렉터리에 위치해 있습니다.
