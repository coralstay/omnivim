---
title: PRACTICAL_VIM_MAP
description: 크로스 에디터 단축키 명세와 팁 1~144 색인(팁 제목과 직접 쓴 한국어 요약)을 모은 OmniVim 명령어 지도
authors: [coralstay]
license: AGPL-3.0-only
status: draft
created_date: '2026-11-12'
updated_date: '2026-11-12'
---
# 🗺️ OmniVim 144 Tips & Comprehensive Command Map

> **Quick Links**: [🏠 README (홈)](README.md) • [🚀 Practice Guide (실습 가이드)](PRACTICE_GUIDE.md) • [🏗️ Architecture (아키텍처 설계서)](PROJECT_STRUCTURE.md) • [⌨️ Hands-On Practice (단축키 실전 훈련)](JETBRAINS_VIM_KEYMAP_PRACTICE.md) • [🗺️ 144 Tips Map (144 팁 색인)](PRACTICAL_VIM_MAP.md) • [🤖 AI Agent Interface (AI 에이전트 인터페이스)](AI_AGENT_INTERFACE.md)

---

> 본 문서는 Drew Neil 저 《Practical Vim (Second Edition)》의 전 20개 챕터 123가지 순정 실전 테크닉과 21장 모던 IDE 필수 플러그인 11선, 22장 크로스 IDE 10대 실무 상황별 집중 훈련(총 144개) 전체 및 JetBrains 전 제품군, VS Code, CLI 환경을 아우르는 OmniVim 통합 단축키 체계를 집대성한 종합 색인표입니다.

---

## 1. Cross-Editor (크로스 에디터) 통합 단축키 명세

### 1.1 표준 Vim 네비게이션 및 편집 (전 에디터 공통)
| 단축키 | 기능 명칭 | 세부 동작 및 IDE 위임 원리 |
|---|---|---|
| `<C-a>` / `<C-x>` | 숫자 1 증가 / 감소 | IDE 전체 선택 단축키 충돌을 해제하고 Vim 고유 기능으로 위임 (`sethandler`) |
| `<C-r>` | Redo (재실행) | IDE 검색/치환 충돌을 방지하고 Vim Redo 기능 보장 |
| `<C-v>` | Visual Block (세로 열 블록 선택) | IDE 붙여넣기 충돌을 해제하고 Vim 직사각형 열 선택 모드 진입 |
| `<C-o>` / `<C-i>` | Jump List (점프 리스트) 이전 / 이후 이동 | Jump List 히스토리를 순회하여 이전/다음 편집 지점으로 이동 |
| `<C-w>` prefix | 창 분할 및 이동 조작 | `<C-w>v`, `<C-w>s`, `<C-w>h/j/k/l`, `<C-w>c`, `<C-w>o` 분할 제어 |
| `<C-d>` / `<C-u>` | 반 페이지 스크롤 다운 / 업 | 커서 중앙 정렬 유지 (`zz`) 스크롤 |
| `K` / `gh` | Quick Documentation (도움말 조회) | IDE Quick Documentation (`ShowErrorDescription` / `QuickJavaDoc`) 호출 |
| `gd` / `gD` | 심볼 정의 / 타입 선언 점프 | `GotoDeclaration` / `GotoTypeDeclaration` 네이티브 액션 실행 |
| `gi` / `gr` | 구현체 / 모든 참조 위치 찾기 | `GotoImplementation` / `FindUsages` 네이티브 액션 실행 |
| `[d` / `]d` | Diagnostics Navigation (진단 라인 순회) | 파일 내 정적 분석 진단 라인 순회 |
| `[c` / `]c` | VCS Change Marker (변경점 마커 순회) | Hunk (버전 관리 변경점) 단위 순회 |
| `[m` / `]m` | Method Navigation (메서드 탐색) | 함수 선언부 단위 순회 |
| `za` / `zR` / `zM` | Code Folding (코드 접기 제어) | 코드 접기 토글 / 전체 펼치기 / 전체 접기 |
| `gf` / `gx` | 커서 아래 파일 열기 / 외부 링크 브라우저 열기 | Go to file / Open URL in browser |

