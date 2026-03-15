# 2026-03-08-copilot-instructions 개선 & EC2 SSH 접속 및 Docker 설치

## Summary (회의 요약)
CLAUDE.md 작성 요령을 조사하고 `copilot-instructions.md`를 개선함. 이후 EC2 인스턴스에 SSH로 첫 접속에 성공하고, Docker 공식 apt repository 방식으로 Docker를 설치함.

## Key Decisions (주요 결정 사항)

### Commands / Architecture 섹션 추가
- **내용:** 파일 상단부에 실행 명령어와 디렉토리 역할 설명 섹션을 추가함.
- **이유:** Boris Cherny(Claude Code 창시자)의 CLAUDE.md 철학에 따르면 "코드에서 추론 불가능한 정보"만 작성하는 것이 핵심. 명령어와 아키텍처는 AI가 코드만 봐서는 알 수 없는 대표적인 정보임.

### Karpathy 행동 원칙 통합 및 범위 한정
- **내용:** Andrej Karpathy의 4원칙(Think Before Coding / Simplicity First / Surgical Changes / Goal-Driven Execution)을 AI 가이드라인에 추가하되, "예외 조건으로 코드를 작성할 때만 적용"으로 범위를 명시적으로 한정함.
- **이유:** 이 프로젝트는 학습 중심 개발이므로 AI가 코드를 직접 작성하는 경우가 제한적. Karpathy 원칙이 항상 활성화되면 학습 가이드라인과 충돌할 수 있음.

### AI 가이드라인을 AI 직접 명령 언어로 재작성
- **내용:** 기존 "AI에게 요청 불가능한 것" 형식(사용자 가이드 언어)을 "사용자가 구현 요청 시 아래 순서를 따라라" 형식(AI 직접 지시 언어)으로 전환함.
- **이유:** AI는 자신에게 직접 말하는 명령에 더 일관되게 반응함. 사용자 언어로 쓰인 규칙은 AI가 자신의 행동 지침으로 해석하지 않을 수 있음.

### 응답 패턴 예시 및 예외 조건 명시
- **내용:** 구현 요청 / 에러 / 코드 리뷰 3가지 유형별 응답 예시와, 코드 직접 제시가 허용되는 4가지 예외 조건을 추가함.
- **이유:** 경계가 없으면 AI가 매번 다르게 판단함. 구체적인 예시와 예외 조건이 있어야 일관된 학습 보조 역할을 수행할 수 있음.

### GitHub Issue/PR 상세 템플릿 간소화
- **내용:** 본문에 인라인으로 포함되어 있던 상세 템플릿을 요약 규칙만 남기는 형식으로 간소화함.
- **이유:** 상세 템플릿은 이미 `.github/prompts/` 파일에 별도로 관리되고 있어 중복이었음. 중복 제거로 약 60줄 감소.

### Must Follow / Don't 섹션 추가
- **내용:** 코드 리뷰 섹션에 "Must Follow"와 "Don't" 항목을 명시적으로 분리하여 추가함.
- **이유:** 기존에는 필수/금지 사항이 파일 전체에 산재해 있어 AI가 우선순위를 파악하기 어려웠음.

## Blockers & Solutions (블로커 & 해결책)

### TIL 작성 방식 변경 — AI 질문 후 사용자 답변 기반 작성
- **내용:** `meeting-summary.md`의 TIL 섹션을 AI가 직접 작성하던 방식에서, AI가 세션 내용 기반 질문을 제시하고 사용자 답변을 받아 작성하는 방식으로 변경함. "TIL 질문 단계" 지침을 파일 하단에 별도 섹션으로 추가함.
- **이유:** AI가 작성한 TIL은 실제 느낀 점이 아닌 작업 요약에 가까워졌음. 사용자의 언어로 작성된 TIL이 미래의 나를 위한 기록에 더 부합함.

### 회의록 동일 날짜 파일 추가 방식 — 기존 섹션에 병합
- **내용:** 같은 날짜에 여러 세션이 있으면 별도 섹션(`---`)으로 분리하지 않고 기존 Summary/Key Decisions/Blockers/Action Items 섹션에 내용을 병합함.
- **이유:** 날짜 기준 파일 하나에 그날의 모든 작업이 응집되어야 일관성 있는 회의록이 됨.

- **문제:** Windows에서 SSH 접속 시 `.pem` 키 파일 권한 에러 발생
  ```
  WARNING: UNPROTECTED PRIVATE KEY FILE!
  Bad permissions. Try removing permissions for user: NT AUTHORITY\Authenticated Users
  ```
- **해결:** `icacls` 명령어로 권한 재설정
  1. 상속 제거: `icacls <키파일> /inheritance:r`
  2. Authenticated Users 제거: `icacls <키파일> /remove "NT AUTHORITY\Authenticated Users"`
  3. 현재 사용자에게만 읽기 권한 부여: `icacls <키파일> /grant "$($env:USERNAME):R"`

- **문제:** `sudo apt install docker-ce` 실행 시 `Package 'docker-ce' has no installation candidate` 에러
- **해결:** Docker GPG 키 및 apt 저장소를 먼저 등록한 뒤 재설치. 설치 전 저장소 등록 단계(`Set up Docker's apt repository`)가 선행되어야 함

## TIL (느낀 점)
- 역시.. PowerShell만의 독특한 명령어가 가끔은 불편할 때가 있다. Linux와 병합해줬으면 좋겠어ㅋㅋㅋ
- Linux 학습 때 배운 apt 저장소 개념을 실전에서 복습할 수 있어서 좋았다.

## Action Items (다음 할 일)
- [ ] EC2에 Docker Compose 설치
- [ ] EC2 서버 환경 설정 후 진행한 회의록을 한번에 커밋하기