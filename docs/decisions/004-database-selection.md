# 4. Database Selection

**Status:** Accepted
**Date:** 2025-12-18

## Context (배경 및 문제점)
- SpaceSignal은 위성 메타데이터, 사용자 정보, 통신 로그 등 **관계형 데이터(Relational Data)**를 저장하고 조회해야 함.
- 위성-통신 로그 간의 관계를 표현하려면 JOIN, Foreign Key 등 SQL 기능이 필수적임.
- **AWS 관리형 서비스**를 경험하고 싶음.

## Decision (결정 사항)
데이터베이스로 **Amazon RDS for PostgreSQL**을 선정함.

1. **Amazon RDS (Relational Database Service):** AWS 관리형 데이터베이스 서비스로, 백업/패치/모니터링이 자동화됨.
2. **PostgreSQL 14+:** 오픈소스 RDBMS로, JSON 타입 지원 및 확장성이 우수함.
3. **Terraform IaC:** RDS 인스턴스를 Terraform으로 프로비저닝하여 인프라를 코드로 관리함.

## Consequences (결과 및 효과)
### Positive (장점)
- **운영 자동화:** 백업, 패치, 장애 복구(Failover)를 AWS가 자동으로 처리하여 운영 부담 감소.
- **확장성:** 트래픽 증가 시 콘솔에서 클릭 몇 번으로 스펙 업그레이드 가능.

### Negative (단점/리스크)
- **제어 제약:** OS 레벨 접근이 불가능하여 특수한 설정이 제한적임. (현 프로젝트에서는 문제없음)

## Alternatives (대안)
- **EC2에 PostgreSQL 직접 설치:** 비용은 절감되나, 백업/모니터링을 직접 구현해야 하며 AWS 관리형 서비스 경험을 어필하기 어려움.
- **Amazon Aurora (PostgreSQL 호환):** 고성능이지만 월 $50+ 비용으로 개인 프로젝트에는 과도함.
- **DynamoDB (NoSQL):** 서버리스로 편리하나, 관계형 데이터 모델링에 부적합하고 SQL 쿼리 불가.
