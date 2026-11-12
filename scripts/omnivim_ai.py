#!/usr/bin/env python3
# ---
# title: omnivim_ai
# description: 헤드리스 Vim 실행, 실습 자동 채점, GUI 자동화를 묶은 AI 에이전트용 CLI·프로그램 엔진
# authors: [coralstay]
# license: AGPL-3.0-only
# status: draft
# created_date: '2026-11-06'
# updated_date: '2026-11-06'
# ---
"""
🥋 OmniVim AI Agent Interface (omnivim_ai.py)
Unified CLI and Programmatic Engine for AI Agents, MCP Servers, and Computer Use.
Supports headless Vim RPC execution, automatic practice grading, and GUI automation.
"""

import os
import sys
import re
import json
import argparse
import difflib
import subprocess
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

try:
    from data.all_tips import TIPS
except ImportError:
    TIPS = []

try:
    from computer_use import send_gui_action, ACTIONS  # ---- 1
except ImportError:
    ACTIONS = {}
    def send_gui_action(action, target_app=None):
        return False, "computer_use module unavailable"


class OmniVimAI:
    def __init__(self, root: Path = PROJECT_ROOT):
        self.root = root
        self.practice_dir = self.root / "practice"

    def get_tip_data(self, tip_id: int | str) -> dict | None:
        """Finds tip metadata from TIPS dataset."""
        try:
            num = int(str(tip_id).lower().replace("tip", ""))
        except ValueError:
            return None
        for t in TIPS:
            if t["tip_num"] == num:
                return t
        return None

    def get_tip_dir(self, tip_num: int) -> Path | None:
        """Finds the on-disk practice directory for a tip."""
        t = self.get_tip_data(tip_num)
        if t and "chapter_id" in t and "tip_id" in t:
            d = self.practice_dir / t["chapter_id"] / t["tip_id"]
            if d.is_dir():
                return d
        pattern = f"tip{tip_num:02d}_*"
        matches = sorted(list(self.practice_dir.glob(f"*/{pattern}")))
        return matches[0] if matches else None

    def list_tips(self, chapter: str = None, keyword: str = None) -> list[dict]:
        """Returns list of tips with current completion status."""
        results = []
        for t in TIPS:
            if chapter and chapter.lower() not in t["chapter_id"].lower() and chapter.lower() not in t["chapter_title"].lower():
                continue
            if keyword:
                kw = keyword.lower()
                if kw not in t["title"].lower() and kw not in t["concept"].lower() and kw not in t["mission"].lower():
                    continue

            tip_dir = self.get_tip_dir(t["tip_num"])
            passed = False
            if tip_dir and tip_dir.is_dir():
                p_files = list(tip_dir.glob("practice.*"))
                e_files = list(tip_dir.glob("expected_*"))
                if p_files and e_files:
                    try:
                        p_text = p_files[0].read_text(encoding="utf-8")
                        e_text = e_files[0].read_text(encoding="utf-8")
                        passed = (p_text == e_text)
                    except Exception:
                        passed = False

            results.append({
                "tip_num": t["tip_num"],
                "chapter_id": t["chapter_id"],
                "chapter_title": t["chapter_title"],
                "title": t["title"],
                "book_page": t["book_page"],
                "completed": passed,
                "practice_file": t["practice_file"],
                "keys_recommended": "".join(t["keys"]) if isinstance(t["keys"], list) else str(t["keys"])
            })
        return results

    def inspect_tip(self, tip_num: int) -> dict:
        """Returns full details of a specific practice tip."""
        t = self.get_tip_data(tip_num)
        if not t:
            return {"error": f"Tip {tip_num} not found"}

        tip_dir = self.get_tip_dir(tip_num)
        p_path = tip_dir / t["practice_file"] if tip_dir else None

        current_content = ""
        is_completed = False
        if p_path and p_path.is_file():
            current_content = p_path.read_text(encoding="utf-8")
            is_completed = (current_content == t["expected_content"])

        return {
            "tip_num": t["tip_num"],
            "chapter_id": t["chapter_id"],
            "chapter_title": t["chapter_title"],
            "title": t["title"],
            "book_page": t["book_page"],
            "concept": t["concept"],
            "mission": t["mission"],
            "recommended_keys": t["keys"],
            "practice_file": t["practice_file"],
            "practice_path": str(p_path) if p_path else None,
            "current_content": current_content,
            "expected_content": t["expected_content"],
            "completed": is_completed
        }

    def execute_vim_keys(self, target_file: Path | str, keys: str) -> tuple[bool, str]:
        """
        Executes raw Vim keystrokes headlessly against target_file using Neovim Lua API.
        Accurately interprets <Esc>, <CR>, <Space>, <C-v>, <C-a>, operators, and text objects.
        """
        target_path = Path(target_file).resolve()
        if not target_path.is_file():
            return False, f"File not found: {target_path}"

        # Clean string for lua string literal
        escaped_keys = keys.replace('\\', '\\\\').replace('"', '\\"').replace("'", "\\'")  # ---- 2

        shims_path = (self.root / "scripts" / "headless_plugin_shims.lua").resolve()
        shim_load = f"pcall(dofile, '{shims_path}')\n" if shims_path.is_file() else ""

        # Neovim nvim_feedkeys Lua call
        lua_code = (  # ---- 3
            f"{shim_load}"
            f"local keys = vim.api.nvim_replace_termcodes('{escaped_keys}', true, false, true)\n"
            f"vim.api.nvim_feedkeys(keys, 'x', false)\n"
            f"vim.cmd('silent! wa')\n"
            f"vim.cmd('qall!')\n"
        )

        cmd = [  # ---- 4
            "nvim",
            "--clean",
            "--headless",
            "-n",
            str(target_path),
            "-c", f"lua {lua_code}"
        ]

        try:
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=10)  # ---- 5
            if res.returncode == 0:
                return True, target_path.read_text(encoding="utf-8")
            else:
                return False, f"Neovim execution error: {res.stderr}"
        except Exception as e:
            return False, f"Subprocess error: {str(e)}"

    def check_tip(self, tip_num: int) -> dict:
        """Grades the current practice file against expected output."""
        t = self.get_tip_data(tip_num)
        if not t:
            return {"passed": False, "error": f"Tip {tip_num} not found"}

        tip_dir = self.get_tip_dir(tip_num)
        if not tip_dir:
            return {"passed": False, "error": f"Directory for tip {tip_num} not found"}

        p_files = list(tip_dir.glob("practice.*"))
        e_files = list(tip_dir.glob("expected_*"))
        if not p_files or not e_files:
            return {"passed": False, "error": "Missing practice or expected file"}

        p_lines = p_files[0].read_text(encoding="utf-8").splitlines(keepends=True)
        e_lines = e_files[0].read_text(encoding="utf-8").splitlines(keepends=True)

        diff = "".join(difflib.unified_diff(p_lines, e_lines, fromfile=p_files[0].name, tofile=e_files[0].name))  # ---- 6
        passed = (diff == "")

        return {
            "tip_num": tip_num,
            "title": t["title"],
            "passed": passed,
            "diff": diff,
            "practice_file": str(p_files[0])
        }

    def reset_tip(self, tip_num: int) -> dict:
        """Restores the practice file from .original backup."""
        tip_dir = self.get_tip_dir(tip_num)
        if not tip_dir:
            return {"success": False, "error": f"Tip {tip_num} not found"}

        b_files = list(tip_dir.glob(".original_*"))
        if not b_files:
            return {"success": False, "error": "Original backup file missing"}

        backup = b_files[0]
        orig_name = backup.name.replace(".original_", "")
        target = tip_dir / orig_name
        target.write_text(backup.read_text(encoding="utf-8"), encoding="utf-8")  # ---- 7
        return {"success": True, "restored": str(target)}

    def solve_tip(self, tip_num: int, keys: str = None) -> dict:
        """
        AI Solving Pipeline:
        1. Resets practice file to original
        2. Applies given keystrokes (or recommended keys if omitted)
        3. Grades result and returns structured evaluation report
        """
        # 1. Reset first
        self.reset_tip(tip_num)  # ---- 8

        t = self.get_tip_data(tip_num)
        if not t:
            return {"passed": False, "error": f"Tip {tip_num} not found"}

        if not keys:
            # Use recommended keys from dataset
            if isinstance(t["keys"], list):
                filtered = [k for k in t["keys"] if not re.search(r'[\uac00-\ud7a3]', k)]  # ---- 9
                keys = "".join(filtered)
            else:
                keys = str(t["keys"])

        tip_dir = self.get_tip_dir(tip_num)
        p_file = tip_dir / t["practice_file"]

        # 2. Execute
        ok, res_text = self.execute_vim_keys(p_file, keys)
        if not ok:
            return {"passed": False, "error": res_text, "keys_used": keys}

        # 3. Grade
        grade = self.check_tip(tip_num)
        grade["keys_used"] = keys
        return grade


