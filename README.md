# 🛰️ SpaceSignal (스페이스시그널)

**SpaceSignal**은 전 세계 위성의 실시간 위치와 지상국 통신 로그를 지도 위에서 직관적으로 탐색할 수 있는 웹 서비스입니다.

> **현재 상태:** Phase 1 개발 중 (위치 기반 위성 추적 & 배포)

## Project Goal
- **실시간 위성 추적:** 사용자의 현재 위치 상공을 지나가는 위성을 실시간으로 계산하여 시각화합니다.
- **통신 로그 분석:** 전 세계 지상국에서 수신된 위성 신호 데이터를 기반으로 통신 현황을 모니터링합니다.
- **지상국 시각화:** 전 세계 지상국의 관측 이력을 지도 기반으로 제공합니다.

## Tech Stack

### Backend
- **Language:** Python 3.13+
- **Framework:** FastAPI
- **Database:** PostgreSQL (Planned)

### Frontend
- **Framework:** Svelte (Vite)

### Infrastructure
- **Container:** Docker & Docker Compose
- **Cloud:** AWS

## 🗺️ Roadmap

### Phase 1: 위치 기반 위성 추적 & 배포 (Current)
- [ ] 사용자 위치 기반 위성 위치 API 개발
- [ ] TLE(궤도 데이터) 데이터 자동 동기화
- [ ] Svelte 기반의 지도 UI 구현
- [ ] Docker 컨테이너화 및 docker-compose 구성
- [ ] AWS EC2 배포 및 네트워크 설정

### Phase 2: 위성별 통신 로그 조회
- [ ] 위성 통신 로그 데이터베이스 설계
- [ ] 위성별 수신 로그 조회 API 개발
- [ ] 위성별 주파수 대역 시각화

### Phase 3: 지상국별 통신 로그 조회
- [ ] 전 세계 지상국 위치 및 관측 이력 조회 API 개발
- [ ] 국가/지역별 지상국 필터링 기능