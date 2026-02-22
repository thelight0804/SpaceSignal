# 2026-02-22-Frontend 환경 변수 설정, CORS 이해, GitHub 템플릿 작성 및 PR 코드 리뷰 반영

## Summary (회의 요약)
Frontend 환경 변수(`VITE_API_URL`)를 설정하고, Docker 환경에서 발생한 CORS 문제를 Backend의 `CORSMiddleware`를 활용하여 해결함. 이후 GitHub Issue 및 PR 템플릿을 작성하고 `copilot-instructions.md`에 이슈 작성 가이드라인을 추가함

## Key Decisions (주요 결정 사항)

### 환경 변수 방식으로 API URL 관리
- **내용:** `fetch("http://127.0.0.1:8000/health")` 하드코딩 → `import.meta.env.VITE_API_URL` 환경 변수로 변경
- **이유:** 로컬 개발, Docker, 프로덕션 등 환경별로 다른 URL을 유연하게 관리하기 위함

### CORS 해결 방법으로 Backend CORSMiddleware 선택
- **내용:** Vite Proxy 대신 FastAPI의 `CORSMiddleware`로 `http://localhost:5173` 출처를 허용
- **이유:**
  - Vite Proxy는 개발 서버에서만 동작하며, `rewrite` 설정 등 추가 복잡성이 있음
  - Backend에 이미 `CORSMiddleware`가 설정되어 있었음
  - 브라우저가 직접 Backend에 요청하는 구조가 현재 단계에서 더 단순함

## Blockers & Solutions (블로커 & 해결책)

- **문제:** `VITE_API_URL=http://backend:8000`으로 설정 시 브라우저에서 접근 불가
  - **해결:** `backend`는 Docker 내부 호스트네임으로, 브라우저(Docker 외부)에서는 인식 불가. 브라우저가 접근 가능한 `http://localhost:8000`으로 변경

- **문제:** compose.yaml의 `environment`가 `.env` 파일 값을 오버라이드하여 `http://backend:8000`이 계속 적용됨
  - **해결:** compose.yaml에서 `environment` 섹션 제거

- **문제:** Vite Proxy 설정 시 `/api` 경로가 `http://backend:8000/api/health`로 전달되어 404 발생
  - **해결:** `rewrite` 옵션 미적용 문제. 방법 자체를 CORS 방식으로 전환하여 해결

## TIL (느낀 점)
- CORS가 어떤 원리의 에러인지는 이해했지만, 실제로 CORS의 문제를 해결하는 과정은 정확히 이해하지 못했다...

## GitHub Issue 및 PR 템플릿 작성

### 작업 내용
- `.github/ISSUE_TEMPLATE/` 디렉토리에 3개의 Issue 템플릿 생성
  - `epic.md`: Phase 단위 대형 이슈 템플릿 (`[Phase X-X]` 형식 제목)
  - `feature.md`: 기능 개발 및 작업 단위 이슈 템플릿
  - `bug_report.md`: 버그 리포트 템플릿 (`[Bug]` 접두사 제목)
  - `config.yml`: 빈 이슈 생성 비활성화 설정
- `copilot-instructions.md`에 `## GitHub Issue 작성 가이드라인` 섹션 추가
  - 이모지 사용 금지 규칙 명시
  - 세 가지 템플릿 구조를 코드 블록으로 명시하여 AI가 일관된 형식으로 이슈를 작성할 수 있도록 함

### 주요 결정 사항
- Feature 템플릿의 Tasks는 flat하게 유지 (소제목 없음)
  - 대부분의 Feature 이슈는 단일 영역 작업이므로 소제목이 불필요
  - 필요한 경우 작성자가 직접 소제목을 추가하는 방식으로 유연성 확보

## PR 템플릿 작성

### 작업 내용
- `.github/PULL_REQUEST_TEMPLATE.md` 생성
- `copilot-instructions.md`에 `## GitHub Pull Request 작성 가이드라인` 섹션 추가

## Copilot 코드 리뷰 검토 및 반영 (PR #8)

### 배경
PR #8에서 Copilot이 제안한 4개의 코드 리뷰 코멘트를 하나씩 검토하여 타당성을 판단하고 처리함.

### 코멘트별 결정 사항

#### 코멘트 1: `App.svelte` - `VITE_API_URL` 폴백 추가 → 무시
- **제안:** `import.meta.env.VITE_API_URL || 'http://localhost:8000'` 폴백 추가
- **결정:** 무시
- **이유:** 폴백을 넣으면 `.env` 설정 누락 시에도 앱이 정상 동작하여 설정 실수를 숨겨버림. 환경 변수가 없을 때 에러를 명확히 드러내는 현재 방식이 더 올바른 동작임

#### 코멘트 3: `frontend/.vite/` - `.gitignore` 추가 → 처리 완료
- `.gitignore` 하단에 `.vite/`가 이미 포함되어 있음을 확인
- 이미 추적 중이던 파일은 `git rm -r --cached frontend/.vite/`로 추적 해제

#### 코멘트 4 & 2: `compose.yaml` `environment` 추가 → 처리 완료
- **내용:** `compose.yaml` frontend 서비스에 `VITE_API_URL=http://localhost:8000` 추가
- **이유:**
  - `frontend/.env` 파일 없이도 동작하여, README에 `.env` 생성 단계를 별도로 안내할 필요가 없어짐 (코멘트 2 해결)
  - 설정이 `compose.yaml` 한 곳에 집중됨
- **참고:** 이전에 CORS 문제로 `environment`를 제거했던 것과 `VITE_API_URL`은 독립적인 문제. `VITE_API_URL`은 브라우저가 백엔드로 요청을 보낼 URL을 결정하고, CORS는 브라우저가 그 요청을 허용할지 결정함

## Action Items (다음 할 일)
- [ ] #5 PR Merge
- [ ] #6 Issue 작업 진행
