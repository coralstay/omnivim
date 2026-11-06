#!/usr/bin/env bash
# ---
# title: install
# description: Vim, Neovim, JetBrains, VS Code 설정을 한 번에 설치하는 macOS/Linux용 마스터 설치 스크립트
# authors: [coralstay]
# license: AGPL-3.0-only
# status: draft
# created_date: '2026-11-06'
# updated_date: '2026-11-06'
# ---
# [설계 메모]
# 🚀 Unified Development & Practical Vim Master Installer
# One-click script to configure Vim, Neovim, JetBrains IDEs, and VS Code.
# Works on macOS and Linux.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIGS_DIR="$SCRIPT_DIR/configs"
BACKUP_DIR="$HOME/.vim_ide_backups/$(date +%Y%m%d_%H%M%S)"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${CYAN}${BOLD}"
echo "======================================================================"
echo "   🥋 Practical Vim & Unified Cross-IDE Master Installer"
echo "======================================================================"
echo -e "${NC}"

# 1. OS Detection
OS_TYPE="$(uname -s)"
echo -e "${BLUE}📌 운영체제 감지:${NC} $OS_TYPE"

mkdir -p "$BACKUP_DIR"
echo -e "${YELLOW}📁 백업 디렉터리:${NC} $BACKUP_DIR"

backup_file() {
  local target="$1"
  if [ -f "$target" ] || [ -d "$target" ]; then
    echo -e "  ${YELLOW}↳ 백업 중:${NC} $target"
    cp -R "$target" "$BACKUP_DIR/"
  fi
}

# ------------------------------------------------------------------------------
# 2. Deploy Practical Vim Core (~/practical-vim/)
# ------------------------------------------------------------------------------
echo -e "\n${BOLD}[1/6] Practical Vim 공통 코어 설정 배포...${NC}"
mkdir -p "$HOME/practical-vim"
backup_file "$HOME/practical-vim/vimrc_practical.vim"
cp "$CONFIGS_DIR/practical_vim/vimrc_practical.vim" "$HOME/practical-vim/vimrc_practical.vim"
echo -e "${GREEN}✓ ~/practical-vim/vimrc_practical.vim 배포 완료${NC}"

# ------------------------------------------------------------------------------
# 3. Deploy IdeaVim (~/.ideavimrc)
# ------------------------------------------------------------------------------
echo -e "\n${BOLD}[2/6] IdeaVim 설정 배포...${NC}"
backup_file "$HOME/.ideavimrc"
cp "$CONFIGS_DIR/ideavim/.ideavimrc" "$HOME/.ideavimrc"
echo -e "${GREEN}✓ ~/.ideavimrc 배포 완료 (모든 JetBrains IDE 공유)${NC}"

# ------------------------------------------------------------------------------
# 4. Deploy JetBrains Unified Keymaps to ALL Products
# ------------------------------------------------------------------------------
echo -e "\n${BOLD}[3/6] JetBrains 제품군 단축키 일괄 적용 중...${NC}"
JB_DIRS=()

if [ "$OS_TYPE" = "Darwin" ]; then
  JB_BASE="$HOME/Library/Application Support/JetBrains"
else
  JB_BASE="$HOME/.config/JetBrains"
fi

