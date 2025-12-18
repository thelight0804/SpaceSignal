# 5. Infrastructure as Code with Terraform

**Status:** Accepted
**Date:** 2025-12-18

## Context (배경 및 문제점)
- SpaceSignal은 AWS 환경(EC2, RDS, VPC 등)에 배포되며, 인프라 구성 요소가 복잡해질 수 있음.
- **클릭 기반 GUI 배포**는 재현성(Reproducibility)이 낮고, 변경 이력 추적이 어려움.
- DevOps 역량을 향상시키기 위해 IaC(Infrastructure as Code) 도입이 필요함.
- Terraform, CloudFormation, Pulumi 등 여러 IaC 도구 중 선택이 필요함.

## Decision (결정 사항)
인프라 관리 도구로 **Terraform**을 선정하고, 다음 전략을 따름:

1. **Terraform 사용:** AWS 리소스(EC2, RDS, VPC, Security Group 등)를 코드로 정의하고 버전 관리.
2. **학습 전략 - GUI 선행 학습 후 코드화:**
   - 처음에는 AWS 콘솔에서 직접 리소스를 생성하며 서비스 개념 이해.
   - 이후 동일한 구성을 Terraform 코드로 작성하여 IaC로 전환.
   - 이를 통해 AWS 서비스와 Terraform 문법을 동시에 학습.
3. **상태 관리 - 단계적 접근:**
   - **Phase 1 (초기):** 로컬 `terraform.tfstate` 파일로 시작 (학습 곡선 완화).
   - **Phase 2+ (협업/CI/CD):** S3 백엔드 + DynamoDB 락으로 마이그레이션 (동시성 제어 및 상태 공유).
   - 1인 프로젝트에서는 로컬 관리로 충분하며, 필요 시점에 전환하여 마이그레이션 경험 확보.
4. **모듈화:** 환경별(Dev/Prod) 분리 및 재사용 가능한 모듈 구조로 설계.

## Consequences (결과 및 효과)
### Positive (장점)
- **재현성:** 인프라를 코드로 관리하여 언제든 동일한 환경을 재생성 가능.
- **버전 관리:** Git으로 인프라 변경 이력 추적 및 롤백 가능.
- **협업:** 팀원 간 인프라 상태 공유 및 리뷰 가능.
- **멀티 클라우드 확장 가능:** Terraform은 AWS 외에도 GCP, Azure 등 다양한 프로바이더 지원.
- **학습 효율:** GUI로 AWS 서비스 개념을 먼저 익히고, 이를 코드로 변환하는 과정에서 IaC 이해도 향상.

### Negative (단점/리스크)
- **학습 곡선:** HCL(HashiCorp Configuration Language) 문법 학습 필요.
- **로컬 상태 관리 제약 (Phase 1):** 로컬 tfstate는 협업 불가 및 백업 부재 (Phase 2에서 S3로 해결).
- **초기 설정 시간:** GUI 대비 초기 코드 작성 시간이 더 소요됨 (장기적으로는 효율 증대).

## Alternatives (대안)
- **AWS CloudFormation:** AWS 네이티브 IaC 도구로 통합은 좋으나, JSON/YAML 문법이 복잡하고 AWS에만 종속됨.
- **Pulumi:** 익숙한 프로그래밍 언어(Python, TypeScript)로 작성 가능하나, Terraform 대비 커뮤니티가 작고 학습 자료가 부족함.
- **수동 관리(GUI):** 빠른 프로토타입에는 유리하나, 프로덕션 환경에서는 재현성과 협업 측면에서 불리함.