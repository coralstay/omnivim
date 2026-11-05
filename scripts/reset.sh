#!/usr/bin/env bash
# ==============================================================================
# Practical Vim Practice Reset Tool (reset.sh)
# Restores practice file back to original unedited state.
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PRACTICE_DIR="$PROJECT_ROOT/practice"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BOLD='\033[1m'
NC='\033[0m'

if [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
  echo -e "${BOLD}사용법:${NC} reset <tip_number | tip_name | tip_dir> | --all [--help]"
  echo "예시: reset 1 또는 reset tip01"
  echo "전체 초기화: reset --all"
  exit 0
fi

if [ "$1" = "--all" ]; then
  echo -e "${YELLOW}🔄 전체 실습 파일을 최초 상태로 초기화합니다...${NC}"
  find "$PRACTICE_DIR" -type f -name ".original_*" | while read -r backup; do
    dir=$(dirname "$backup")
    orig_name=$(basename "$backup" | sed 's/^\.original_//')
    cp "$backup" "$dir/$orig_name"
  done
  echo -e "${GREEN}✅ 전체 실습 파일 복구 완료!${NC}"
  exit 0
fi

if [ -z "$1" ]; then
  echo -e "${BOLD}사용법:${NC} reset <tip_number | tip_name | tip_dir> | --all [--help]"
  echo "예시: reset 1 또는 reset tip01"
  echo "전체 초기화: reset --all"
  exit 1
fi

INPUT_ARG="$1"
TARGET_DIR=""

if [ -d "$INPUT_ARG" ]; then
  TARGET_DIR="$(cd "$INPUT_ARG" && pwd)"
elif [ -d "$PROJECT_ROOT/$INPUT_ARG" ]; then
  TARGET_DIR="$(cd "$PROJECT_ROOT/$INPUT_ARG" && pwd)"
elif [[ "$INPUT_ARG" =~ ^[0-9]+$ ]]; then
  NUM=$((10#$INPUT_ARG))
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
  exit 1
fi

BACKUP_FILE=$(find "$TARGET_DIR" -maxdepth 1 -type f -name ".original_*" | head -n 1)

if [ -z "$BACKUP_FILE" ]; then
  echo -e "${RED}❌ 원본 백업 파일이 없습니다. generate_practice.py를 다시 실행하세요.${NC}"
  exit 1
fi

TIP_NAME=$(basename "$TARGET_DIR")
TARGET_FILE="$TARGET_DIR/$(basename "$BACKUP_FILE" | sed 's/^\.original_//')"
cp "$BACKUP_FILE" "$TARGET_FILE"
echo -e "${GREEN}✅ ${TIP_NAME} 실습 파일이 최초 원본 상태로 복구되었습니다:${NC} $TARGET_FILE"
