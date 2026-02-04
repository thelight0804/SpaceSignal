# 2026-02-04-Frontend Dockerfile 작성 및 컨테이너 실행

## Summary (회의 요약)
Frontend Dockerfile 작성을 완료하고, Docker 이미지 빌드 및 컨테이너 실행에 성공함. Backend와 Frontend 컨테이너 모두 실행하여 양방향 통신(헬스체크)까지 확인 완료. Docker 네트워크 개념(localhost, 127.0.0.1, 0.0.0.0)과 컨테이너 관리 명령어(run vs start)를 학습함.

## Key Decisions (주요 결정 사항)

### 레이어 캐싱 최적화 적용
- **내용:** 
  1. `COPY package.json .`, `COPY package-lock.json .` 먼저 추가
  2. `RUN npm install` 실행
  3. `COPY . .` 나중에
- **이유:** 
  - node_modules 설치 레이어를 캐시로 재사용 → 빌드 시간 단축
  - Backend의 requirements.txt 전략과 동일한 패턴

### vite.config.js 서버 설정 추가
  - 기본값(localhost)은 컨테이너 내부에서만 리스닝
  - `0.0.0.0`으로 바인딩해야 컨테이너 외부(호스트)에서 접근 가능
  - Backend의 `--host 0.0.0.0` 설정과 동일한 원리
  - Docker 환경에서 필수 설정

### 컨테이너 파일시스템 격리 이해
- **내용:** Backend와 Frontend 컨테이너 모두 `/app` 작업 디렉토리 사용
- **이유:** 
  - Backend와 Frontend의 작업 디렉토리를 `/app` 공용으로 사용하는 것으로 착각
  - 애초에 컨테이너가 다르니 서로의 `/app`은 다른 공간

## Blockers & Solutions (블로커 & 해결책)

### 문제 1: docker run vs docker start 혼동
- **현상:** 정지된 Backend 컨테이너 재시작 시 `docker run [컨테이너 ID]` 실행 → 오류 발생
- **원인:** 
  - `docker run`과 `docker start`의 차이 미숙지
- **해결:** 
  - `docker run`: **새 컨테이너** 생성 및 실행 (이미지명 필요)
  - `docker start`: **기존 컨테이너** 재시작 (컨테이너명/ID 필요)

### 문제 2: localhost와 0.0.0.0의 차이 이해
- **질문:** `host: '0.0.0.0'` 설정 후 브라우저에서 `http://0.0.0.0:5173` 접속 가능한가?
- **해결:** 
  - **서버 바인딩 주소:** 어떤 네트워크 인터페이스에서 리스닝할지 결정
    - `127.0.0.1` (localhost): 내부에서만 요청 받음
    - `0.0.0.0`: 모든 인터페이스에서 요청 받음 (외부 접근 허용)
  - **브라우저 접속 주소:** 항상 `localhost` 또는 `127.0.0.1` 사용
  - `0.0.0.0`은 실제 주소가 아님

## TIL (느낀 점)

### Docker 컨테이너 격리 개념
- 각 컨테이너는 완전히 독립적인 파일시스템
- Backend `/app`과 Frontend `/app`은 별개

### 네트워크 바인딩의 이해
- **바인딩 주소 (서버 설정):**
  - `127.0.0.1`: 집 안 인터폰 (내부만)
  - `0.0.0.0`: 집의 모든 문 (외부 접근 가능)
- **접속 주소 (브라우저):**
  - `localhost` 또는 `127.0.0.1`
  - `0.0.0.0`은 주소가 아니라 "모든 문"이라는 설정

### IPv4와 IPv6 병존
- `127.0.0.1` (IPv4) = `::1` (IPv6)
- `ping localhost` 결과: `::1`로 응답
- Windows가 IPv6를 우선 사용 중

## Action Items (다음 할 일)
- [ ] docker-compose.yml 작성 (Backend + Frontend 통합 관리)
- [ ] docker-compose로 전체 시스템 실행 테스트
- [ ] GitHub Issue #5 완료 및 PR 생성