### 1.2 Mnemonic Leader Key (니모닉 리더키) 체계 (`<Space>` 리더키)
| 범주 | 단축키 | 기능 명칭 | JetBrains / VS Code 네이티브 매핑 |
|---|---|---|---|
| **[e] Explorer** | `<Space>e` | 프로젝트 탐색기 창 열기 / 포커스 | `⌘1` (`ActivateProjectToolWindow`) |
| | `<Space>ee` | Scroll from Source (현재 파일 위치 전개) | `⌥F1, 1` (`SelectInProjectView`) |
| | `<Space>ea` / `Esc` | 에디터 작업 위치로 즉시 포커스 복귀 | `Escape` (`FocusEditor`) |
| **[t] Terminal** | `<Space>t` | 내장 터미널 도구창 토글 | `⌥F12` (`ActivateTerminalToolWindow`) |
| **[o] Tool Windows** | `<Space>or` | Run (실행) 콘솔 창 열기 | `⌘4` (`ActivateRunToolWindow`) |
| | `<Space>od` | Debug (디버그) 콘솔 창 열기 | `⌘5` (`ActivateDebugToolWindow`) |
| | `<Space>op` | Problems (문제 진단) 목록 창 열기 | `⌘6` (`ActivateProblemsViewToolWindow`) |
| | `<Space>os` | Structure (파일 심볼 구조) 창 열기 | `⌘7` (`ActivateStructureToolWindow`) |
| **[c] Compile & Code** | `<Space>cc` | **현재 활성 파일만 단일 컴파일** | `⌘⇧F9` (`CompileDirty`) |
| | `<Space>cp` | 프로젝트 전체 빌드 | `⌘F9` (`CompileProject`) |
| | `<Space>cf` | Code Formatting (코드 자동 정렬) | `⌘⌥L` (`ReformatCode`) |
| | `<Space>cr` | Rename Refactoring (심볼 이름 변경) | `⇧F6` (`RenameElement`) |
| | `<Space>ca` | Quick Fix (빠른 수정 및 인텐션) | `⌥Enter` (`ShowIntentionActions`) |
| | `<Space>co` | Optimize Imports (임포트문 최적화) | `⌃⌥O` (`OptimizeImports`) |
| | `<Space>cs` | Structure Popup (파일 내 심볼 팝업) | `⌘F12` (`FileStructurePopup`) |
| **[r] Run & Test** | `<Space>rc` | **현재 파일/테스트 메서드 단일 실행** | `⌃⇧R` (`RunClass`) |
| | `<Space>dc` | **현재 파일/테스트 단일 디버깅** | `⌃⇧D` (`DebugClass`) |
| | `<Space>rr` | 직전 실행 설정 재실행 | `⌃R` (`Run`) |
| | `<Space>rd` | 직전 디버그 설정 재실행 | `⌃D` (`Debug`) |
| | `<Space>rs` | 실행 프로세스 강제 중단 | `⌘F2` (`Stop`) |
| **[f] Find & Files** | `<Space>ff` | Go to File (파일명으로 검색) | `⌘P` / `⌘⇧O` (`GotoFile`) |
| | `<Space>fg` | Find in Path (프로젝트 텍스트 검색) | `⌘⇧F` (`FindInPath`) |
| | `<Space>fr` | Recent Files (최근 열어본 파일) | `⌘E` (`RecentFiles`) |
| | `<Space>fb` | Recent Changed (최근 변경된 파일) | `RecentChangedFiles` |
| | `<Space>/` | Search Everywhere (어디서나 검색) | `Shift + Shift` (`SearchEverywhere`) |
| **[b] Buffer & Tabs** | `<Space>bd` | 현재 활성 탭 / 버퍼 닫기 | `⌘W` (`CloseContent`) |
| | `<Space>bn` / `bp` | 다음 / 이전 에디터 탭 이동 | `NextTab` / `PreviousTab` |
| | `<Space>bo` | 다른 모든 탭 일괄 닫기 | `CloseAllEditorsButActive` |
| **[s] Splits** | `<Space>sv` / `sh` | 창 세로 / 가로 분할 | `SplitVertically` / `SplitHorizontally` |
| | `<Space>sc` / `so` | 현재 분할 창 닫기 / 모든 분할 해제 | `Unsplit` / `UnsplitAll` |
| | `⌃h / ⌃j / ⌃k / ⌃l` | 분할 창 간 포커스 방향 이동 | `navigateLeft/Down/Up/Right` |
| **[g] Git** | `<Space>gg` | Git 버전 관리 도구창 열기 | `⌘9` (`ActivateVersionControlToolWindow`) |
| | `<Space>gb` | Git Annotate (블레임 라인 주석 토글) | `Annotate` |
| | `<Space>gd` | 변경점 Diff 비교 창 열기 | `Compare.SameVersion` |
| **기타 유틸리티** | `<Space>h` | 검색 결과 하이라이트 일시 해제 | `:nohlsearch` |

