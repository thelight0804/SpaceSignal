# 7. Git Workflow and Branch Strategy

**Status:** Accepted
**Date:** 2025-12-21

## Context (배경 및 문제점)
- SpaceSignal 프로젝트는 Phase 1부터 Phase 3까지 단계적으로 개발되며, 각 기능을 독립적으로 관리할 필요가 있음.
- 1인 프로젝트이지만 실무 Git 워크플로우를 적용하여 협업 역량을 강화 함.
- 기능 개발, 버그 수정, 문서 작업 등을 체계적으로 추적하고 이력을 관리해야 함.
- GitHub Issues, Pull Requests, Project Board(칸반)를 활용하여 작업 진행 상황을 시각화해야 함.
- 회사에서 사용 중인 워크플로우와 일관성을 유지하여 실무 경험을 축적하고자 함.

## Decision (결정 사항)
Git 브랜치 전략으로 **Modified GitHub Flow**(develop 브랜치 추가)를 채택하고, Issue 기반 개발 프로세스를 적용함.

### 1. 브랜치 전략
- **`main`**: 항상 배포 가능한 상태. Phase 완료 시 태그 생성 (예: `v0.1.0`).
- **`develop`**: 다음 릴리스를 위한 통합 브랜치. 모든 feature 브랜치는 여기서 분기하고 병합됨.
- **`feature/#N-기능명`**: 새로운 기능 개발 (예: `feature/#15-backend-hello-world`).
- **`fix/#N-버그명`**: 버그 수정 (예: `fix/#25-docker-port-conflict`).
- **`docs/#N-문서명`**: 문서 작업 (예: `docs/#30-adr-007-git-workflow`).

### 2. 브랜치 네이밍 규칙
- **형식**: `타입/#이슈번호-간단한-설명`
- **구분자**: 하이픈(`-`) 사용 (언더스코어 `_` 금지).
- **예시**: `feature/#10-satellite-position-api`, `fix/#20-tle-parsing-error`

### 3. Issue 관리
- **제목 규칙**: `영역 작업명` (예: `Backend Hello World 구현`)
- **Labels**: Type (`feature`, `bug`, `documentation`), Area (`backend`, `frontend`, `infrastructure`), Phase (`phase-1`, `phase-2`, `phase-3`), Priority (`priority-p0`, `priority-p1`, `priority-p2`)
- **칸반 보드**: Backlog → Ready → In Progress → In Review → Done
- **Sub-issues**: 큰 작업은 Epic Issue로 관리하고, 독립적인 Sub-issue들을 생성하여 `develop`에서 각각 분기

### 4. Pull Request 규칙
- **제목 형식**: `작업명 (#이슈번호)` (예: `Backend Hello World 구현 (#15)`)
- **본문**: `Closes #이슈번호` 포함하여 Issue 자동 종료
- **병합 전략**: Squash and Merge 또는 Rebase and Merge 사용
- **Self-Review**: 1인 프로젝트이므로 본인이 approve하되, AI 도구(GitHub Copilot, ChatGPT)로 코드 리뷰 수행

### 5. Commit Message: Conventional Commits
- **형식**: `<타입>: <제목> #이슈번호`
- **타입**: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`
- **예시**: `feat: Add FastAPI health endpoint #15`

### 6. 릴리스 전략 (Walking Skeleton)
- Phase 하나씩 완료할 때마다 `develop` → `main` 병합하여 AWS EC2에 배포.
- Semantic Versioning: Phase 1 (`v0.1.0`) → Phase 2 (`v0.2.0`) → Phase 3 (`v1.0.0`)
- `main` 브랜치 push 시 GitHub Actions로 자동 배포.

## Alternatives (대안)
- **순수 GitHub Flow**: `develop` 브랜치 없이 `main`에 바로 병합. 1인 프로젝트에는 충분하지만, 실무 경험과의 연결성이 낮고 통합 테스트 완충지대 부족.
- **Git Flow**: `main`, `develop`, `release`, `hotfix` 등 복잡한 브랜치 구조. 1인 프로젝트에는 과도한 복잡도와 오버헤드 발생.
- **Trunk-Based Development**: 매우 짧은 주기로 main에 직접 커밋. CI/CD 성숙도가 높아야 하므로 초기 프로젝트에는 부적합.

## Consequences (결과 및 효과)

### Positive (장점)
- **실무 경험 축적**: 회사에서 사용 중인 develop 브랜치 패턴과 일치하여 실무 워크플로우를 체득함.
- **트레이서빌리티**: Issue → PR → Commit 연결로 코드 변경의 "왜"를 명확히 추적 가능.
- **코드 품질 유지**: PR 단위로 CI 자동 실행, AI 도구를 활용한 코드 리뷰로 버그 조기 발견.
- **릴리스 관리**: Phase별 명확한 태그(v0.1.0, v0.2.0, v1.0.0)와 배포 이력 추적.
- **점진적 배포 경험**: Walking Skeleton 전략으로 Phase마다 실제 AWS 배포를 경험하여 리스크 분산.

### Negative (단점/리스크)
- **1인 프로젝트 오버헤드**: Issue 생성, PR 작성, Self-Review 등의 부가 작업 시간 소요.
- **Self-Review 한계**: 타인의 코드 리뷰 없이 본인이 approve하므로 놓칠 수 있는 버그 존재 (AI 도구로 보완).
- **단계적 적용 필요**: 초기에는 워크플로우 적응 시간이 필요하며, 익숙해질 때까지 개발 속도가 다소 느릴 수 있음.