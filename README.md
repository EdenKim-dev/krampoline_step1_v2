# krampoline-step1

## 소개

`krampoline-step1`은 krampoline의 가장 기본적인 예제입니다. 
이 저장소에서는 `index.py`를 사용하여 3000번 포트에서 서버를 열고 "hello krampoline!"를 출력하는 예제를 제공합니다.


쿠버네티스 구성은 다음과 같습니다.
![image](https://github.com/MonoKim01/krampoline-step1/assets/85483855/248fb708-aa34-446b-9d0c-8bb30c9bc5f4)

1. Deployment
  - 목적: 애플리케이션의 레플리카(복제본)를 관리하고 업데이트하는 방식을 정의.
    - 기능:
      - 애플리케이션의 레플리카 수를 지정하고 유지.
      - 롤링 업데이트를 사용하여 애플리케이션의 새 버전을 점진적으로 배포.
      - 애플리케이션의 상태를 모니터링하고, 필요한 경우 레플리카를 재시작.
2. Service
  - 목적: 네트워크 경로를 사용하여 일련의 파드에 액세스하는 방법을 정의.
    - 기능:
      - 파드의 집합에 대한 로드 밸런싱 제공.
      - 하나의 IP와 포트를 사용하여 파드 집합에 액세스.
      - 서비스 발견을 위한 내부 DNS 이름 제공.
3. Ingress
  - 목적: HTTP 및 HTTPS 트래픽을 클러스터 서비스로 라우팅하는 방법을 정의.
    - 기능:
      - URL 경로 기반의 트래픽 라우팅. ( krampoline의 경우 매우 중요함. )
      - 호스트 기반 트래픽 라우팅.
      - SSL/TLS 종료 및 리다이렉트.

이 외의 다른 구성요소들은 해당 저장소에서 설명하지 않습니다.

## 수정이 필요한 파일

### k8s/deployment.yaml
```yaml
...
  template:
    metadata:
      labels:
        app: krampoline
    spec:
      containers:
        - name: krampoline
          # 여러분의 image 주소를 입력해주세요.
          # 해당 image 주소는 IDE 에서 d2hub 기능을 이용해서 생성하실 수 있습니다.
          # 다음은 예시입니다.
          image: krmp-d2hub-idock.9rum.cc/dev-test/repo_3cdea8ed6566

```

### k8s/ingress.yaml
```yaml
...
spec:
  rules:
    - http:
        paths:
          - backend:
              serviceName: krampoline
              servicePort: 3000
            # 여러분의 app path 를 넣어주세요.
            # 해당 app path 주소는 IDE 에서 kargo 기능을 이용해서 생성하실 수 있습니다.
            # 다음은 예시입니다.
            path: /ka74894a7123da(/|$)(.*)

```

## 기본적인 명령어
자주 질문 주시는 명령어 입니다. 더 다양한 명령어는 [Kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)을 참고해주세요.

### log 보는 법
1. `kubectl get pods`를 이용해서 pod의 이름을 봅니다. ( my-pod 라고 가정 )
2. `kubectl logs -f my-pod`를 이용하면 실시간으로 pod의 로그를 볼 수 있습니다.

### pod를 재시작 하는 법
1. `kubectl rollout restart deployment/krampoline`을 이용하면 krampoline을 이름으로 가지는 deployment를 재시작합니다.


## 필요 사항

- 기본적인 IDE 사용법 (자세한 내용은 가이드 문서 참조)

## 주의 사항

- 꼭 `Dockerfile`과 `k8s` 폴더를 프로젝트에 포함시켜주세요.
  - 프로젝트의 루트 (`/`) 위치에 포함되게 해주세요.
- `k8s/deployment.yaml`과 `k8s/ingress.yaml` 파일은 필히 확인하시기 바랍니다.
- `main`브런치에 작성해주세요.
