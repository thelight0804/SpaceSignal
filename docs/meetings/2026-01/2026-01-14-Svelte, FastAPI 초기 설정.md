# 2026-01-14-Svelte 프론트엔드 초기 설정

## Summary (회의 요약)
Svelte + Vite를 이용한 프론트엔드 초기 설정을 완료하고, 템플릿 예제 파일들을 정리하여 커밋 준비를 마침. `feature/#2-fastapi-initial-setup` 브랜치에서 작업했으나, 참고 자료의 학습 흐름상 Svelte를 먼저 설치하기로 결정함.

## Key Decisions (주요 결정 사항)

### Svelte 설치 및 템플릿 정리
- **내용:** Svelte 5.43.8 + Vite 7.2.4 설치, Vite 템플릿의 예제 파일들(Counter.svelte, 로고 파일 등) 정리
- **이유:** 
  - SpaceSignal 프로젝트에 맞는 깨끗한 시작점 확보

### FastAPI 브랜치에서 Svelte 작업 진행
- **내용:** `feature/#2-fastapi-initial-setup` 브랜치에서 프론트엔드 코드 커밋
- **이유:** 
  - 참고 중인 책의 학습 흐름상 Svelte를 먼저 설치하는 순서
  - 별도 브랜치 생성보다는 현재 브랜치에서 통합 작업 진행

## Blockers & Solutions (블로커 & 해결책)
- **문제:** 브랜치 전략 관련 혼란 - FastAPI 브랜치에서 Svelte 작업을 해도 되는가?
- **해결:** 
  - 책의 학습 흐름에 따라 현재 브랜치에서 작업하기로 결정
  - 커밋 메시지에 `feat: Add Svelte frontend initial setup` 명시하여 명확히 함

## FastAPI 백엔드 동작 확인
- `backend/main.py`에 FastAPI 애플리케이션 및 `/hello` 엔드포인트 구현 완료
- uvicorn 서버 실행: `uvicorn main:app --reload`
- 브라우저에서 http://127.0.0.1:8000/docs 접속하여 Swagger UI 확인
- `/hello` 엔드포인트 테스트 성공: `{"message": "Hello SpaceSignal!"}` 응답 확인

## TIL (느낀 점)
- Git 워크플로우에서는 브랜치 목적과 작업 내용이 일치하는 것이 이상적이지만, 학습 과정에서는 유연하게 적용 가능

## Action Items (다음 할 일)
- [] Svelte 웹 페이지 만들기
