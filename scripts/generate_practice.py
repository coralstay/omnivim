#!/usr/bin/env python3
# ---
# title: generate_practice
# description: scripts/data/all_tips.py 의 선언적 메타데이터로 실습 디렉터리를 생성하는 스캐폴드 생성기
# authors: [coralstay]
# license: AGPL-3.0-only
# status: draft
# created_date: '2026-11-06'
# updated_date: '2026-11-06'
# ---
"""
Practical Vim Practice Scaffold Generator
Declarative Scaffold Engine architecture for self-contained practice modules.
Reads declarative metadata from scripts/data/all_tips.py and generates self-contained practice directories.
Covers all 144 tips (Practical Vim Chapters 1-20 Tips 1-123 + Essential Modern Plugins Chapter 21 Tips 124-134 + Situational Drills Chapter 22 Tips 135-144).
"""

import sys
import os
import argparse
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(CURRENT_DIR))

try:
    from data.all_tips import TIPS  # ---- 1
except ImportError:
    print("❌ Failed to import TIPS metadata from data.all_tips")
    sys.exit(1)

PROJECT_ROOT = CURRENT_DIR.parent
PRACTICE_DIR = PROJECT_ROOT / "practice"


def generate_readme(tip: dict) -> str:
    keys_formatted = " ".join([f"`{k}`" for k in tip["keys"]])
    return f"""# Tip {tip['tip_num']}: {tip['title']}

> **출처**: 《Practical Vim, Second Edition》 {tip.get('book_page', '')}  
> **챕터**: {tip['chapter_title']} ({tip['chapter_id']})

---

## 🎯 Concept (학습 목표)
{tip['concept']}

---

## 📝 Mission (실습 미션)
{tip['mission']}

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **{keys_formatted}**

---

## 📂 실습 파일 안내
- **`{tip['practice_file']}`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_{tip['practice_file']}`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh {tip['tip_num']}
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `{tip['practice_file']}`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh {tip['tip_num']}
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh {tip['tip_num']}
   ```
"""


def scaffold(force: bool = False, verify_only: bool = False):
    print(f"🚀 Practical Vim 실습 스캐폴드 엔진 가동 (총 {len(TIPS)}개 팁 전체 생성)")
    created_count = 0
    skipped_count = 0

    if not PRACTICE_DIR.exists():
        PRACTICE_DIR.mkdir(parents=True, exist_ok=True)

    for tip in TIPS:
        chapter_dir = PRACTICE_DIR / tip["chapter_id"]
        tip_dir = chapter_dir / tip["tip_id"]

        if verify_only:  # ---- 2
            expected_files = [
                tip_dir / "README.md",
                tip_dir / tip["practice_file"],
                tip_dir / f"expected_{tip['practice_file']}",
            ]
            missing = [f for f in expected_files if not f.exists()]
            if missing:
                print(f"⚠️ [누락] Tip {tip['tip_num']}: {missing}")
            continue

        tip_dir.mkdir(parents=True, exist_ok=True)

        readme_file = tip_dir / "README.md"
        practice_file = tip_dir / tip["practice_file"]
        backup_file = tip_dir / f".original_{tip['practice_file']}"
        expected_file = tip_dir / f"expected_{tip['practice_file']}"

        readme_file.write_text(generate_readme(tip), encoding="utf-8")

        if not practice_file.exists() or force:  # ---- 3
            practice_file.write_text(tip["practice_content"], encoding="utf-8")
            backup_file.write_text(tip["practice_content"], encoding="utf-8")
            created_count += 1
        else:
            skipped_count += 1

        expected_file.write_text(tip["expected_content"], encoding="utf-8")  # ---- 4

    if not verify_only:
        print(f"✅ 스캐폴드 완료! 생성/갱신: {created_count}개, 보존: {skipped_count}개")
        print(f"📁 총 실습 디렉터리: {len(list(PRACTICE_DIR.glob('*/tip*')))}개")


def main():  # ---- 5
    parser = argparse.ArgumentParser(description="Practical Vim Practice Scaffolder")
    parser.add_argument("--force", "-f", action="store_true", help="기존 실습 파일 덮어쓰기")
    parser.add_argument("--verify", "-v", action="store_true", help="누락된 실습 파일 검증만 수행")
    args = parser.parse_args()

    scaffold(force=args.force, verify_only=args.verify)


if __name__ == "__main__":
    main()

# ======== 노트 ========
# 1 팁 메타데이터가 유일한 원천
#   설명: 모든 실습은 scripts/data/all_tips.py의 TIPS에서만 만들어진다. 이 파일은 저장소에 없으므로(.gitignore) 없으면 스캐폴드를 포기하고 종료 코드 1로 끝낸다.
#   관련: .gitignore
#   개념: SSOT
# 2 --verify는 읽기 전용
#   설명: 누락 점검만 하고 파일을 만들지 않는다. README, 실습 파일, 정답 파일 세 가지가 있어야 온전한 팁이다.
# 3 실습 파일은 덮어쓰지 않는다
#   설명: 학습자가 편집 중인 practice.* 를 지키려고 --force가 아니면 이미 있는 파일은 건드리지 않는다. 새로 만들 때만 .original_* 백업도 같이 쓴다.
#   관련: scripts/reset.sh
#   개념: 보존 불변식
# 4 정답 파일은 항상 동기화
#   설명: expected_* 는 데이터셋이 기준이라 매번 덮어쓴다. 실습 파일 보존과 반대 규칙이다.
#   개념: SSOT
# 5 CLI 진입점
#   설명: --force와 --verify 두 옵션을 scaffold()에 그대로 넘긴다.
