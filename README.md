# omnivim — 크로스 IDE 단축키 일원화 및 Practical Vim 144개 전수 실습 툴킷

[![OmniVim CI](https://github.com/coralstay/omnivim/actions/workflows/ci.yml/badge.svg)](https://github.com/coralstay/omnivim/actions/workflows/ci.yml)
[![License: AGPL-3.0-only](https://img.shields.io/badge/License-AGPL--3.0--only-blue.svg)](./LICENSE)
[![144 Tips](https://img.shields.io/badge/Tips-144%20Verified-brightgreen.svg)](PRACTICAL_VIM_MAP.md)
[![Cross-IDE Parity](https://img.shields.io/badge/Cross--IDE-JetBrains%20%7C%20VS%20Code%20%7C%20Vim-blue.svg)](configs/)

> *"AI가 코드를 쏟아내는 시대일수록, 에디터와 손가락이 하나 되어 생각의 속도로 타이핑하고(OmniVim) 0.1초 만에 검증하는 장인정신(Craftsmanship)이 진짜 차이를 만듭니다."*  
> *(참조 철학: 《Practical Vim, Second Edition》, Drew Neil)*
>
> 🚀 초심자를 위한 완벽 실습 가이드 (5단계 폐쇄 루프 사이클 & IDE 연동): [PRACTICE_GUIDE.md](PRACTICE_GUIDE.md)  
> 🏗️ 프로젝트 아키텍처 및 디렉터리 트리 상세 설계서: [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)  
> 🗺️ 144 팁 전체 색인 및 핵심 명령어 상세 레퍼런스: [PRACTICAL_VIM_MAP.md](PRACTICAL_VIM_MAP.md)  
> ⌨️ JetBrains & Vim 10대 실무 타이핑 집중 훈련 가이드: [JETBRAINS_VIM_KEYMAP_PRACTICE.md](JETBRAINS_VIM_KEYMAP_PRACTICE.md)  
> 🤖 AI 에이전트 인터페이스 (CLI·MCP·Computer Use): [AI_AGENT_INTERFACE.md](AI_AGENT_INTERFACE.md)

본 저장소는 Drew Neil의 전설적인 바이블 《Practical Vim, Second Edition》의 123개 전수 팁에 현대적 필수 플러그인 11개와 크로스 IDE 실무 시나리오 10개를 더한 총 22개 챕터, 144개의 방대한 실습 항목을 단 1개의 축약도 없이(Zero Abbreviation) 전수 수록한 엔터프라이즈급 타이핑 및 단축키 일원화 툴킷입니다.

각 실습 항목 폴더는 표준화된 자기완비형(Self-contained) 4-파일 구조로 설계되었습니다:
- `README.md`: 원서 출처 페이지, 핵심 개념, 실습 미션, 권장 키스트로크 해설
- `practice.*`: 학습자가 직접 에디터를 열고 손으로 키를 입력하며 실습하는 대상 소스 코드
- `expected_*`: 타이핑 완료 후 완벽히 도달해야 하는 기준 정답 파일
- `.original_*`: 초기화(`reset`) 실행 시 언제든 0.1초 만에 최초 원본 상태로 복구하는 원본 백업 파일

---

## 📊 전체 트랙 및 실습 규모 (총 22개 챕터, 144개 항목)

| 챕터 번호 | 챕터명 / 범주 | 소속 팁 번호 | 항목 수 | 핵심 개념 및 주요 훈련 내용 |
|:---|:---|:---:|:---:|:---|
| ch01 | The Vim Way (마침표 공식) | Tip 001 ~ 006 | 6개 | 마침표(.) 명령어, DRY 원칙, 오퍼레이터-모션 결합, 마침표 공식 |
| ch02 | Normal Mode (일반 모드) | Tip 007 ~ 012 | 6개 | 홈 행 정지, Undo 청크 분할, 반복 가능 변경 조합, 오퍼레이터+모션 |
| ch03 | Insert Mode (삽입 모드) | Tip 013 ~ 019 | 7개 | 즉시 백스페이스, `<C-o>` 정규 복귀, 수식 레지스터(`<C-r>=`), 문자 삽입 |
| ch04 | Visual Mode (비주얼 모드) | Tip 020 ~ 026 | 7개 | 선택 영역 재지정, 열 블록(`<C-v>`), 여러 행 동시 수정, 텍스트 치환 |
| ch05 | Command-Line Mode (명령행 모드) | Tip 027 ~ 034 | 8개 | Ex 명령어, 줄 범위(`:1,5`), `:copy`/`:move`, `:normal` 배치 실행 |
| ch06 | Manage Multiple Files (다중 파일 관리) | Tip 035 ~ 039 | 5개 | 버퍼 목록(`:ls`), 인자 목록(`:args`), 창 분할(`<C-w>s`, `<C-w>v`), 탭 관리 |
| ch07 | Open Files and Save (파일 열기 및 저장) | Tip 040 ~ 044 | 5개 | `:edit` 상대 경로 탐색, `find` 디렉터리 검색, `sudo tee` 권한 저장 |
| ch08 | Motions & Text Objects (모션 & 텍스트 오브젝트) | Tip 045 ~ 053 | 9개 | 단어 단위(`w`, `b`, `e`), 문자 찾기(`f`, `t`), 괄호/따옴표 텍스트 오브젝트(`i"`, `a)`) |
| ch09 | Navigate with Jumps (점프 리스트) | Tip 054 ~ 059 | 6개 | 점프 리스트(`<C-o>`, `<C-i>`), 변경 목록(`g;`, `g,`), 마크 지정(`m{a-z}`) |
| ch10 | Copy and Paste (복사 및 붙여넣기) | Tip 060 ~ 064 | 5개 | 무명 레지스터, 명칭 레지스터(`"a`), 시스템 클립보드(`"+`), 교체 붙여넣기 |
| ch11 | Macros (매크로) | Tip 065 ~ 072 | 8개 | 매크로 녹화(`q{a-z}`), 반복 실행(`@@`), 직렬/병렬 실행, 매크로 편집 |
| ch12 | Matching Patterns (정규표현식) | Tip 073 ~ 077 | 5개 | Very Magic(`\v`), 대소문자 무시(`\c`), 단어 경계(`\<`, `\>`), 하위 일치 |
| ch13 | Search (검색) | Tip 078 ~ 085 | 8개 | 현재 단어 검색(`*`, `#`), 검색 오프셋(`/s+1`), 검색 히스토리, 하이라이트 |
| ch14 | Substitution (치환) | Tip 086 ~ 096 | 11개 | 치환 명령(`:s`), 전역 플래그(`/g`), 확인 플래그(`/c`), 레지스터 연동 치환 |
| ch15 | Global Commands (전역 명령어) | Tip 097 ~ 100 | 4개 | `:global`, `:vglobal`, 특정 패턴 행 일괄 수집/삭제, 파이프라인 |
| ch16 | Index & Navigate with Ctags (태그 탐색) | Tip 101 ~ 105 | 5개 | 태그 생성, 정의 위치 점프(`<C-]>`), 태그 스택 복귀(`<C-t>`), 함수 추적 |
| ch17 | Quickfix List (퀵픽스 목록) | Tip 106 ~ 109 | 4개 | 컴파일 에러 순회(`:cnext`, `:cprev`), 퀵픽스 창, Location 리스트 |
| ch18 | Search Project-Wide with Grep (전역 검색) | Tip 110 ~ 112 | 3개 | 내장 `:vimgrep`, 외부 Ripgrep 연동, 검색 결과 퀵픽스 파이프라인 |
| ch19 | Autocompletion (자동완성) | Tip 113 ~ 119 | 7개 | 단어 자동완성(`<C-n>`), 행 자동완성(`<C-x><C-l>`), 파일명 완성, Omni 완성 |
| ch20 | Spell Checker (맞춤법 검사) | Tip 120 ~ 123 | 4개 | `:setlocal spell`, 오타 점프(`]s`), 추천 단어 교체(`z=`), 사전 추가(`zg`) |
| ch21 | Essential Modern Plugins (필수 모던 플러그인) | Tip 124 ~ 134 | 11개 | vim-surround, vim-commentary, argtextobj, textobj-entire, vim-exchange |
| ch22 | Cross-IDE Situational Keymap Drills (크로스 IDE 실전 훈련) | Tip 135 ~ 144 | 10개 | 탐색기-에디터 전환, 심볼 리팩터링, 단일 테스트 디버그, 터미널 분할 |
| 합계 | 22개 전 챕터 통합 커리큘럼 | Tip 001 ~ 144 | 144개 | 원서 순정 123개 + 플러그인 11개 + 실무 시나리오 10개 전수 완비 |

---

## ⚡ 초고속 실습 및 자동 채점 파이프라인 (Fast-path)

본 툴킷은 144개 실습 환경에서도 단 0.1초 만에 실행, 채점 및 복구가 가능하도록 고속 파이프라인을 지원합니다.

### 1. 원클릭 마스터 설치 (`./install.sh`)
저장소를 클론한 후 `./install.sh`를 실행하면 기존 설정을 자동으로 백업하고 JetBrains 전 제품군, VS Code, CLI Vim, Neovim에 단일화된 단축키와 실습 환경을 일괄 배포합니다.
```bash
./install.sh
```

### 2. 대화형 fzf TUI 검색 런처 (`practice` 또는 `practice -i`)
터미널에서 `practice`를 입력하면 `fzf` 기반 실시간 분할 창이 열립니다. 키워드로 검색하며 우측 분할 화면에서 각 팁의 `README.md` (학습 목표, 실습 미션, 권장 키스트로크)를 실시간으로 읽고 `Enter`를 눌러 즉시 실습을 시작할 수 있습니다.
```bash
# 대화형 TUI 검색 런처 실행 (터미널)
practice

# Neovim 모드로 TUI 런처 실행
practice -i --nvim
```

### 3. 선호하는 IDE / 에디터로 0.1초 즉시 오픈
특정 팁 번호와 에디터 옵션을 지정하여 원하는 개발 환경에서 바로 실습 파일을 열 수 있습니다:
```bash
practice 1           # 기본 CLI Vim으로 열기 (Tip 1: 마침표 공식)
practice 85          # CLI Vim으로 열기 (Tip 85: 단어 전방 검색)
practice 113 --nvim  # Neovim으로 열기 (Tip 113: 자동완성)
practice 124 --code  # VS Code로 열기 (Tip 124: vim-surround)
practice 135 --clion # CLion으로 열기 (Tip 135: 탐색기 포커스)
practice 12 --pycharm# PyCharm으로 열기 (Tip 12: 오퍼레이터 결합)
practice 87 --idea   # IntelliJ IDEA로 열기 (Tip 87: 치환 플래그)
```

### 4. 0.1초 고속 자동 채점기 (`check <번호>`)
타이핑을 마친 후 `check <번호>`를 실행하면, 기대 정답 파일(`expected_*`)과 내 실습 파일(`practice.*`)을 비교하여 0.1초 만에 합격 여부를 판정합니다.
```bash
check 1
```
* 🟢 `[ PASS ]` 통과: 기준 정답과 100% 일치 시 성공 메시지 출력
* 🔴 `[ FAIL ]` 오답: 기대값과 내 코드의 차이점을 Unified Diff 형식으로 색상 표시

### 5. 0.1초 원본 복원 도구 (`reset <번호>`)
연습 중 코드가 엉켰거나 다시 처음부터 훈련하고 싶을 때 숨김 백업본(`.original_*`)으로부터 즉시 원본을 복원합니다.
```bash
reset 1       # Tip 1 파일 원본 상태로 복원
reset --all   # 144개 전체 실습 파일 일괄 복원
```

### 6. JetBrains IDE 무재부팅 핫 리로드 (Hot Reload)
JetBrains IDE(CLion, PyCharm, DataGrip 등)가 이미 켜져 있는 상태에서 설정을 갱신하려면 IDE를 재시작하지 않고 에디터 일반 모드에서 다음 명령어를 입력합니다:
```vim
:source ~/.ideavimrc
```

---

## ⌨️ Cross-IDE (크로스 IDE) 통합 단축키 매트릭스

다음 단축키는 JetBrains IDEs (CLion, IntelliJ IDEA, PyCharm, DataGrip, WebStorm, GoLand, RustRover, DataSpell) 및 Visual Studio Code, CLI Vim/Neovim에서 동일하게 동작합니다.

### 5.1 Mnemonic Leader Key (니모닉 리더키) 체계 (`<Space>` 계열)

리더키 조합은 기능의 영문 첫 글자인 Mnemonic (니모닉 약어)을 기반으로 계층화되어 있습니다.

| 범주 | 단축키 | 기능 설명 | 네이티브 매핑 / Action ID |
|---|---|---|---|
| Explorer | `<Space>e` | 프로젝트 탐색기 열기 / 포커스 | `⌘1` (`ActivateProjectToolWindow`) |
| | `<Space>ee` | 탐색기 트리에서 현재 파일 위치 표시 | `⌥F1, 1` (`SelectInProjectView`) |
| | `<Space>ea` / `Esc` | 탐색기/도구창에서 에디터로 포커스 복귀 | `Escape` (`FocusEditor`) |
| Terminal / Tools | `<Space>t` | 내장 터미널 토글 | `⌥F12` (`ActivateTerminalToolWindow`) |
| | `<Space>or` | Run (실행) 콘솔 창 열기 | `⌘4` (`ActivateRunToolWindow`) |
| | `<Space>od` | Debug (디버그) 콘솔 창 열기 | `⌘5` (`ActivateDebugToolWindow`) |
| | `<Space>op` | Problems (문제/에러) 목록 창 열기 | `⌘6` (`ActivateProblemsViewToolWindow`) |
| | `<Space>os` | Structure (심볼 구조) 창 열기 | `⌘7` (`ActivateStructureToolWindow`) |
| Compile & Build | `<Space>cc` | 현재 활성 파일만 단일 컴파일 | `⌘⇧F9` (`CompileDirty`) |
| | `<Space>cp` | 프로젝트 전체 빌드 | `⌘F9` (`CompileProject`) |
| Run & Test | `<Space>rc` | 현재 커서 위치의 테스트/클래스 단일 실행 | `⌃⇧R` (`RunClass`) |
| | `<Space>dc` | 현재 커서 위치의 테스트/클래스 단일 디버깅 | `⌃⇧D` (`DebugClass`) |
| | `<Space>rr` | 직전 실행 설정 재실행 | `⌃R` (`Run`) |
| | `<Space>rs` | 실행 중인 프로세스 강제 중단 | `⌘F2` (`Stop`) |
| Code & Refactor| `<Space>cf` | Code Formatting (코드 자동 정렬) | `⌘⌥L` (`ReformatCode`) |
| | `<Space>cr` | Rename Refactoring (심볼 이름 변경) | `⇧F6` (`RenameElement`) |
| | `<Space>ca` | Quick Fix (빠른 수정 및 인텐션 액션) | `⌥Enter` (`ShowIntentionActions`) |
| | `<Space>co` | Optimize Imports (임포트 최적화) | `⌃⌥O` (`OptimizeImports`) |
| | `<Space>cs` | Structure Popup (파일 내 심볼 팝업) | `⌘F12` (`FileStructurePopup`) |
| Search & Files | `<Space>ff` | Go to File (파일명으로 검색) | `⌘P` / `⌘⇧O` (`GotoFile`) |
| | `<Space>fg` | Find in Path (프로젝트 전체 텍스트 검색) | `⌘⇧F` (`FindInPath`) |
| | `<Space>fr` | Recent Files (최근 열어본 파일) | `⌘E` (`RecentFiles`) |
| | `<Space>/` | Search Everywhere (어디서나 전체 검색) | `Shift + Shift` (`SearchEverywhere`) |
| Buffer & Tabs | `<Space>bd` | 현재 탭 / 버퍼 닫기 | `⌘W` (`CloseContent`) |
| | `<Space>bn` / `bp` | 다음 / 이전 탭 이동 | `NextTab` / `PreviousTab` |
| | `<Space>bo` | 다른 모든 탭 일괄 닫기 | `CloseAllEditorsButActive` |
| Splits | `<Space>sv` / `sh` | 창 세로 / 가로 분할 | `SplitVertically` / `SplitHorizontally` |
| | `<Space>sc` / `so` | 현재 분할 닫기 / 모든 분할 해제 | `Unsplit` / `UnsplitAll` |
| | `⌃h / ⌃j / ⌃k / ⌃l` | 분할 창 간 포커스 방향 이동 | `navigateLeft/Down/Up/Right` |

### 5.2 표준 Vim 키바인딩 및 플러그인 기능

IDE 단축키와의 충돌을 해제하고 Vim 고유 기능이 우선 동작하도록 보장된 조작 목록입니다.

| 단축키 | 기능 설명 | 비고 |
|---|---|---|
| `<C-a>` / `<C-x>` | 숫자 1 증가 / 감소 | IDE 전체선택 충돌 해제, Vim 고유 기능 위임 (`sethandler`) |
| `<C-r>` | Redo (재실행) | IDE 검색/치환 충돌 해제, Vim Redo 기능 보장 |
| `<C-v>` | Visual Block (세로 열 블록 선택) | IDE 붙여넣기 충돌 해제, Vim 블록 선택 보장 |
| `[d` / `]d` | 이전 / 다음 에러 및 경고 점프 | Diagnostics Navigation (진단 라인 순회) |
| `[c` / `]c` | 이전 / 다음 Git 변경점 점프 | VCS Change Markers (형상 관리 변경점 순회) |
| `K` / `gh` | 키워드 문서 / 호버 정보 팝업 | Quick Documentation (도움말 조회) |
| `gd` / `gi` / `gr` | 정의 / 구현체 / 모든 참조 위치 점프 | Code Navigation (심볼 탐색) |
| `cs"'` / `ds"` / `ysiw]` | 괄호 및 따옴표 감싸기 / 변경 / 삭제 | `vim-surround` (Tip 124) |
| `gcc` / `gc{motion}` | 줄 단위 / 블록 단위 주석 토글 | `vim-commentary` (Tip 126) |
| `griw` | 레지스터 내용으로 현재 단어 교체 | `replaceWithRegister` (Tip 130) |
| `cxiw` | 두 단어의 위치 상호 맞교환 | `vim-exchange` (Tip 131) |

---

## 🛠️ 스크립트 도구 모음

| 스크립트 / 바이너리 | 용도 및 기능 |
|:---|:---|
| `practice` (`bin/practice`, `scripts/practice.sh`) | 대화형 fzf TUI 실습 런처 (실시간 README 미리보기 지원) |
| `check <번호>` (`bin/check`, `scripts/check.sh`) | 정답 파일과 실습 파일 간 0.1초 자동 채점 및 Unified Diff 분석 |
| `reset <번호>` (`bin/reset`, `scripts/reset.sh`) | 원본 백업본(`.original_*`)으로부터 실습 파일 0.1초 무손실 복구 (`--all` 지원) |
| `omnivim` (`bin/omnivim`, `bin/omnivim-ai`) | AI 에이전트 CLI 메인 실행기 (`tip`, `solve`, `reset` 명령 지원) |
| `install.sh` | 전 IDE 단축키, 플러그인, 코어 설정 및 실습 144개 원클릭 일괄 배포기 |
| `verify_all.sh` | 전체 교차 IDE 환경 패리티 및 실습 디렉터리 요약 검증 스크립트 |
| `scripts/audit_all.py` | 81개 세부 항목에 대한 전수 정밀 무결성 검증 감사 엔진 |
| `scripts/interactive_menu.py` | fzf 및 bat/cat 기반 터미널 퍼지 검색 런처 코어 |
| `scripts/generate_practice.py` | 선언적 메타데이터 기반 144개 실습 디렉터리 멱등 일괄 생성기 |
| `scripts/omnivim_ai.py` | 헤드리스 Neovim 자율 제어 및 JSON 인터페이스 코어 |
| `scripts/mcp_server.py` | Anthropic Model Context Protocol (MCP) 표준 stdio 서버 |
| `scripts/computer_use.py` | macOS GUI 단축키 주입 자동화 브리지 |

---

## 🤖 AI Agent (AI 에이전트) 인터페이스

인간 개발자뿐만 아니라 LLM 및 시각 기반 AI Agent (Claude Desktop, Cursor, OpenAI Operator, Anthropic Computer Use 등)가 OmniVim 환경을 프로그램 방식으로 조작할 수 있도록 3가지 연동 모드를 지원합니다:

1. CLI Interface (CLI 인터페이스) (`omnivim` / `bin/omnivim-ai`):
   - 100% JSON 입출력을 지원하여 터미널 에이전트가 144개 팁의 정보를 조회하고, 헤드리스 Neovim 엔진을 통해 임의의 파일에 Vim 키스트로크를 직접 주입할 수 있습니다.
2. Anthropic MCP Server (MCP 표준 서버) (`scripts/mcp_server.py`):
   - Claude Desktop 또는 Cursor의 MCP 설정에 추가하여 Tool Calling (도구 호출) 방식으로 실습 풀이, 코드 채점, 파일 편집을 수행합니다.
3. Computer Use GUI Bridge (Computer Use GUI 브리지) (`omnivim gui <action>`):
   - 화면 인식 에이전트가 작은 IDE 메뉴 버튼의 좌표를 추정하여 마우스로 클릭할 필요 없이, `compile`, `run-test`, `focus-editor` 등의 액션 명령어로 OS 레벨 단축키를 활성 IDE 창에 즉시 주입합니다.

세부 연동 방법 및 설정 예시는 [AI 에이전트 인터페이스 명세서](AI_AGENT_INTERFACE.md)를 참조하시기 바랍니다.

---

## 📖 라이선스 및 저작권 안내

본 프로젝트에서 직접 작성한 코드와 문서(스캐폴딩 생성기, 실행 도구, 색인 엔진, 설정 템플릿, 실습 스캐폴드)는 [GNU AGPL-3.0-only](./LICENSE)를 따릅니다(2026-10-31 MIT에서 변경).

실습의 원문 개념과 팁 출처는 Drew Neil 저 《Practical Vim, Second Edition》(The Pragmatic Bookshelf)입니다. 도서의 공식 예제 코드(`official_sources/`), 팁 목록·페이지 데이터(`scripts/data/all_tips.py`, `PRACTICAL_VIM_MAP.md`), 그리고 공식 예제와 같은 내용의 실습 파일은 저작권자 소유이므로 이 저장소에 포함하지 않습니다. 공식 예제는 출판사 사이트에서 직접 받으세요.
