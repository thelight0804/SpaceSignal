# 2026-01-20-Docker 기초 학습 및 requirements.txt 생성

## Summary (회의 요약)
GitHub Issue #5 시작 단계로 Docker의 필요성과 컨테이너 개념을 학습하고, Backend의 requirements.txt 파일을 생성함. Python 의존성 관리 방식에 대해 이해함.

## Key Decisions (주요 결정 사항)

### requirements.txt에 명시할 패키지 범위 결정
- **내용:** 
  - 핵심 패키지만 명시: `fastapi`, `uvicorn`, `starlette`
  - 간접 의존성(pydantic, anyio 등)은 제외
- **이유:** 
  - 간결성: 직접 사용하는 패키지만 관리
  - 의존성 트리는 pip가 자동으로 해결
  - `starlette`는 코드에서 직접 import하므로 명시적으로 포함

### 버전 고정 방식 채택
- **내용:** `==` 연산자로 정확한 버전 고정 (예: `fastapi==0.128.0`)
- **이유:** 
  - 재현 가능성(Reproducibility) 보장
  - 다른 환경(팀원 PC, Docker, AWS)에서 동일한 버전 설치
  - 위성 도메인 특성상 계산 정확성이 중요하므로 환경 일관성 필수

### 의존성 관리 도구 선택: 현재는 수동, Phase 2 이후 Poetry 도입 검토
- **내용:** 
  - Phase 1: requirements.txt 수동 관리
  - Phase 2 이후: Poetry 전환 고려
- **이유:** 
  - 현재 학습 단계: Docker 집중 학습 필요, 도구 복잡도 최소화
  - 의존성이 적음 (3개): 수동 관리 가능한 수준
  - Poetry는 실무 표준이므로 향후 도입 가치 있음

## Blockers & Solutions (블로커 & 해결책)

### 문제 1: Docker와 requirements.txt의 관계 이해 부족
- **원인:** Docker를 기초만 학습했고, 실제 프로젝트 적용은 처음
- **해결:** 
  - requirements.txt는 Dockerfile에서 읽어서 패키지 자동 설치하는 용도

### 문제 2: Python 내장 모듈 vs 외장 모듈 구분 방법
- **해결:** 
  - `pip freeze` 결과에 없으면 내장 모듈
  - Python 공식 문서 "Standard Library" 확인
  - 예: `datetime`(내장), `fastapi`(외장)

### 문제 3: pip freeze 출력 결과 해석
- **현상:** 설치한 적 없는 19개 패키지가 출력됨
- **해결:** 
  - `pipdeptree`로 의존성 트리 확인
  - fastapi → starlette → anyio → idna 같은 간접 의존성 이해
  - 직접 설치(fastapi, uvicorn)와 간접 설치(pydantic, h11 등) 구분

## TIL (느낀 점)

### Docker 개념 정리
- **컨테이너화의 가치:**
  - 개발 환경 통일: 모든 팀원이 동일한 Python, Node.js 버전 사용
  - "내 PC에선 되는데" 문제 해결
  - AWS 배포 시에도 동일한 이미지 사용 가능
- **SpaceSignal 아키텍처:**
  - Backend Container (Python/FastAPI)
  - Frontend Container (Node.js/Svelte)
  - Docker Compose로 두 컨테이너 통합 관리 (오케스트라 지휘자!)

### Python 의존성 관리 생태계
- **언어별 의존성 파일:**
  - Python: `requirements.txt` (pip)
  - Node.js: `package.json` (npm)
  - Java: `pom.xml` (maven)
- **실무 도구들:**
  - Poetry: 현재 회사에서 사용 중인 도구이므로, 추후에 직접 사용해보자!

### requirements.txt 파일 테스트
- `pip install -r requirements.txt` 실행 결과:
  - "Requirement already satisfied": 이미 설치되어 있음

## Action Items (다음 할 일)
- [x] GitHub Issue #5 확인
- [x] Docker 개념 학습
- [x] requirements.txt 생성 및 테스트
- [ ] Backend Dockerfile 작성
- [ ] Backend Docker 이미지 빌드 및 테스트
- [ ] Frontend Dockerfile 작성
- [ ] docker-compose.yml 작성
- [ ] 전체 시스템 Docker 환경 테스트