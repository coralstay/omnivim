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
    from all_tips import TIPS  # ---- 1
except ImportError:
    TIPS = []

def run_fzf_selector() -> tuple[bool, int | None]:
    """Launches fzf with real-time markdown preview. Returns (ran_fzf, selected_tip)."""
    fzf_bin = shutil.which("fzf")
    if not fzf_bin:
        return False, None

    lines = []
    for t in TIPS:
        tip_num = t["tip_num"]
        ch_title = t.get("chapter_title", "")
        title = t.get("title", "")
        tip_dir = PRACTICE_DIR / t["chapter_id"] / t["tip_id"]
        
        display = f"Tip {tip_num:03d} │ {title:<48} │ [{ch_title}]"
        lines.append(f"{display}\t{tip_dir}\t{tip_num}")  # ---- 2

    input_data = "\n".join(lines)

    preview_cmd = "bat --color=always --style=plain {2}/README.md 2>/dev/null || cat {2}/README.md 2>/dev/null"  # ---- 3

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
        return True, None  # ---- 4
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
    
    if not sys.stdin.isatty():  # ---- 5
        print("💡 대화형 메뉴는 터미널(TTY) 환경에서 실행해야 합니다.")
        sys.exit(1)

    ran_fzf, selected_tip = run_fzf_selector()
    if not ran_fzf:
        selected_tip = run_fallback_selector()

    if selected_tip:
        practice_script = PROJECT_ROOT / "scripts" / "practice.sh"
        cmd = ["bash", str(practice_script), str(selected_tip)] + editor_args
        os.execvp("bash", cmd)  # ---- 6

if __name__ == "__main__":
    main()

# ======== 노트 ========
# 1 TIPS는 선택 의존
#   설명: 메타데이터 파일이 없는 환경(공개 저장소 클론)에서도 import 오류로 죽지 않게 빈 목록으로 대체한다.
#   개념: graceful degradation
# 2 탭으로 구분한 fzf 입력
#   설명: 표시 문자열, 팁 디렉터리, 팁 번호를 탭으로 잇는다. fzf는 --with-nth=1로 첫 열만 보이고 선택 결과에서 세 번째 열을 번호로 쓴다.
# 3 미리보기는 bat, 없으면 cat
#   설명: 설치 여부에 의존하지 않도록 || 로 대체 경로를 둔다. {2}는 fzf의 두 번째 열(디렉터리)이다.
#   개념: fzf 자리표시자
# 4 취소와 선택 없음
#   설명: ESC나 Ctrl-C로 끝나도 fzf는 실행된 것이므로 (True, None)이다. 호출자가 대체 검색기를 또 띄우지 않게 하는 구분이다.
# 5 TTY에서만 동작
#   설명: fzf와 input()은 터미널이 필요하다. 파이프나 CI에서는 안내만 하고 종료 코드 1이다.
# 6 execvp로 프로세스 교체
#   설명: 선택 후에는 practice.sh로 현재 프로세스를 바꿔 에디터가 터미널을 직접 쓰게 한다. 돌아오지 않는다.
#   관련: scripts/practice.sh
