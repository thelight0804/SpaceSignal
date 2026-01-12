# 2026-01-12-GitHub Issues 이슈 생성

## Summary (회의 요약)
GitHub Issues 템플릿 구조와 Projects(칸반 보드) 설정 방법을 확립하고, Phase 1의 첫 Main Issue와 Sub Issues를 생성함. Walking Skeleton 전략에 따라 배포 파이프라인 확립에 집중하는 최소 범위로 이슈를 정리함.

## Key Decisions (주요 결정 사항)

### Phase 1-1
- **내용:** 첫 Main Issue는 FastAPI Health Check + Docker + AWS 배포만 포함. TLE 데이터, Skyfield, 위성 API는 별도 Main Issue로 분리.
- **이유:** Walking Skeleton 전략에 따라 "배포 파이프라인 확립"을 최우선 목표로 설정. 위성 기능 없이 배포 경험을 먼저 쌓고 이후 기능 확장. ADR 문서(001, 002, 005) 검토 결과 GUI 선행 학습 후 Terraform 코드화 전략 확인.

### Sub Issues 3개 생성
- **내용:** #2 FastAPI 프로젝트 초기 설정, #5 Docker 구성, #6 AWS EC2 배포로 구성. 각 Issue는 독립적으로 작업 가능하도록 설계.
- **이유:** ADR 007의 Modified GitHub Flow 전략에 따라 모든 브랜치를 develop에서 직접 분기. 병렬 작업 가능하도록 의존성 최소화.

### AI 페어 프로그래밍 가이드라인 수립
- **내용:** copilot-instructions.md에 "AI 페어 프로그래밍 가이드라인" 섹션 추가. AI는 학습을 돕는 보조 도구로만 활용하며, 완성된 코드를 직접 작성해주는 방식은 지양. 학습 자료를 우선 참고하고, 에러/개념 이해에만 AI 활용.
- **이유:** FastAPI를 처음 다루므로 책을 통한 체계적 학습이 필요. AI가 코드를 바로 작성해주면 학습 효과가 떨어지므로, 설명과 힌트 위주로 도움을 받는 방식 채택.

### Python 개발 환경 설정 전략 수립
- **내용:** 로컬 Python + Docker 병행 전략 채택. 개발 시에는 로컬에 설치된 Python 사용, 배포 시에는 Docker 컨테이너 사용. Python 버전 관리를 위해 pyenv-win 도입.
- **이유:** FastAPI 학습 초기에는 빠른 개발 사이클이 중요하므로 로컬 Python 환경 구축. Walking Skeleton 전략에 따라 Issue #2(FastAPI 초기 설정)에서는 로컬 개발에 집중하고, Issue #5(Docker 구성)에서 컨테이너화 진행. pyenv를 통해 프로젝트별 Python 버전 관리 및 팀원 간 환경 통일.

### 가상환경 사용 결정
- **내용:** 프로젝트 전용 가상환경(.venv) 사용. 패키지 격리를 통해 의존성 관리 및 requirements.txt 생성으로 Docker 배포 준비.
- **이유:** 프로젝트별 패키지 독립성 확보. Issue #5에서 Docker 구성 시 `pip freeze > requirements.txt`로 정확한 의존성 파일 생성 필요. 전역 Python에 설치 시 관련 없는 패키지까지 Docker 이미지에 포함되는 문제 방지.

## Blockers & Solutions (블로커 & 해결책)
- **문제:** 초기 Issue 구조가 Phase 1 전체 기능(TLE, Skyfield, 위성 API 등)을 포함하여 범위가 너무 넓었음.
- **해결:** ADR 문서(001, 002, 005) 및 회의록(2025-12-14, 2025-12-15) 재검토 후 Walking Skeleton 전략 재확인. Phase 1-1을 "배포 파이프라인 확립"만으로 축소하고 위성 기능은 Phase 1-2로 분리 예정.

## TIL (느낀 점)
- GitHub Issues를 Main Issue + Sub Issues 구조로 관리하면 큰 작업을 체계적으로 추적 가능.
- AWS 배포 과정을 문서화하는 것이 Terraform 학습의 발판이 됨(GUI → IaC 전환 전략).
- 공식 문서와 학습 자료를 먼저 참고하고, 막히는 부분만 AI에게 질문하는 방식이 효과적.
- pyenv는 Python 버전 관리 도구로, 프로젝트별로 다른 Python 버전을 독립적으로 사용 가능.
- Mac에는 pyenv, Windows에는 pyenv-win을 사용한다.
- 가상환경(venv)은 프로젝트별 패키지 격리를 위해 사용한다.

## Action Items (다음 할 일)
- [ ] FastAPI 패키지 설치
- [ ] Sub Issue #2: FastAPI 프로젝트 초기 설정 작업 시작
- [ ] Health Check API 구현 및 로컬 테스트