---

## 2. Complete Catalog: OmniVim 144개 실습 전체 색인

### Chapter 1: The Vim Way (Tip 1 ~ 6)
- **Tip 1**: Meet the . Command (마침표 명령어를 통한 직전 편집 작업 재실행)
- **Tip 2**: Don't Repeat Yourself (A; 로 이동과 삽입 동작을 원자적으로 결합)
- **Tip 3**: Take One Step Back, Then Go Forward (s 또는 cw 로 편집 후 마침표 공식 적용)
- **Tip 4**: Act, Pause, Repeat (실행, 확인, 반복의 리듬을 통한 조작 최적화)
- **Tip 5**: Find and Replace by Hand (* 검색 후 cw + n + . 수동 치환 패턴)
- **Tip 6**: Meet the . Formula (1회 이동과 1회 변경을 결합하는 마침표 공식)

### Chapter 2: Normal Mode (Tip 7 ~ 12)
- **Tip 7**: Pause with Your Fingers on the Home Row (작업 종료 즉시 기본 노멀 모드로 복귀)
- **Tip 8**: Chunk Your Undos (실행 취소 단위를 고려한 삽입 모드 진입 및 탈출)
- **Tip 9**: Compose Repeatable Changes (daw, caw 로 반복성 있는 변경 조작 구성)
- **Tip 10**: Use Counts to Multiply Change (3dw, 5j 등 반복 카운트 곱하기 적용)
- **Tip 11**: Don't Count If You Can Repeat (카운트 계산 대신 마침표 명령어로 반복 적용)
- **Tip 12**: Combine Operators with Motions (오퍼레이터와 모션의 결합을 통한 작업 구성)

### Chapter 3: Insert Mode (Tip 13 ~ 19)
- **Tip 13**: Make Corrections Instantly from Insert Mode (<C-h>, <C-w>, <C-u> 기반 즉각 오타 교정)
- **Tip 14**: Get Back to Normal Mode (<C-o>로 단일 노멀 명령 실행 후 삽입 모드 유지)
- **Tip 15**: Paste from a Register Without Leaving Insert Mode (<C-r>{reg} 즉시 붙여넣기)
- **Tip 16**: Do Back-of-the-Envelope Calculations (<C-r>= 표현식 레지스터 산술 연산 입력)
- **Tip 17**: Insert Unusual Characters by Character Code (<C-v>u{hex} 유니코드 직접 입력)
- **Tip 18**: Insert Unusual Characters by Digraph (<C-k>{c1}{c2} 다이그래프 특수기호 입력)
- **Tip 19**: Overwrite Existing Text with Replace Mode (R 키로 기존 문자 덮어쓰기 모드 진입)

