# OmniVim AI Pair-Programming Guidelines & Agent Memory

## 🎯 1. 프로젝트 목적 및 핵심 워크플로우

`omnivim`은 《Practical Vim, Second Edition》(Drew Neil 저)의 전수 123개 팁 + 모던 플러그인 11개 + 실무 시나리오 10개, 총 **144개의 자가완비형 실습 모듈**과 **크로스 IDE (JetBrains 5종+, VS Code, CLI Vim, Neovim) 단축키 일원화**를 제공하는 엔터프라이즈급 툴킷입니다.

### 사용자 프롬프트 대응 원칙 (Memory Trigger)

사용자가 **"어떻게 사용하지?", "어떻게 해야해?", "실습 순서 알려줘", "어떻게 실습해?"** 와 같이 사용법이나 워크플로우를 질문하면, [PRACTICE_GUIDE.md](PRACTICE_GUIDE.md)를 기반으로 다음 **실전 폐쇄 루프 사이클(Closed-Loop Cycle)**을 즉시 안내하세요:

1. **🔍 1단계: 실습 팁 검색 및 선택 (어디를 연습할까?)**
   - 터미널에서 `practice` (또는 `practice -i`) 실행 ➔ fzf 대화형 검색창 오픈
   - 실시간으로 렌더링되는 우측 창의 `README.md` (출처 도서 페이지, 학습 목표, 실습 미션, 권장 키스트로크) 확인
   - `Enter` 키로 실습 에디터 즉시 오픈 (특정 팁 직접 지정: `practice 1`, `practice 85`)
2. **💻 2단계: 선호하는 에디터 열기 (어떤 에디터로 열까?)**
   - 기본 CLI Vim: `practice <번호>`
   - Neovim: `practice <번호> --nvim`
   - Visual Studio Code: `practice <번호> --code`
   - JetBrains CLion: `practice <번호> --clion`
   - JetBrains PyCharm: `practice <번호> --pycharm`
   - JetBrains IntelliJ IDEA: `practice <번호> --idea`
3. **⌨️ 3단계: 직접 손으로 타이핑 훈련 (어떻게 코딩할까?)**
   - `README.md`에 명시된 목표 키스트로크를 의식하며 `practice.*` 파일 편집
   - 편집 완료 후 에디터 저장 (`:w`)
4. **⚡ 4단계: 0.1초 고속 자동 채점 (맞게 했나?)**
   - 터미널에서 `check <번호>` (또는 `./scripts/check.sh <번호>`) 실행
   - 🟢 `[ PASS ]`: 기준 정답과 100% 일치 판정 ➔ 다음 팁으로 이동
   - 🔴 `[ FAIL ]`: Unified Diff (기대 정답 vs 내 결과) 라인별 대조 후 에디터에서 보정
5. **🔄 5단계: 원본 복원 및 초기화 (다시 연습하고 싶을 때)**
   - `reset <번호>` (또는 `./scripts/reset.sh <번호>`): 개별 팁 0.1초 즉시 복구
   - `reset --all`: 144개 전체 실습 파일 일괄 복구
6. **🚀 3.5단계: JetBrains 실행 중 핫 리로드 (IDE 재부팅 금지)**
   - JetBrains IDEs(CLion, PyCharm, DataGrip 등)에서 단축키가 즉시 반영되지 않을 때는 IDE를 재시작하지 않고 에디터 일반 모드에서 `:source ~/.ideavimrc` 를 입력하도록 안내합니다.

---

## 🛠️ 2. 주요 스크립트 및 실행 파일 요약

| 경로 / 명령어 | 용도 및 기능 |
|:---|:---|
| **`practice`** (`scripts/practice.sh`) | 대화형 fzf TUI 실습 런처 (실시간 README 미리보기 지원) |
| **`check <번호>`** (`scripts/check.sh`) | 정답 파일과 실습 파일 간 0.1초 자동 채점 및 Unified Diff 분석 |
| **`reset <번호>`** (`scripts/reset.sh`) | `.original_*` 백업 파일로부터 원본 0.1초 무손실 복구 (`--all` 지원) |
| **`omnivim`** (`bin/omnivim-ai`) | AI 에이전트 CLI 래퍼 (`tip`, `solve`, `reset` 명령 지원) |
| **`./install.sh`** | JetBrains 20여 종, VS Code, Vim, Neovim 단축키 및 실습 원클릭 배포기 |
| **`./verify_all.sh`** | 전체 교차 IDE 환경 패리티 및 실습 디렉터리 요약 검증 스크립트 |
| **`scripts/audit_all.py`** | 81개 세부 항목에 대한 전수 정밀 무결성 검증 감사 엔진 |
| **`scripts/interactive_menu.py`** | fzf 및 bat/cat 기반 터미널 퍼지 검색 런처 코어 |
| **`scripts/generate_practice.py`** | 선언적 메타데이터 기반 144개 실습 디렉터리 멱등 일괄 생성기 |
