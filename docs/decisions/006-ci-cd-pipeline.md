# 6. CI/CD Pipeline with GitHub Actions

**Status:** Accepted
**Date:** 2025-12-18

## Context (배경 및 문제점)
- SpaceSignal은 AWS EC2에 Docker 컨테이너 기반으로 배포되며, 지속적인 기능 추가와 버그 수정이 예상됨.
- 수동 배포는 휴먼 에러 위험이 높고, 배포 재현성이 낮으며, 시간이 많이 소요됨.
- 코드 품질 유지(테스트, 린트)와 자동화된 배포 파이프라인이 필요함.
- GitHub Actions, GitLab CI, Jenkins, CircleCI 등 다양한 CI/CD 도구 중 선택이 필요함.

## Decision (결정 사항)
CI/CD 도구로 **GitHub Actions**를 선정하고, 다음과 같은 파이프라인 전략을 따름:

### 1. CI/CD 도구: GitHub Actions
- **이유:** 이미 GitHub에서 코드를 관리하고 있어 별도 서비스 연동 불필요.
- 실무에서 널리 사용되는 도구로, 학습한 내용을 실무 환경에 바로 적용 가능.
- YAML 기반 설정으로 코드로 관리 가능 (Pipeline as Code).

### 2. CI (Continuous Integration) 파이프라인
Pull Request 및 main 브랜치 push 시 자동 실행:

#### Backend (Python/FastAPI)
- **Linting:** `ruff` 또는 `flake8`로 코드 스타일 검사.
- **Type Checking:** `mypy`로 타입 힌트 검증.
- **Testing:** `pytest`로 유닛 테스트 및 API 테스트 실행.
- **Coverage:** 테스트 커버리지 측정 (목표: 80% 이상).

#### Frontend (Svelte/TypeScript)
- **Linting:** `eslint`로 TypeScript 코드 검사.
- **Type Checking:** `tsc --noEmit`으로 타입 에러 검증.
- **Testing:** `vitest` 또는 `jest`로 컴포넌트 테스트 실행.
- **Build Test:** `npm run build`로 빌드 가능 여부 확인.

### 3. CD (Continuous Deployment) 파이프라인
main 브랜치로 머지 후 자동 배포:

#### 배포 전략: Docker 기반 Rolling Restart
단일 EC2 인스턴스에서 `docker-compose up -d`로 컨테이너를 재시작하는 방식.

1. **Docker Image Build:** 
   - Backend와 Frontend를 각각 Docker 이미지로 빌드.
   - GitHub Container Registry (ghcr.io)에 푸시.
   - 이미지 태그: `latest` 및 Git Commit SHA.

2. **AWS EC2 배포:**
   - SSH를 통해 EC2 인스턴스에 접속.
   - 새 Docker 이미지를 Pull.
   - `docker-compose pull && docker-compose up -d`로 컨테이너 재시작.
   - Health Check 후 이상 없으면 배포 완료.

3. **Secrets 관리:**
   - GitHub Secrets에 민감 정보 저장:
     - `EC2_SSH_KEY`: 배포 전용 SSH Private Key (최소 권한 사용자)
     - `EC2_HOST`: EC2 인스턴스 IP/도메인
     - Database 연결 정보 (RDS endpoint, credentials)
     - API Keys (TLE 데이터 소스 등)
   - **Environment secrets 활용:** Phase 2+에서 Production/Staging 환경별로 secrets 분리하여 접근 제어 강화.
   - **최소 권한 원칙:** SSH key는 배포 전용 사용자(deploy-user)로 제한하고, Docker 관련 명령만 실행 가능하도록 설정.

### 4. 단계별 구현 전략
#### Phase 1 (초기 배포)
- **간단한 CI:** Lint + Type Check + Build Test만 수행.
- **수동 배포:** `workflow_dispatch`로 수동 트리거 가능한 배포 워크플로우 구성.
- **목표:** CI 파이프라인 경험 축적 및 배포 프로세스 검증.

#### Phase 2 (자동 배포)
- **CD 파이프라인 추가:** main 브랜치 머지 시 자동으로 EC2에 배포.
- **Environment secrets:** Production/Staging 환경별 secrets 분리.
- **테스트 강화:** 유닛 테스트 및 통합 테스트 추가.
- **알림:** Discord/Slack 웹훅으로 배포 결과 알림.

#### Phase 3 (고도화)
- **Staging 환경:** Dev/Staging/Production 환경 분리.
- **진정한 Blue-Green 배포:** Nginx/Traefik 리버스 프록시 도입하여 무중단 배포 구현.
- **Rollback 전략:** 배포 실패 시 이전 버전으로 자동 롤백.
- **보안 강화:** OIDC 기반 인증 또는 AWS SSM을 통한 SSH 키 관리로 전환.
- **성능 모니터링:** Prometheus/Grafana 연동.

## Consequences (결과 및 효과)
### Positive (장점)
- **자동화:** 코드 머지 후 자동으로 테스트 및 배포되어 개발 속도 향상.
- **안정성:** CI에서 코드 품질 검증 후 배포하여 프로덕션 버그 감소.
- **재현성:** 배포 프로세스가 코드로 정의되어 언제든 동일한 방식으로 배포 가능.
- **빠른 피드백:** Pull Request 시점에 테스트 실패 여부를 즉시 확인 가능.
- **무료:** GitHub Actions의 무료 티어로 충분히 운영 가능.

### Negative (단점/리스크)
- **학습 곡선:** GitHub Actions YAML 문법 및 Docker 배포 플로우 학습 필요.
- **초기 설정 시간:** CI/CD 파이프라인 구축에 시간 투자 필요.
- **Secrets 관리:** AWS SSH Key 등 민감 정보를 GitHub Secrets에 안전하게 관리해야 함.
- **네트워크 의존성:** GitHub Actions와 AWS 간 네트워크 문제 시 배포 실패 가능.

## Alternatives (대안)
- **GitLab CI/CD:** GitLab Runner 설정이 유연하나, 이미 GitHub에서 프로젝트를 관리 중이므로 비효율적.
- **Jenkins:** 자체 서버에서 운영 가능하나, 초기 설정이 복잡하고 유지보수 비용이 높음.
- **CircleCI:** 성능은 좋으나 무료 티어 제약이 있고, GitHub Actions로 충분한 수준.
- **AWS CodePipeline:** AWS 네이티브 서비스이나, GitHub Actions보다 유연성이 떨어지고 비용이 발생함.