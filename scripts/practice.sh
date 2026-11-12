#!/usr/bin/env bash
# ---
# title: practice
# description: 선택한 팁의 실습 파일을 원하는 에디터로 여는 대화형 실습 실행기
# authors: [coralstay]
# license: AGPL-3.0-only
# status: draft
# created_date: '2026-11-06'
# updated_date: '2026-11-06'
# ---
# [설계 메모]
# Practical Vim Practice Runner (practice.sh)
# Self-contained interactive practice runner architecture.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PRACTICE_DIR="$PROJECT_ROOT/practice"

# ANSI Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

show_usage() {
  echo -e "${BOLD}사용법:${NC} practice [tip_number | -i | --list] [옵션]"
  echo ""
  echo -e "${BOLD}옵션:${NC}"
  echo "  -i, --interactive 대화형 fzf 검색 런처 실행"
  echo "  --vim             CLI Vim으로 열기 (기본값)"
  echo "  --nvim            Neovim으로 열기"
  echo "  --code            Visual Studio Code로 열기"
  echo "  --idea            IntelliJ IDEA로 열기"
  echo "  --clion           CLion으로 열기"
  echo "  --pycharm         PyCharm으로 열기"
  echo "  --list            사용 가능한 전체 팁 목록 표시"
  echo "  --help            이 도움말 표시"
  echo ""
  echo -e "${BOLD}예시:${NC}"
  echo "  practice             # 대화형 TUI 검색 런처 실행 (터미널)"
  echo "  practice -i          # 대화형 TUI 검색 런처 명시적 실행"
  echo "  practice 1           # Tip 1 (The Dot Command) 실습 시작"
  echo "  practice 113 --nvim  # Tip 113 (vim-surround) Neovim으로 실습"
  echo "  practice 87 --code   # Tip 87 (Substitute) VS Code로 실습"
  exit 0
}

if [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
  show_usage
fi

if [ "$1" = "-i" ] || [ "$1" = "--interactive" ]; then
  shift
  exec python3 "$SCRIPT_DIR/interactive_menu.py" "$@"  # ---- 1
fi

if [ -z "$1" ] && [ -t 0 ]; then  # ---- 2
  exec python3 "$SCRIPT_DIR/interactive_menu.py" "$@"
fi

if [ "$1" = "--list" ] || [ -z "$1" ]; then
  echo -e "${CYAN}${BOLD}📋 Practical Vim 실습 목록:${NC}"
  find "$PRACTICE_DIR" -type d -name "tip*" | sort | while read -r dir; do
    tip_name=$(basename "$dir")
    readme="$dir/README.md"
    if [ -f "$readme" ]; then
      title=$(head -n 1 "$readme" | sed 's/^# //')
      echo -e "  ${YELLOW}$tip_name${NC} : $title"
    fi
  done
  echo ""
  if [ -z "$1" ]; then
    show_usage
  fi
  exit 0
fi

INPUT_ARG="$1"
shift || true

# Parse editor option
EDITOR_CMD="vim"
while [ $# -gt 0 ]; do
  case "$1" in
    --vim)     EDITOR_CMD="vim" ;;
    --nvim)    EDITOR_CMD="nvim" ;;
    --code)    EDITOR_CMD="code" ;;
    --idea)    EDITOR_CMD="open -a 'IntelliJ IDEA'" ;;  # ---- 3
    --clion)   EDITOR_CMD="open -a 'CLion'" ;;
    --pycharm) EDITOR_CMD="open -a 'PyCharm'" ;;
    *) echo -e "${RED}알 수 없는 옵션: $1${NC}"; show_usage ;;
  esac
  shift
done

TARGET_DIR=""
if [ -d "$INPUT_ARG" ]; then
  TARGET_DIR="$(cd "$INPUT_ARG" && pwd)"
elif [ -d "$PROJECT_ROOT/$INPUT_ARG" ]; then
  TARGET_DIR="$(cd "$PROJECT_ROOT/$INPUT_ARG" && pwd)"
