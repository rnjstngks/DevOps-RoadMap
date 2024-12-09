# Terraform 을 사용하여 vSphere에서 가상머신 생성

원래는 DigitalOcean에서 가상머신을 생성하는 프로젝트 인데, 

요금이 발생하는 것 때문에, 이미 구성되어있는 vSphere 환경에서 가상머신을 생성해보도록 하겠습니다.

**1. 노트북 (WSL 환경)에 Terraform을 설치**
```sh
wget -O - https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform
```

**2. main.tf에서 vsphere에 대한 정보 입력**

**3. create_vm.tf에서 생성할 가상머신의 정보 입력**