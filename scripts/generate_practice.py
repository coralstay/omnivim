#!/usr/bin/env python3
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
    from data.all_tips import TIPS
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

        if verify_only:
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

        # 1. README.md
        readme_file.write_text(generate_readme(tip), encoding="utf-8")

        # 2. practice file (skip overwrite if not force)
        if not practice_file.exists() or force:
            practice_file.write_text(tip["practice_content"], encoding="utf-8")
            backup_file.write_text(tip["practice_content"], encoding="utf-8")
            created_count += 1
        else:
            skipped_count += 1

        # 3. expected file (always sync with truth)
        expected_file.write_text(tip["expected_content"], encoding="utf-8")

    if not verify_only:
        print(f"✅ 스캐폴드 완료! 생성/갱신: {created_count}개, 보존: {skipped_count}개")
        print(f"📁 총 실습 디렉터리: {len(list(PRACTICE_DIR.glob('*/tip*')))}개")


def main():
    parser = argparse.ArgumentParser(description="Practical Vim Practice Scaffolder")
    parser.add_argument("--force", "-f", action="store_true", help="기존 실습 파일 덮어쓰기")
    parser.add_argument("--verify", "-v", action="store_true", help="누락된 실습 파일 검증만 수행")
    args = parser.parse_args()

    scaffold(force=args.force, verify_only=args.verify)


if __name__ == "__main__":
    main()
