# 2026-03-14-EC2 배포 및 환경 변수 설정

## Summary (회의 요약)
EC2 서버 환경 설정을 완료하고(Docker, Docker Compose 설치, 프로젝트 클론), CORS 및 API URL 환경 변수화를 통해 외부에서 Backend와 Frontend 모두 접근 가능한 상태를 만듦.

## Key Decisions (주요 결정 사항)

### CORS 및 API URL을 환경 변수로 관리
- **내용:** `ALLOWED_ORIGINS`와 `VITE_API_URL`을 `compose.yaml`에 하드코딩하지 않고 `.env` 파일로 분리하여 관리함. `compose.yaml`에서는 `${VAR:-기본값}` 문법으로 기본값(localhost)을 지정함.
- **이유:** 로컬 개발 환경과 EC2 배포 환경이 다른 주소를 사용하기 때문. 코드 변경 없이 환경별로 다른 값을 주입하기 위함.

### `develop` 브랜치로 EC2 클론
- **내용:** `git clone -b develop` 으로 develop 브랜치 코드를 EC2에 클론함.
- **이유:** ADR 007 전략에 따라 Phase 1 완료 시 `develop` → `main` 병합 예정이므로, 현 단계에서는 `main`에 병합하기 이름. 배포 작업은 `develop` 기준으로 진행함.

### `.env.example` 관리 방식
- **내용:** `.env`는 `.gitignore`로 차단하고, `.env.example`에는 `localhost` 기본값만 담아 GitHub에 공개함.
- **이유:** 실제 서버 IP 등 민감 정보를 저장소에 노출하지 않기 위함. 개발자가 `.env.example`을 보고 `.env`를 만들 수 있도록 가이드 역할 제공.

## Blockers & Solutions (블로커 & 해결책)

- **문제:** `docker compose up -d` 실행 시 `permission denied while trying to connect to the Docker socket` 에러 발생.
- **해결:** `sudo docker compose up -d`로 실행.

- **문제:** Frontend에서 "Failed to load service status" 에러 발생.
- **해결:** Backend의 CORS `origins`에 `http://localhost:5173`만 있어 EC2 IP에서의 요청이 차단된 것이 원인. `os.getenv("ALLOWED_ORIGINS")` 방식으로 환경 변수화하여 해결.

- **문제:** `compose.yaml`에서 `VITE_API_URL=http://localhost:8000`으로 설정된 채 배포되어 브라우저가 EC2 대신 사용자 PC로 API 요청을 보냄.
- **해결:** `VITE_API_URL`도 환경 변수로 분리하고, EC2의 `.env`에 Public IP를 직접 설정.

## TIL (느낀 점)
1. **로컬/EC2 환경을 분리:** 지금까지 로컬하고 EC2 환경을 어떻게 분리해서 관리하는 지 몰랐는데, 이번에 직접 EC2에 작업하면서 로컬과 EC2를 분리해서 개발하는 흐름을 알게 되었다.
2. **외부에서 접속 시 API 연결이 안 됐던 이유:** localhost는 로컬의 IP를 나타내고, 외부에서는 퍼블릭 IP를 사용해야 한다는 점을 이해했다.
3. 지금까지 간단한 작업이었지만 배포할 때는 항상 기분이 짜릿한 거 같다! 스마트폰으로도 접속이 되어서 기쁘다!
4. **AI 시대의 개발 방식 변화:** `copilot-instructions.md`를 생각보다 자주 수정하게 된다. 대학생 때는 코드 짜는 것에 대부분의 시간을 보냈는데, 요즘은 AI 관련 파일이나 지시사항을 수정하는 데에도 시간을 보내게 되었다. 시대가 바뀌었다는 것이 느껴진다.

## Key Decisions (주요 결정 사항) — copilot-instructions 구조 개선

### instruction 파일 분리
- **내용:** `copilot-instructions.md` 단일 파일(340줄)을 5개 파일로 분리함.
  - `copilot-instructions.md` — 항상 로드되는 핵심 컨텍스트 (Commands, 아키텍처 제약, 워크플로우 트리거)
  - `.github/instructions/ai-pair-programming.instructions.md` (`applyTo: **`) — 페어 프로그래밍 원칙, 코딩 행동 원칙
  - `.github/instructions/python-backend.instructions.md` (`applyTo: backend/**`) — Python/FastAPI 규칙, DB 설계
  - `.github/instructions/svelte-frontend.instructions.md` (`applyTo: frontend/src/**`) — Svelte/TypeScript 규칙
  - `.github/instructions/git-workflow.instructions.md` (`applyTo: **`) — 커밋/PR/Issue 가이드라인
- **이유:** CLAUDE.md 작성 요령(wikidocs.net/333419) 참고. AI가 추측 가능한 내용(프로젝트 개요, 기술 스택)은 제거하고, `applyTo` 패턴으로 필요한 파일 작업 시에만 로드되도록 최적화함.

### 코딩 행동 원칙 적용 범위 명확화
- **내용:** 코딩 행동 원칙(Simplicity First, Surgical Changes 등)은 예외 조건 여부와 관계없이 **항상 적용**으로 변경. 코드 직접 제시 예외 조건은 구문 오류(typo)와 사용자 명시적 허용 2가지로 축소.
- **이유:** 기존에는 "예외 조건으로 코드를 작성할 때만"이라고 명시되어 있어 힌트를 줄 때도 단순하게 줘야 한다는 의도가 불분명했음.

## Action Items (다음 할 일)
- [ ] README에 배포 환경 URL 추가
- [ ] `feature/#6-aws-deploy` → `develop` PR 작성 및 Merge
