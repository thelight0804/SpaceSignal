# 2026-02-12-README 업데이트 및 GitHub MCP 설정

## Summary (회의 요약)
README.md 파일에 Docker 실행 방법을 추가하고, VSCode Copilot에 GitHub MCP를 설정함

## Key Decisions (주요 결정 사항)

### README.md에 Getting Started 섹션 추가
- **이유:**
  - SpaceSignal은 초기 단계 프로젝트로 설정이 간단함 (`docker compose up` 한 줄로 실행)
  - GitHub 공식 문서도 README에 "how to get started" 포함을 권장
  - 대규모 프로젝트(GitLab, Immich)는 별도 문서로 분리하지만, 소규모 프로젝트는 README에 포함하는 것이 일반적

## 추가된 내용

### Getting Started 섹션 구성
1. **Prerequisites:** Docker, Docker Compose
2. **How to Run:**
   - 프로젝트 클론
   - `docker compose up` 실행
   - 서비스 접속 URL (Backend API, Frontend, Swagger 문서)
3. **Stopping Services:** `docker compose down`

### VSCode Copilot 전역 설정 - 도구 자동 실행 권한 설정
- **목적:** 읽기 전용 도구는 자동 실행, 쓰기 도구는 확인 후 실행
- **설정 위치:** `%APPDATA%\Code\User\settings.json` (Windows 전역 설정)
- **효과:**
  - 자동 실행: 파일 읽기, 검색, 조회 등의 읽기 전용 작업
  - 확인 필요: 파일 생성/수정/삭제, 터미널 명령 실행 등의 쓰기 작업

### VSCode Copilot에 GitHub MCP 추가
- **시도 과정:**
  - Remote GitHub MCP Server와 Local GitHub MCP Server로 추가 시도
  - 에러 발생으로 사용 불가
- **해결 방법:**
  - 인터넷 검색을 통해 VSCode 확장 기능에 MCP marketplace 발견
  - MCP marketplace를 통해 GitHub MCP 추가 및 테스트 완료

## TIL (느낀 점)

### README 문서 구조의 Best Practice 학습
- 파일별 역할 구분:
  - **README.md:** 프로젝트 소개, 실행 방법 (Getting Started)
  - **CONTRIBUTING.md:** 개발 환경 설정, 코드 기여 가이드
  - **docs/:** 상세한 사용자 가이드, API 문서, 아키텍처 설명

### GitHub MCP
- GitHub MCP를 통해 Copilot의 기능 확장 가능성 확인
- 향후 Copilot을 활용한 Commit, Issue, PR를 편하게 관리할 수 있을 것으로 기대중! (ワクワク)

## Action Items (다음 할 일)
- [ ] Frontend 환경 변수 설정
- [ ] Issue, PR 템플릿 작성
- [ ] #5 PR 작성
