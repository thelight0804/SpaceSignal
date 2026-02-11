# 2026-02-11-Docker Compose 작성 및 설정

## Summary (회의 요약)
compose.yaml 파일을 작성하여 Backend와 Frontend 컨테이너를 통합 관리하는 환경을 구축함. Volumes를 활용한 코드 자동 반영 설정을 완료하고, Docker Compose의 핵심 개념(build, volumes, depends_on)을 학습함. Backend와 Frontend 모두 코드 변경 시 자동으로 반영되도록 설정 완료.

## Key Decisions (주요 결정 사항)

### compose.yaml 파일명 사용 (docker-compose.yml 아님)
- **내용:** 파일명을 `compose.yaml`로 결정
- **이유:** 
  - Docker 공식 문서가 권장하는 최신 표준
  - `docker-compose.yml`도 호환되지만 신규 프로젝트는 `compose.yaml` 권장
  - 파일 우선순위: compose.yaml > compose.yml > docker-compose.yaml > docker-compose.yml

### version 필드 생략
- **내용:** compose.yaml에서 `version: '3'` 등의 버전 필드를 명시하지 않음
- **이유:** 
  - Docker Compose v1.27.0 이상에서는 version 필드가 선택사항
  - 자동으로 최신 포맷으로 해석됨

### Volumes를 통한 코드 자동 반영 설정
- **내용:**
  1. Backend: `./backend:/app` (Bind Mount)
  2. Frontend: `./frontend:/app` + `/app/node_modules` (Bind Mount + Anonymous Volume)
- **이유:**
  - 코드 변경 시 컨테이너 재빌드 없이 즉시 반영

### depends_on으로 시작 순서 제어
- **내용:** Frontend가 Backend에 의존하도록 설정
- **이유:**
  - 논리적 의존성 명시 (문서화 효과)
  - 향후 API 연동 대비

## Blockers & Solutions (블로커 & 해결책)

### 문제 1: Backend 코드 변경이 반영되지 않음
- **현상:** main.py 수정 후 저장해도 FastAPI가 재시작하지 않음
- **원인:** uvicorn에 `--reload` 옵션 누락
- **해결:** 
  - backend/Dockerfile의 CMD에 `--reload` 옵션 추가

### 문제 2: Frontend 코드 변경이 반영되지 않음
- **현상:** App.svelte 수정 후 저장해도 브라우저가 자동 새로고침하지 않음
- **원인:** Docker 볼륨 마운트 시 파일 시스템 이벤트(inotify)가 제대로 전달 안 됨 (Windows + Docker 환경)
- **해결:**
  - vite.config.js에 polling 방식 추가

## TIL (느낀 점)

### Docker Compose를 사용한 개발 환경의 변화
- **이전:** 가상 환경 활성화 → Backend 서버 실행 → Frontend 서버 실행 (3단계)
- **현재:** `docker compose up` 하나로 모든 서버 실행 (1단계)
- 가상 환경의 역할이 변화함:
  - **실행 환경** → Docker가 담당
  - **개발 환경** → 가상 환경 유지 (VS Code IntelliSense, 자동완성, 타입 체킹을 위해 필요)
- 가상 환경과 각 서버를 실행할 필요 없이 docker 한 번에 관리할 수 있게 되어서 편리해졌다!
- 다만 가상 환경은 여전히 유지하는 것이 좋음

### 개발 진행이 느림
- 퇴근 후 진행하다 보니 운동, 집안일 등 다른 일과 병행하다 보니 개발 속도가 느림
- 최근에는 영어 토익 공부도 시작하고 있어서 더욱 시간이 부족함
- 개발 진행이 느려질수록 흥미도가 떨어지는 거 같아 걱정이지만, 30분이라도 꾸준히 시간을 내서 진행할 수 있게 노력해야겠다 😣

## Action Items (다음 할 일)
- [ ] README에 Docker 실행 방법 추가