### Chapter 4: Visual Mode (Tip 20 ~ 26)
- **Tip 20**: Grok Visual Mode (v, V, <C-v> 3가지 Visual Mode 선택)
- **Tip 21**: Define a Visual Selection with o (o 키로 선택 영역의 시작점과 끝점 전환)
- **Tip 22**: Repeat Multi-Line Changes (V 로 다중 행 선택 후 들여쓰기 반복 적용)
- **Tip 23**: Prefer Operators over Visual Operations (모드 전환 비용을 줄이는 오퍼레이터 우선 원칙)
- **Tip 24**: Edit Tabular Data with Visual-Block Mode (<C-v> Visual Block 열 I/A 일괄 삽입)
- **Tip 25**: Change Columns of Text with c (<C-v> Visual Block 열 c 일괄 교체)
- **Tip 26**: Append After a Ragged Right Visual Block (<C-v>$A; 비정형 블록 일괄 후방 추가)

### Chapter 5: Command-Line Mode (Tip 27 ~ 34)
- **Tip 27**: Meet Vim's Command Line (: Ex 명령행 인터페이스 기초)
- **Tip 28**: Execute on Consecutive Lines (:1,5d 등 범위 지정 일괄 조작)
- **Tip 29**: Duplicate or Move Lines with :t and :m (:t 복사, :m 행 이동 조작)
- **Tip 30**: Run Commands on a Range with :normal (:'<,'>normal 기반 시각 영역 일괄 실행)
- **Tip 31**: Repeat the Previous Ex Command with @: (@: 키로 직전 Ex 명령 재실행)
- **Tip 32**: Autocomplete Ex Commands with Tab (명령어 및 파일 경로 자동완성)
- **Tip 33**: Compose at the Command Line with q: (q: 명령행 전용 윈도우 편집)
- **Tip 34**: Run Shell Commands with :! (:! 외부 시스템 셸 명령 연동)

### Chapter 6: Manage Multiple Files (Tip 35 ~ 39)
- **Tip 35**: Track Open Files with Buffer List (:ls, :bnext, :bdelete 버퍼 라이프사이클)
- **Tip 36**: Group Buffers with Argument List (:args, :argdo 인수 목록 기반 일괄 작업)
- **Tip 37**: Manage Hidden Buffers (:set hidden 설정 기반 미저장 버퍼 안전 전환)
- **Tip 38**: Divide Workspace into Split Windows (:vsplit, :split 화면 분할 관리)
- **Tip 39**: Organize Window Layouts with Tab Pages (:tabnew, gt, gT 탭 페이지 레이아웃)

### Chapter 7: Open Files and Save Them to Disk (Tip 40 ~ 44)
- **Tip 40**: Open a File by Its Filepath with :edit (:edit 기반 파일 열기)
- **Tip 41**: Open a File by Filename Using :find (:find 경로 자동 탐색 오픈)
- **Tip 42**: Open Files with File Explorer (Netrw 및 프로젝트 탐색기 연동)
- **Tip 43**: Save Files to Nonexistent Directories (존재하지 않는 디렉터리 경로 자동 생성 저장)
- **Tip 44**: Save a File as the Super User (:w !sudo tee % 관리자 권한 파일 저장)