# CLI Argument Parser
def main():  # ---- 10
    base_parser = argparse.ArgumentParser(add_help=False)
    base_parser.add_argument("--json", action="store_true", help="Output machine-readable JSON")

    parser = argparse.ArgumentParser(prog="omnivim", description="🥋 OmniVim AI Agent & Computer Use Interface", parents=[base_parser])
    subparsers = parser.add_subparsers(dest="command")

    # tips
    p_tips = subparsers.add_parser("tips", parents=[base_parser], help="List all practice tips")
    p_tips.add_argument("--chapter", help="Filter by chapter")
    p_tips.add_argument("--keyword", help="Filter by keyword")

    # tip
    p_tip = subparsers.add_parser("tip", parents=[base_parser], help="Inspect a specific tip")
    p_tip.add_argument("id", type=int, help="Tip number (e.g. 1)")

    # exec
    p_exec = subparsers.add_parser("exec", parents=[base_parser], help="Execute Vim keystrokes headlessly on any file")
    p_exec.add_argument("--file", required=True, help="Target file path")
    p_exec.add_argument("--keys", required=True, help="Vim keystrokes (e.g. 'A;<Esc>j.j.')")

    # solve
    p_solve = subparsers.add_parser("solve", parents=[base_parser], help="Solve practice tip using Vim keystrokes")
    p_solve.add_argument("id", type=int, help="Tip number")
    p_solve.add_argument("--keys", help="Custom keystrokes (defaults to recommended solution)")

    # check
    p_check = subparsers.add_parser("check", parents=[base_parser], help="Grade a practice tip")
    p_check.add_argument("id", type=int, help="Tip number")

    # reset
    p_reset = subparsers.add_parser("reset", parents=[base_parser], help="Reset practice tip to original state")
    p_reset.add_argument("id", type=int, help="Tip number")

    # gui
    p_gui = subparsers.add_parser("gui", parents=[base_parser], help="Trigger OmniVim GUI action via macOS Computer Use bridge")
    p_gui.add_argument("action", help=f"Action name: {', '.join(sorted(ACTIONS.keys()))}")
    p_gui.add_argument("--app", help="Target application name (e.g. 'IntelliJ IDEA', 'CLion', 'Code')")

    # keymaps
    subparsers.add_parser("keymaps", parents=[base_parser], help="List unified cross-IDE keymap matrix")

    args = parser.parse_args()
    engine = OmniVimAI()

    if args.command == "tips":
        data = engine.list_tips(chapter=args.chapter, keyword=args.keyword)
        if args.json:
            print(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            print(f"\n📋 OmniVim Tips ({len(data)} items):")
            for t in data:
                status = "✓ [DONE]" if t["completed"] else "○ [TODO]"
                print(f"  {status} Tip {t['tip_num']:02d}: {t['title']} ({t['chapter_title']})")

    elif args.command == "tip":
        data = engine.inspect_tip(args.id)
        if args.json:
            print(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            if "error" in data:
                print(f"❌ {data['error']}", file=sys.stderr)
                sys.exit(1)
            print(f"\n🥋 Tip {data['tip_num']}: {data['title']} ({data['book_page']})")
            print(f"📖 Concept: {data['concept']}")
            print(f"🎯 Mission: {data['mission']}")
            print(f"⌨️  Keys   : {data['recommended_keys']}")
            print(f"📁 File   : {data['practice_path']}")
            print(f"Status    : {'Completed (PASS)' if data['completed'] else 'Pending'}")

    elif args.command == "exec":
        ok, res = engine.execute_vim_keys(args.file, args.keys)
        out = {"success": ok, "file": args.file, "keys": args.keys, "result": res if ok else None, "error": None if ok else res}
        if args.json:
            print(json.dumps(out, ensure_ascii=False, indent=2))
        else:
            if ok:
                print(f"✓ Vim keys applied successfully to {args.file}")
            else:
                print(f"❌ Execution failed: {res}", file=sys.stderr)
                sys.exit(1)

    elif args.command == "solve":
        data = engine.solve_tip(args.id, keys=args.keys)
        if args.json:
            print(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            if data.get("passed"):
                print(f"🎉 [PASS] Tip {args.id} solved successfully with keys: '{data.get('keys_used')}'")
            else:
                print(f"❌ [FAIL] Tip {args.id} failed:\n{data.get('diff', data.get('error'))}", file=sys.stderr)
                sys.exit(1)

    elif args.command == "check":
        data = engine.check_tip(args.id)
        if args.json:
            print(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            if data.get("passed"):
                print(f"✓ [PASS] Tip {args.id} matches expected solution!")
            else:
                print(f"❌ [FAIL] Tip {args.id} differs:\n{data.get('diff')}", file=sys.stderr)
                sys.exit(1)

    elif args.command == "reset":
        data = engine.reset_tip(args.id)
        if args.json:
            print(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            if data.get("success"):
                print(f"✓ Tip {args.id} restored to original state.")
            else:
                print(f"❌ Reset failed: {data.get('error')}", file=sys.stderr)
                sys.exit(1)

    elif args.command == "gui":
        ok, msg = send_gui_action(args.action, target_app=args.app)
        out = {"success": ok, "action": args.action, "app": args.app, "message": msg}
        if args.json:
            print(json.dumps(out, ensure_ascii=False, indent=2))
        else:
            if ok:
                print(f"✓ Computer Use: Injected '{args.action}' into {'active window' if not args.app else args.app}")
            else:
                print(f"❌ Computer Use error: {msg}", file=sys.stderr)
                sys.exit(1)

    elif args.command == "keymaps":
        km = {
            "leader": "<Space>",
            "actions": ACTIONS,
            "mnemonic_prefixes": {
                "<Space>e": "Explorer & Window Focus",
                "<Space>c": "Code Actions, Compile & Structure",
                "<Space>r": "Run & Test Execution",
                "<Space>t": "Terminal & Output Tool Windows",
                "<Space>f": "Find & Search",
                "<Space>b": "Buffer & Tab Management",
                "<Space>s": "Splits"
            }
        }
        if args.json:
            print(json.dumps(km, ensure_ascii=False, indent=2))
        else:
            print("Unified OmniVim Keymaps:")
            for k, v in km["mnemonic_prefixes"].items():
                print(f"  {k:<12} : {v}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()

# ======== 노트 ========
# 1 computer_use는 선택 의존
#   설명: macOS 전용 GUI 브리지라 import에 실패해도 엔진 전체는 돌아야 한다. 실패하면 ACTIONS를 비우고 send_gui_action을 항상 실패를 돌려주는 대역으로 바꾼다.
#   관련: scripts/computer_use.py
#   개념: 선택적 의존(graceful degradation)
# 2 Lua 문자열 이스케이프
#   설명: 키 입력을 nvim -c 'lua ...' 안의 작은따옴표 Lua 리터럴로 넣으므로 역슬래시와 따옴표를 먼저 이스케이프한다. 빠지면 키 문자열이 Lua 문법을 깨뜨린다.
#   개념: 이스케이프
# 3 nvim_feedkeys로 키 실행
#   설명: shim 로드, <Esc> 같은 표기를 termcode로 바꾸고, 'x' 모드로 끝까지 실행한 뒤 변경을 저장하고 종료한다. 사람이 에디터에서 치는 것과 같은 경로로 풀이를 검증한다.
#   관련: scripts/headless_plugin_shims.lua
#   개념: 헤드리스 실행
# 4 깨끗한 헤드리스 nvim
#   설명: --clean으로 사용자 설정과 플러그인을 배제하고 -n으로 스왑 파일을 쓰지 않는다. 채점이 개발자 환경에 좌우되지 않게 하는 불변식이다. 플러그인 동작은 shim이 대신한다.
#   개념: 재현성
# 5 10초 타임아웃
#   설명: nvim이 입력 대기 등으로 멈춰도 채점기가 매달리지 않게 한다. 실패하면 stderr를 오류 메시지로 돌려준다.
# 6 채점은 정확한 텍스트 일치
#   설명: unified diff가 빈 문자열일 때만 통과다. 공백 한 칸 차이도 실패이고, diff 자체가 학습자에게 보여줄 피드백이 된다.
#   관련: scripts/check.sh
#   개념: 정확 일치 채점
# 7 원본 백업에서 복원
#   설명: 각 실습 폴더의 .original_* 파일이 편집 전 원본 상태의 단일 근거다. 대상 이름은 접두사를 뗀 practice.* 이다.
#   관련: scripts/generate_practice.py
# 8 풀이 전에 항상 reset
#   설명: solve를 몇 번 불러도 같은 결과가 나오도록(멱등) 먼저 원본으로 되돌린다. CI의 144팁 감사가 이 성질에 기대고 있다.
#   관련: .github/workflows/ci.yml
#   개념: 멱등
# 9 한글 키 항목 제외
#   설명: 데이터셋의 keys 목록에는 설명용 한글 문장이 섞여 있다. 한글이 든 항목은 실제 키 입력이 아니므로 거른다.
#   관련: scripts/data/all_tips.py (저장소에는 포함하지 않음)
# 10 CLI 진입점
#   설명: 서브커맨드 tips/tip/exec/solve/check/reset/gui/keymaps를 OmniVimAI 엔진에 연결한다. --json은 모든 서브커맨드가 공유해 에이전트가 기계 판독 출력을 얻는다. 실패하면 종료 코드 1이다.
#   관련: scripts/mcp_server.py
