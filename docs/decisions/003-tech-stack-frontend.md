# 3. Frontend Tech Stack Selection

**Status:** Accepted
**Date:** 2025-12-14
**Last Updated:** 2025-12-15

## Context (배경 및 문제점)
- 수백/수천 개의 위성 마커를 지도 위에 실시간으로 렌더링해야 하므로, **DOM 조작 비용이 낮고 가벼운 프레임워크**가 필요함.
- React 경험이 있으나, 이번 프로젝트를 통해 **새로운 기술 스택에 도전**하고 기술적 시야를 넓히고자 함.
- 복잡한 상태 관리보다는 데이터 시각화 로직에 집중할 수 있는 직관적인 문법이 선호됨.

## Decision (결정 사항)
프론트엔드 핵심 기술로 **Svelte** (Build tool: Vite)를 선정함.

1. **Svelte:** 가상 돔(Virtual DOM) 없이 컴파일 타임에 최적화된 바닐라 JS를 생성하여 런타임 성능이 매우 우수함.
2. **Leaflet:** 지도 시각화를 위해 가볍고 확장성이 좋은 Leaflet 라이브러리를 채택.
3. **Challenge:** 익숙한 React 대신 Svelte를 선택함으로써, 새로운 패러다임을 학습하고 적응을 기대함.

## Consequences (결과 및 효과)
### Positive (장점)
- **성능(Performance):** 런타임 오버헤드가 적어 다량의 위성 마커를 지도에 표시할 때 버벅임이 덜함.
- **생산성:** 보일러플레이트 코드(useState, useEffect 등)가 적어 핵심 로직 구현에 집중할 수 있음.
- **학습 곡선:** HTML/CSS/JS 표준과 가까워 빠르게 배우고 적용할 수 있음.

### Negative (단점/리스크)
- **생태계:** React에 비해 라이브러리나 레퍼런스(참고 자료)가 부족할 수 있음.

## Alternatives (대안)
- **React:** 가장 익숙하고 생태계가 넓지만, 대량의 DOM 업데이트 시 최적화(Memoization 등) 노력이 더 필요할 수 있음.
