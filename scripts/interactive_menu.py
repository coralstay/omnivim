#!/usr/bin/env python3
# ---
# title: interactive_menu
# description: fzf로 144개 팁을 검색하고 README를 미리보는 대화형 TUI 런처
# authors: [coralstay]
# license: AGPL-3.0-only
# status: draft
# created_date: '2026-11-06'
# updated_date: '2026-11-06'
# ---
"""
🥋 OmniVim Interactive TUI Launcher (interactive_menu.py)
Provides interactive fuzzy search and real-time README preview
for all 144 practice tips using fzf (with clean fallback).
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PRACTICE_DIR = PROJECT_ROOT / "practice"

try:
    sys.path.insert(0, str(PROJECT_ROOT / "scripts" / "data"))
    from all_tips import TIPS
except ImportError:
    TIPS = []

def run_fzf_selector() -> tuple[bool, int | None]:
    """Launches fzf with real-time markdown preview. Returns (ran_fzf, selected_tip)."""
    fzf_bin = shutil.which("fzf")
    if not fzf_bin:
        return False, None

    # Prepare lines for fzf: Display string \t Directory Path \t Tip Number
    lines = []
    for t in TIPS:
        tip_num = t["tip_num"]
        ch_title = t.get("chapter_title", "")
        title = t.get("title", "")
        tip_dir = PRACTICE_DIR / t["chapter_id"] / t["tip_id"]
        
        display = f"Tip {tip_num:03d} │ {title:<48} │ [{ch_title}]"
        lines.append(f"{display}\t{tip_dir}\t{tip_num}")

    input_data = "\n".join(lines)

    # Use bat for syntax highlight preview if available, otherwise cat
    preview_cmd = "bat --color=always --style=plain {2}/README.md 2>/dev/null || cat {2}/README.md 2>/dev/null"

    cmd = [
        fzf_bin,
        "--delimiter=\t",
        "--with-nth=1",
        "--prompt=🥋 OmniVim [1-144] > ",
        "--header=Enter: 실습 열기 │ ESC: 취소 │ 검색어로 필터링",
        f"--preview={preview_cmd}",
        "--preview-window=right:55%:wrap",
        "--height=85%",
        "--layout=reverse",
        "--border"
    ]

    try:
        res = subprocess.run(cmd, input=input_data, capture_output=True, text=True)
        if res.returncode == 0 and res.stdout.strip():
            parts = res.stdout.strip().split("\t")
            if len(parts) >= 3:
                return True, int(parts[2])
        # User pressed ESC / Ctrl-C / canceled
        return True, None
    except Exception:
        return False, None

def run_fallback_selector() -> int | None:
    """Clean terminal search fallback when fzf is unavailable."""
    print("\n🥋 \033[1mOmniVim 실습 검색 (1~144)\033[0m")
    try:
        query = input("검색할 팁 번호 또는 키워드 입력 (Enter시 전체 목록): ").strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return None
    
    matches = []
    for t in TIPS:
        if not query:
            matches.append(t)
        elif query.isdigit() and t["tip_num"] == int(query):
            matches.append(t)
        elif query.lower() in t["title"].lower() or query.lower() in t.get("concept", "").lower():
            matches.append(t)

    if not matches:
        print("검색 결과가 없습니다.")
        return None

    print(f"\n총 {len(matches)}개 일치:")
    for idx, m in enumerate(matches[:15], 1):
        print(f"  [{m['tip_num']:3d}] {m['title']} ({m['chapter_title']})")
    if len(matches) > 15:
        print(f"  ... 외 {len(matches) - 15}개 생략")

    try:
        sel = input("\n실습을 시작할 팁 번호 입력 (q: 취소): ").strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return None

    if sel.isdigit():
        return int(sel)
    return None

def main():
    editor_args = [arg for arg in sys.argv[1:] if arg.startswith("--") and arg not in ("-i", "--interactive")]
    
    if not sys.stdin.isatty():
        print("💡 대화형 메뉴는 터미널(TTY) 환경에서 실행해야 합니다.")
        sys.exit(1)

    ran_fzf, selected_tip = run_fzf_selector()
    if not ran_fzf:
        selected_tip = run_fallback_selector()

    if selected_tip:
        practice_script = PROJECT_ROOT / "scripts" / "practice.sh"
        cmd = ["bash", str(practice_script), str(selected_tip)] + editor_args
        os.execvp("bash", cmd)

if __name__ == "__main__":
    main()