### Chapter 8: Navigate Inside Files with Motions (Tip 45 ~ 53)
- **Tip 45**: Keep Your Fingers on the Home Row (홈 로우 h, j, k, l 기본 이동)
- **Tip 46**: Distinguish Actual Lines and Screen Lines (실제 행과 줄바꿈 화면 행 구별: gj, gk)
- **Tip 47**: Move Word by Word with w, b, e, ge (단어 단위 정방향/역방향 탐색)
- **Tip 48**: Traverse Characters with f and t (f, t 문자를 지정한 인라인 점프)
- **Tip 49**: Search for Character with t or f (dt, ct 등 오퍼레이터 결합 삭제/치환)
- **Tip 50**: Trace Selection with Text Objects (iw, aw, i", it Text Objects 선택)
- **Tip 51**: Delete Around or Inside with di and da (경계자 내부 및 전체 삭제)
- **Tip 52**: Mark Your Place and Return with Marks (ma, `a 북마크 설정 및 복귀)
- **Tip 53**: Jump Between Matching Parentheses with % (짝이 맞는 괄호 간 상호 점프)

### Chapter 9: Navigate Between Files with Jumps (Tip 54 ~ 59)
- **Tip 54**: Traverse the Change List with g; and g, (변경 목록 순회 이동)
- **Tip 55**: Jump to the Previous Location with '' (직전 점프 위치 복귀)
- **Tip 56**: Track Jumps with Jump List (<C-o>, <C-i> Jump List 탐색)
- **Tip 57**: Browse History of Changes (:changes 변경 이력 조회)
- **Tip 58**: Traverse Changes with Undo Tree (g-, g+ Undo Tree 탐색)
- **Tip 59**: Navigate to Files Named Inside with gf (텍스트 내 파일 경로 즉시 열기)

### Chapter 10: Copy and Paste (Tip 60 ~ 64)
- **Tip 60**: Delete, Yank, and Put with Unnamed Register ("" Unnamed Register 기본 동작)
- **Tip 61**: Grok Vim's Registers ("0 복사 전용 레지스터 활용)
- **Tip 62**: Replace Visual Selection with Register (선택 영역을 레지스터 내용으로 대체)
- **Tip 63**: Paste from a Register with "_ Black Hole ("_ Black Hole Register 오염 방지)
- **Tip 64**: Interact with the System Clipboard ("+ 시스템 클립보드 상호 연동)

### Chapter 11: Macros (Tip 65 ~ 72)
- **Tip 65**: Record and Execute a Macro (qa, q, @a, @@ 매크로 녹화 및 재생)
- **Tip 66**: Normalize, Strike, Abort in Macros (0 정규화를 통한 매크로 실패 방지)
- **Tip 67**: Play Back with a Count (10@a 카운트 기반 매크로 다중 실행)
- **Tip 68**: Repeat Macro Across Multiple Lines (:normal @a 다중 행 일괄 매크로 적용)
- **Tip 69**: Append Commands to a Macro with qA (대문자 레지스터 추가 녹화)
- **Tip 70**: Act Upon a Collection of Files (:argdo normal @a 전역 파일 매크로 일괄 실행)
- **Tip 71**: Evaluate an Iterator in a Macro (<C-a> 카운터 변수 증가 매크로)
- **Tip 72**: Edit the Contents of a Macro from Register ("ap 매크로 내용 텍스트 수정)

### Chapter 12: Matching Patterns and Searching (Tip 73 ~ 77)
- **Tip 73**: Tune Case Sensitivity with \c and \C (대소문자 구분 스위치)
- **Tip 74**: Use the \v Pattern Switch for Regexes (Very Magic 모드로 정규식 이스케이프 간소화)
- **Tip 75**: Use the \V Switch for Verbatim Search (Very Nomagic 리터럴 문자열 정밀 검색)
- **Tip 76**: Use Parentheses to Capture Submatches (\1, \2 캡처 그룹 활용)
- **Tip 77**: Define Boundaries of a Match with \zs and \ze (일치 영역의 시작/종료 경계 지정)

### Chapter 13: Search (Tip 78 ~ 85)
- **Tip 78**: Meet the Search Command (/, ?, n, N 정방향/역방향 검색)
- **Tip 79**: Highlight Search Matches with hlsearch (검색 결과 시각적 하이라이트)
- **Tip 80**: Preview First Match with incsearch (입력과 동시 점진적 검색 미리보기)
- **Tip 81**: Offset Cursor to End of Match with /e (검색어 종료 위치로 커서 오프셋 이동)
- **Tip 82**: Operate on Complete Search Match with gn (검색 일치 텍스트 단위 오퍼레이터 조작)
- **Tip 83**: Create Complex Patterns Iteratively with q/ (검색 히스토리 윈도우 편집)
- **Tip 84**: Count Matches for Current Pattern with :%s///gn (패턴 일치 개수 무변형 카운트)
- **Tip 85**: Find Every Occurrence with * and # (커서 위치 단어 전방/후방 즉시 검색)

### Chapter 14: Substitution (Tip 86 ~ 96)
- **Tip 86**: Meet the Substitute Command (:s/target/repl/flags 치환 기본 구문)
- **Tip 87**: Find and Replace Every Match in a File (:%s/old/new/g 파일 전역 일괄 치환)
- **Tip 88**: Eyeball Each Substitution with the /c Flag (/c 플래그를 통한 단계별 확인 치환)
- **Tip 89**: Reuse the Last Search Pattern (:%s//repl/g 직전 검색어 자동 재사용)
- **Tip 90**: Generate Replacement Expression with \= (\= 표현식 기반 동적 치환)
- **Tip 91**: Replace with Contents of Register (\\=@0 레지스터 내용으로 치환 문자열 구성)
- **Tip 92**: Repeat Previous Substitute with :& (:& 직전 치환 명령 동일 반복)
- **Tip 93**: Rearrange CSV Fields Using Submatches (정규식 캡처 그룹을 이용한 필드 순서 재배열)
- **Tip 94**: Perform Arithmetic on Replacement (\\=submatch(1)+1 산술 연산 적용 치환)
- **Tip 95**: Swap Two or More Words (임시 토큰을 활용한 2개 이상 식별자 교차 치환)
- **Tip 96**: Find and Replace Across Multiple Files (:argdo %s/old/new/ge 다중 파일 일괄 치환)

### Chapter 15: Global Commands (Tip 97 ~ 100)
- **Tip 97**: Meet the Global Command (:g/pat/[cmd] 조건부 일괄 실행 구문)
- **Tip 98**: Delete Lines Containing a Pattern with :g/pat/d (패턴 일치 라인 일괄 삭제)
- **Tip 99**: Collect TODO Items to a Register (:g/TODO/y A 일치 라인 레지스터 수집)
- **Tip 100**: Alphabetize Properties of Each CSS Rule (:g/{/ .+1,/}-1 sort 블록 단위 정렬)

### Chapter 16: Index and Navigate with Ctags (Tip 101 ~ 105)
- **Tip 101**: Meet Ctags (코드 심볼 색인 도구 개요)
- **Tip 102**: Configure Vim to Work with Ctags (:set tags 인덱스 파일 연동)
- **Tip 103**: Navigate Keyword Definitions with <C-]> and <C-t> (태그 기반 정의 탐색 및 복귀)
- **Tip 104**: Automatically Index with Ctags on Save (저장 시점 태그 자동 인덱싱 구성)
- **Tip 105**: Navigate Code Structure with Tagbar (심볼 계층 아웃라인 트리 탐색)

### Chapter 17: Compile Code and Navigate Errors (Tip 106 ~ 109)
- **Tip 106**: Compile Code Without Leaving Vim with :make (:make 기반 인에디터 빌드)
- **Tip 107**: Browse Quickfix List with :cnext and :cprev (Quickfix List 에러 목록 순회)
- **Tip 108**: Recall Results with :colder and :cnewer (Quickfix 빌드 결과 히스토리 탐색)
- **Tip 109**: Customize External Compiler with makeprg (컴파일러 호출 도구 커스터마이징)

### Chapter 18: Search Project-Wide with Grep (Tip 110 ~ 112)
- **Tip 110**: Search Entire Project with :grep (:grep 외부 텍스트 검색 도구 연동)
- **Tip 111**: Customize the :grep Program with ripgrep (ripgrep 고속 검색 엔진 연동)
- **Tip 112**: Grep with Vim's Internal Search Engine with :vimgrep (Vim 내부 정규식 엔진 검색)

### Chapter 19: Dial X for Autocompletion (Tip 113 ~ 119)
- **Tip 113**: Meet Vim's Keyword Autocompletion (<C-n>, <C-p> 키워드 자동완성)
- **Tip 114**: Work with the Autocomplete Pop-Up Menu (<C-n>, <C-p>, <C-y> 팝업 메뉴 조작)
- **Tip 115**: Understand the Source of Keywords ('complete' 옵션 소스 탐색 범위 제어)
- **Tip 116**: Autocomplete Words from the Dictionary (<C-x><C-k> 시스템 사전 단어 완성)
- **Tip 117**: Autocomplete Entire Lines (<C-x><C-l> 행 단위 일괄 자동완성)
- **Tip 118**: Autocomplete Filenames (<C-x><C-f> 파일 시스템 경로 자동완성)
- **Tip 119**: Autocomplete with Context Awareness (<C-x><C-o> 문맥 인식 옴니완성)

### Chapter 20: Find and Fix Typos with Vim's Spell Checker (Tip 120 ~ 123)
- **Tip 120**: Spell Check Your Work (:setlocal spell, ]s, z= 실시간 맞춤법 검사 및 교정)
- **Tip 121**: Use Alternate Spelling Dictionaries (spelllang 다국어/지역별 사전 전환)
- **Tip 122**: Add Words to the Spell File (zg, zw 사용자 전문 용어 사전 등록)
- **Tip 123**: Fix Spelling Errors from Insert Mode (<C-x>s 삽입 모드 내 즉시 맞춤법 교정)

### Chapter 21: Essential Modern Plugins (Tip 124 ~ 134)
- **Tip 124**: Add, Change, or Delete Delimiters (vim-surround: cs, ds, ysiw 구분자 제어)
- **Tip 125**: Repeat Plugin Actions with vim-repeat (. 키로 플러그인 조작 반복)
- **Tip 126**: Toggle Comments with vim-commentary (gcc, gcap 주석 토글 제어)
- **Tip 127**: Navigate Pairs with vim-unimpaired ([b, ]b, [e, ]e 대칭 단축키 탐색)
- **Tip 128**: Argument Text Objects with vim-argtextobj (cia, daa 함수 인자 Text Objects)
- **Tip 129**: Entire Buffer Text Object with textobj-entire (yie, dae 파일 전체 Text Objects)
- **Tip 130**: Replace with Register without Overwriting (replaceWithRegister: griw 레지스터 보존 치환)
- **Tip 131**: Swap Words and Text with vim-exchange (cxiw 텍스트 객체 상호 맞교환)
- **Tip 132**: Match Expanded Keywords with matchit (% 키 확장 HTML/조건문 대응)
- **Tip 133**: Visual Feedback for Yanks with vim-highlightedyank (복사 영역 시각적 피드백)
- **Tip 134**: Multi-Cursor Editing with vim-multiple-cursors (<A-n> 멀티 커서 동시 편집)

### Chapter 22: Cross-IDE Situational Keymap Drills (Tip 135 ~ 144)
- **Tip 135**: Drill 01: Explorer and Editor Focus Navigation (<Space>e, <Space>ee, Esc 탐색기/에디터 포커스 전환)
- **Tip 136**: Drill 02: Single File Compile and Diagnostics Traversal (<Space>cc, ]d, [d 단일 파일 컴파일 및 진단 에러 순회)
- **Tip 137**: Drill 03: Run and Debug Test in Isolation (<Space>rc, <Space>dc 단일 테스트/메인 메서드 격리 실행 및 디버깅)
- **Tip 138**: Drill 04: Toggle Embedded Terminal and Context Return (<Space>t, Esc 내장 터미널 토글 및 에디터 복귀)
- **Tip 139**: Drill 05: Symbol Navigation and Jump List Traversal (gd, gi, gr, <C-o> 심볼 탐색 및 점프 리스트 복귀)
- **Tip 140**: Drill 06: Three-Step Inline Refactoring (<Space>cr, <Space>ca, <Space>cf 인라인 이름 변경/인텐션/코드 서식 정렬)
- **Tip 141**: Drill 07: Vertical Window Split and Focus Navigation (<Space>sv, <C-l>, <C-h>, <Space>sc 수직 창 분할 및 포커스 탐색)
- **Tip 142**: Drill 08: Delimiter and Text Object Modification with Surround (cs"', ds", ysiw] 구분자 변경/삭제/래핑)
- **Tip 143**: Drill 09: Replace with Register without Clipboard Pollution (yiw, griw 무명 레지스터 보존 텍스트 치환)
- **Tip 144**: Drill 10: Swap Adjacent Identifiers with vim-exchange (cxiw 두 인접 식별자 위치 맞교환)
