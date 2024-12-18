# Blue - Green 배포

**Blue - Green 배포란?**

애플리케이션의 업데이트나 배포 시 다운타임을 최소화하여 리스크 감소를 위해 사용되는 배포 전략 입니다.

ArgoCD를 사용하여 Blue - Green 배포를 진행 해보도록 하겠습니다.
--------------------------------------------------------------------------------------------------------------------------------------------
**ArgoCD 설치 (Helm)**
```sh
helm repo add argo https://argoproj.github.io/argo-helm
helm install argocd argo/argo-cd --version 7.7.10
```

**ArgoCD - rollout 설치 (Helm)**
```sh
helm repo add argo https://argoproj.github.io/argo-helm
helm install argo-rollout argo/argo-rollouts
```
--------------------------------------------------------------------------------------------------------------------------------------------

아래 과정 부터는 Github Action을 통해 진행 합니다.

**1. Docker 이미지 빌드**

**2. 빌드한 이미지 Docker hub에 Push**

**3. rollout.yaml 파일에서 이미지 버전 수정**

위의 과정을 Github Action 통해 진행 해보도록 하겠습니다.

YML 파일의 위치는 **.github/blue-green-deploy.yml** 입니다.