if [ -d "$JB_BASE" ]; then
  for p in "$JB_BASE"/*; do
    if [ -d "$p" ]; then
      base_name=$(basename "$p")
      # Filter IDE configuration folders (CLion, IntelliJ, PyCharm, DataGrip, WebStorm, DataSpell, etc.)
      case "$base_name" in
        CLion*|IntelliJ*|PyCharm*|DataGrip*|WebStorm*|GoLand*|RustRover*|Rider*|AndroidStudio*|DataSpell*|Aqua*|RubyMine*|PhpStorm*|Fleet*)
          JB_DIRS+=("$p")
          ;;
      esac
    fi
  done
fi

if [ ${#JB_DIRS[@]} -gt 0 ]; then
  for ide_dir in "${JB_DIRS[@]}"; do
    ide_name=$(basename "$ide_dir")
    keymaps_dir="$ide_dir/keymaps"
    options_dir="$ide_dir/options/mac"
    if [ "$OS_TYPE" != "Darwin" ]; then
      options_dir="$ide_dir/options"
    fi

    mkdir -p "$keymaps_dir" "$options_dir"
    cp "$CONFIGS_DIR/jetbrains/Unified-Master-Keymap.xml" "$keymaps_dir/"
    cp "$CONFIGS_DIR/jetbrains/keymap.xml" "$options_dir/"
    echo -e "${GREEN}  ✓ $ide_name${NC} ➔ 'Unified Master Keymap' 활성화 완료"
  done
else
  echo -e "${YELLOW}  ℹ 감지된 JetBrains 설정 디렉터리가 없습니다. ($JB_BASE)${NC}"
fi

# ------------------------------------------------------------------------------
# 5. Deploy VS Code Configurations
# ------------------------------------------------------------------------------
echo -e "\n${BOLD}[4/6] Visual Studio Code 설정 및 단축키 배포...${NC}"
if [ "$OS_TYPE" = "Darwin" ]; then
  VSCODE_USER_DIR="$HOME/Library/Application Support/Code/User"
else
  VSCODE_USER_DIR="$HOME/.config/Code/User"
fi

mkdir -p "$VSCODE_USER_DIR"
backup_file "$VSCODE_USER_DIR/settings.json"
backup_file "$VSCODE_USER_DIR/keybindings.json"

cp "$CONFIGS_DIR/vscode/settings.json" "$VSCODE_USER_DIR/settings.json"
cp "$CONFIGS_DIR/vscode/keybindings.json" "$VSCODE_USER_DIR/keybindings.json"
echo -e "${GREEN}✓ VS Code settings.json 및 keybindings.json (JetBrains 패리티) 배포 완료${NC}"

if command -v code >/dev/null 2>&1; then
  if ! code --list-extensions | grep -q "vscodevim.vim"; then
    echo -e "${BLUE}  ↳ VSCodeVim 확장 설치 중...${NC}"
    code --install-extension vscodevim.vim || true
  fi
fi

# ------------------------------------------------------------------------------
# 6. Deploy CLI Vim & Neovim Configurations
# ------------------------------------------------------------------------------
echo -e "\n${BOLD}[5/6] 터미널 Vim & Neovim 설정 배포...${NC}"
backup_file "$HOME/.vimrc"
cp "$CONFIGS_DIR/vim/.vimrc" "$HOME/.vimrc"
echo -e "${GREEN}✓ ~/.vimrc 배포 완료${NC}"

NVIM_CONFIG_DIR="$HOME/.config/nvim/lua/config"
mkdir -p "$NVIM_CONFIG_DIR"
backup_file "$NVIM_CONFIG_DIR/keymaps.lua"
cp "$CONFIGS_DIR/nvim/keymaps.lua" "$NVIM_CONFIG_DIR/keymaps.lua"
echo -e "${GREEN}✓ ~/.config/nvim/lua/config/keymaps.lua 배포 완료${NC}"

# ------------------------------------------------------------------------------
# 7. Set Permissions & Generate All 144 Practice Exercises
# ------------------------------------------------------------------------------
echo -e "\n${BOLD}[6/6] 스크립트 실행 권한 부여 및 실습 환경 스캐폴딩...${NC}"
chmod +x "$SCRIPT_DIR"/bin/* "$SCRIPT_DIR"/scripts/*.sh "$SCRIPT_DIR"/scripts/*.py "$SCRIPT_DIR"/*.sh 2>/dev/null || true
if [ -f "$SCRIPT_DIR/scripts/generate_practice.py" ]; then
  python3 "$SCRIPT_DIR/scripts/generate_practice.py"
fi

echo -e "\n${CYAN}======================================================================${NC}"
echo -e "${GREEN}${BOLD}🎉 모든 편집기 설정 및 실습 환경 구축이 성공적으로 완료되었습니다!${NC}"
echo -e "${CYAN}======================================================================${NC}"

# Run verification script
if [ -f "$SCRIPT_DIR/verify_all.sh" ]; then
  bash "$SCRIPT_DIR/verify_all.sh"
fi
