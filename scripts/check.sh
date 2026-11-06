#!/usr/bin/env bash
# ---
# title: check
# description: practice.* 와 expected_* 를 diff로 비교해 PASS/FAIL을 판정하는 채점 스크립트
# authors: [coralstay]
# license: AGPL-3.0-only
# status: draft
# created_date: '2026-11-06'
# updated_date: '2026-11-06'
# ---
# [설계 메모]
# Practical Vim Practice Validator (check.sh)
# Automated diff grader comparing practice.* and expected_*

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PRACTICE_DIR="$PROJECT_ROOT/practice"

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

if [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
  echo -e "${BOLD}사용법:${NC} check <tip_number | tip_name | tip_dir> [--help]"
  echo "예시: check 1 또는 check tip01"
  exit 0
fi

if [ -z "$1" ]; then
  echo -e "${BOLD}사용법:${NC} check <tip_number | tip_name | tip_dir> [--help]"
  echo "예시: check 1 또는 check tip01"
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

PRACTICE_FILE=$(find "$TARGET_DIR" -maxdepth 1 -type f -name "practice.*" | head -n 1)
EXPECTED_FILE=$(find "$TARGET_DIR" -maxdepth 1 -type f -name "expected_*" | head -n 1)

if [ -z "$PRACTICE_FILE" ] || [ -z "$EXPECTED_FILE" ]; then
  echo -e "${RED}❌ 실습 파일 또는 정답 파일이 누락되었습니다: $TARGET_DIR${NC}"
  exit 1
fi

TIP_NAME=$(basename "$TARGET_DIR")
TIP_NUM=$(echo "$TIP_NAME" | sed -E 's/^tip0*([0-9]+).*/\1/')
echo -e "${CYAN}🔍 ${TIP_NAME} 채점 진행 중...${NC}"

if diff -u "$PRACTICE_FILE" "$EXPECTED_FILE" > /tmp/vim_diff.txt; then
  echo -e "${GREEN}${BOLD}🎉 [PASS] 축하합니다! 완벽하게 실습 미션을 성공했습니다!${NC}"
  echo -e "${GREEN}✓ 파일 내용이 정답과 100% 일치합니다.${NC}"
  exit 0
else
  echo -e "${RED}${BOLD}❌ [FAIL] 아직 정답과 차이가 있습니다.${NC}"
  echo -e "${YELLOW}--- [내 작업 결과 vs 기대 결과 차이] ---${NC}"
  cat /tmp/vim_diff.txt
  echo -e "${CYAN}------------------------------------------------${NC}"
  echo -e "다시 편집하려면: ${BOLD}./scripts/practice.sh $TIP_NUM${NC}"
  echo -e "처음부터 다시 하려면: ${BOLD}./scripts/reset.sh $TIP_NUM${NC}"
  exit 1
fi