elif [[ "$INPUT_ARG" =~ ^[0-9]+$ ]]; then
  NUM=$((10#$INPUT_ARG))  # ---- 4
  FORMATTED_TIP=$(printf "tip%02d" "$NUM")
  TARGET_DIR=$(find "$PRACTICE_DIR" -type d -name "${FORMATTED_TIP}_*" | head -n 1)
else
  CLEAN_TIP=$(echo "$INPUT_ARG" | sed 's/^[tT]ip//')
  if [[ "$CLEAN_TIP" =~ ^[0-9]+$ ]]; then
    NUM=$((10#$CLEAN_TIP))
    FORMATTED_TIP=$(printf "tip%02d" "$NUM")
    TARGET_DIR=$(find "$PRACTICE_DIR" -type d -name "${FORMATTED_TIP}_*" | head -n 1)
  else
    TARGET_DIR=$(find "$PRACTICE_DIR" -type d -name "*$INPUT_ARG*" | head -n 1)
  fi
fi

if [ -z "$TARGET_DIR" ] || [ ! -d "$TARGET_DIR" ]; then
  echo -e "${RED}❌ 실습 디렉터리를 찾을 수 없습니다: '${INPUT_ARG}'${NC}"
  echo -e "목록을 보려면: ${YELLOW}$0 --list${NC}"
  exit 1
fi

TIP_NAME=$(basename "$TARGET_DIR")
TIP_NUM=$(echo "$TIP_NAME" | sed -E 's/^tip0*([0-9]+).*/\1/')

README_PATH="$TARGET_DIR/README.md"
PRACTICE_FILE=$(find "$TARGET_DIR" -maxdepth 1 -type f -name "practice.*" | head -n 1)

if [ -z "$PRACTICE_FILE" ]; then
  echo -e "${RED}❌ 실습 대상 파일이 없습니다: $TARGET_DIR${NC}"
  exit 1
fi

echo -e "${CYAN}======================================================================${NC}"
if [ -f "$README_PATH" ]; then
  head -n 20 "$README_PATH" | grep -v "^#" | grep -v "^>" | grep -v "^---" | sed '/^$/d' | head -n 8 || true
fi
echo -e "${CYAN}======================================================================${NC}"
echo -e "${GREEN}🎯 실습 파일:${NC} ${BOLD}$(basename "$PRACTICE_FILE")${NC}"
echo -e "${YELLOW}💡 실습 완료 후 채점:${NC} ${BOLD}./scripts/check.sh $TIP_NUM${NC}"
echo -e "${CYAN}======================================================================${NC}"

# Launch editor
case "$EDITOR_CMD" in
  vim)
    vim "$PRACTICE_FILE"
    ;;
  nvim)
    nvim "$PRACTICE_FILE"
    ;;
  code)
    code "$PRACTICE_FILE"
    ;;
  open*)
    eval "$EDITOR_CMD '$PRACTICE_FILE'"  # ---- 5
    ;;
esac

# ======== 노트 ========
# 1 -i는 파이썬 런처로 위임
#   설명: exec로 프로세스를 interactive_menu.py에 넘기고 돌아오지 않는다. 남은 인자는 에디터 옵션으로 전달된다.
#   관련: scripts/interactive_menu.py
# 2 인자 없고 TTY면 런처
#   설명: 터미널에서 인자 없이 부르면 fzf 런처를 연다. 파이프나 CI에서는 목록을 출력한다.
#   관련: scripts/interactive_menu.py
# 3 앱 번들은 open -a 문자열
#   설명: JetBrains IDE는 CLI 런처가 없을 수 있어 macOS의 open -a로 연다. 이 값은 아래 case의 open*) 분기로 간다.
# 4 10# 접두
#   설명: check.sh와 같은 8진수 방지다.
#   관련: scripts/check.sh
# 5 eval로 open 명령 실행
#   설명: EDITOR_CMD가 여러 단어('open -a ...')라 eval이 필요하다. 값은 위 case에서 고정 문자열로만 정해지므로 외부 입력이 섞이지 않는 것이 전제다. 파일 경로는 작은따옴표로 감싼다.
#   개념: eval 위험
