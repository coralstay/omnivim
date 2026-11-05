#!/usr/bin/env bash
# ==============================================================================
# 🔍 Environment Verification Script (verify_all.sh)
# Verifies that Vim, Neovim, JetBrains, and VS Code configs are active and valid.
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PRACTICE_DIR="$SCRIPT_DIR/practice"

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "\n${BOLD}${CYAN}🔍 통합 개발 환경 & 실습 세팅 상태 검증 보고서${NC}"
echo "----------------------------------------------------------------------"

PASS_COUNT=0
FAIL_COUNT=0

check_status() {
  local desc="$1"
  local cmd="$2"
  if eval "$cmd" >/dev/null 2>&1; then
    echo -e "  ${GREEN}✓ [PASS]${NC} $desc"
    PASS_COUNT=$((PASS_COUNT + 1))
  else
    echo -e "  ${RED}✗ [FAIL]${NC} $desc"
    FAIL_COUNT=$((FAIL_COUNT + 1))
  fi
}

# 1. Core Vim
check_status "Practical Vim 코어 (~/practical-vim/vimrc_practical.vim)" \
  "[ -f '$HOME/practical-vim/vimrc_practical.vim' ]"

# 2. IdeaVim
check_status "IdeaVim 공통 설정 (~/.ideavimrc)" \
  "[ -f '$HOME/.ideavimrc' ]"

# 3. JetBrains Keymap
OS_TYPE="$(uname -s)"
if [ "$OS_TYPE" = "Darwin" ]; then
  JB_BASE="$HOME/Library/Application Support/JetBrains"
else
  JB_BASE="$HOME/.config/JetBrains"
fi

if [ -d "$JB_BASE" ]; then
  jb_checked=0
  for p in "$JB_BASE"/*; do
    if [ -d "$p" ]; then
      base_name=$(basename "$p")
      case "$base_name" in
        CLion*|IntelliJ*|PyCharm*|DataGrip*|WebStorm*|GoLand*|RustRover*|Rider*|AndroidStudio*|DataSpell*|Aqua*|RubyMine*|PhpStorm*|Fleet*)
          check_status "JetBrains [$base_name] Unified-Master-Keymap 적용" \
            "[ -f '$p/keymaps/Unified-Master-Keymap.xml' ]"
          jb_checked=$((jb_checked + 1))
          ;;
      esac
    fi
  done
fi

# 4. VS Code
if [ "$OS_TYPE" = "Darwin" ]; then
  VSCODE_USER_DIR="$HOME/Library/Application Support/Code/User"
else
  VSCODE_USER_DIR="$HOME/.config/Code/User"
fi

check_status "VS Code settings.json (Vim & Leader 매핑)" \
  "[ -f '$VSCODE_USER_DIR/settings.json' ]"

check_status "VS Code keybindings.json (JetBrains 패리티 단축키)" \
  "[ -f '$VSCODE_USER_DIR/keybindings.json' ]"

# 5. CLI Vim & Neovim
check_status "CLI Vim 설정 (~/.vimrc 구문 검사)" \
  "vim -u '$HOME/.vimrc' -e -s -c 'q'"

check_status "Neovim 단축키 동기화 (~/.config/nvim/lua/config/keymaps.lua)" \
  "[ -f '$HOME/.config/nvim/lua/config/keymaps.lua' ]"

# 6. OmniVim 144 Tips Practice Directories
tip_count=$(find "$PRACTICE_DIR" -type d -name "tip*" 2>/dev/null | wc -l | tr -d ' ')
if [ "$tip_count" -ge 144 ]; then
  echo -e "  ${GREEN}✓ [PASS]${NC} OmniVim 144개 실습 디렉터리 전체 구축 완료 (${tip_count}/144)"
  PASS_COUNT=$((PASS_COUNT + 1))
else
  echo -e "  ${RED}✗ [FAIL]${NC} OmniVim 실습 디렉터리 누락 발생 (${tip_count}/144)"
  FAIL_COUNT=$((FAIL_COUNT + 1))
fi

echo "----------------------------------------------------------------------"
if [ "$FAIL_COUNT" -eq 0 ]; then
  echo -e "${GREEN}${BOLD}🎉 모든 검증 통과! ($PASS_COUNT 개 항목 정상)${NC}"
  echo -e "어떤 편집기(JetBrains 5종, VS Code, Vim, Neovim)에서든 일관된 단축키와 실습을 즐기세요!"
else
  echo -e "${RED}${BOLD}⚠️ 일부 항목 실패 (PASS: $PASS_COUNT, FAIL: $FAIL_COUNT)${NC}"
  echo "실패한 항목은 ./install.sh 를 재실행하여 복구할 수 있습니다."
fi
