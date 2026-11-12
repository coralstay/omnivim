#!/usr/bin/env python3
# ---
# title: computer_use
# description: AppleScript로 JetBrains·VS Code를 조작하는 macOS GUI 자동화 브리지
# authors: [coralstay]
# license: AGPL-3.0-only
# status: draft
# created_date: '2026-11-06'
# updated_date: '2026-11-06'
# ---
"""
OmniVim Computer Use & GUI Automation Bridge for macOS.
Enables AI Agents (Anthropic Computer Use, vision agents) to control
JetBrains IDEs and VS Code using standardized OmniVim shortcuts via AppleScript.
"""

import sys
import subprocess
import shutil

KEY_CODES = {  # ---- 1
    "escape": 53,
    "f1": 122,
    "f2": 120,
    "f6": 97,
    "f9": 101,
    "f12": 111,
    "return": 36,
    "enter": 36,
    "space": 49,
    "tab": 48
}

ACTIONS = {  # ---- 2
    # Focus / Navigation
    "focus-editor": {"type": "code", "code": 53},                                    # Esc (FocusEditor)
    "explorer": {"type": "keystroke", "key": "1", "using": "command down"},           # Cmd+1 (Project View)
    "show-in-explorer": {"type": "code", "code": 122, "using": "option down"},        # Opt+F1 (Select In)
    "terminal": {"type": "code", "code": 111, "using": "option down"},                # Opt+F12 (Terminal)
    "problems": {"type": "keystroke", "key": "6", "using": "command down"},           # Cmd+6 (Problems)
    "structure": {"type": "keystroke", "key": "7", "using": "command down"},          # Cmd+7 (Structure)
    "git": {"type": "keystroke", "key": "9", "using": "command down"},                # Cmd+9 (Git Tool Window)

    # Compile & Build
    "compile": {"type": "code", "code": 101, "using": ["command down", "shift down"]},# Cmd+Shift+F9 (CompileDirty)
    "build-project": {"type": "code", "code": 101, "using": "command down"},          # Cmd+F9 (Build Project)

    # Run & Test & Debug
    "run-test": {"type": "keystroke", "key": "r", "using": ["control down", "shift down"]}, # Ctrl+Shift+R (RunClass)
    "debug": {"type": "keystroke", "key": "d", "using": ["control down", "shift down"]},    # Ctrl+Shift+D (DebugClass)
    "rerun": {"type": "keystroke", "key": "r", "using": "control down"},              # Ctrl+R (Run)
    "stop": {"type": "code", "code": 120, "using": "command down"},                   # Cmd+F2 (Stop)

    # Code Editing & Refactoring
    "format": {"type": "keystroke", "key": "l", "using": ["command down", "option down"]}, # Cmd+Opt+L (Reformat)
    "rename": {"type": "code", "code": 97, "using": "shift down"},                    # Shift+F6 (Rename)
    "quickfix": {"type": "code", "code": 36, "using": "option down"},                 # Opt+Enter (Intention/QuickFix)
    "organize-imports": {"type": "keystroke", "key": "o", "using": ["control down", "option down"]}, # Ctrl+Opt+O
    "symbol-popup": {"type": "code", "code": 111, "using": "command down"},           # Cmd+F12 (File Structure)

    # Search & Files
    "find-files": {"type": "keystroke", "key": "p", "using": "command down"},         # Cmd+P (Go to File)
    "grep": {"type": "keystroke", "key": "f", "using": ["command down", "shift down"]},# Cmd+Shift+F (Find in Path)
    "recent-files": {"type": "keystroke", "key": "e", "using": "command down"},       # Cmd+E (Recent Files)
    "search-everywhere": {"type": "code", "code": 49, "using": "command down"}        # Cmd+Space or Double Shift
}

def is_macos():
    return sys.platform == "darwin"

def run_applescript(script: str) -> tuple[bool, str]:
    if not is_macos():  # ---- 3
        return False, "Computer Use GUI bridge currently supports macOS via AppleScript."
    if not shutil.which("osascript"):
        return False, "osascript not found on system."

    res = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)  # ---- 4
    if res.returncode == 0:
        return True, res.stdout.strip()
    return False, res.stderr.strip()

def send_gui_action(action_name: str, target_app: str = None) -> tuple[bool, str]:
    action = ACTIONS.get(action_name.lower())
    if not action:
        available = ", ".join(sorted(ACTIONS.keys()))
        return False, f"Unknown action '{action_name}'. Available actions: {available}"

    lines = []
    if target_app:
        lines.append(f'tell application "{target_app}" to activate')
        lines.append('delay 0.1')  # ---- 5

    lines.append('tell application "System Events"')

    using_clause = ""
    if "using" in action:
        u = action["using"]
        if isinstance(u, list):
            using_clause = f' using {{{", ".join(u)}}}'  # ---- 6
        else:
            using_clause = f' using {u}'

    if action["type"] == "code":
        lines.append(f'  key code {action["code"]}{using_clause}')
    else:
        lines.append(f'  keystroke "{action["key"]}"{using_clause}')

    lines.append('end tell')
    script = "\n".join(lines)
    return run_applescript(script)

def send_vim_keystrokes_gui(keys: str, target_app: str = None) -> tuple[bool, str]:
    """Types raw characters into the active GUI window."""
    lines = []
    if target_app:
        lines.append(f'tell application "{target_app}" to activate')
        lines.append('delay 0.1')

    lines.append('tell application "System Events"')
    for ch in keys:
        if ch == "\n":
            lines.append('  key code 36') # Return
        elif ch == "\x1b" or ch == "\\e":
            lines.append('  key code 53') # Esc
        elif ch == "\t":
            lines.append('  key code 48') # Tab
        elif ch == " ":
            lines.append('  key code 49') # Space
        elif ch == '"':
            lines.append('  keystroke "\\""')
        elif ch == '\\':  # ---- 7
            lines.append('  keystroke "\\\\"')
        else:
            lines.append(f'  keystroke "{ch}"')
    lines.append('end tell')
    script = "\n".join(lines)
    return run_applescript(script)

if __name__ == "__main__":  # ---- 8
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help", "--list", "help", "list"):
        print("Usage: computer_use.py <action> [target_app]")
        print("Available actions:", ", ".join(sorted(ACTIONS.keys())))
        sys.exit(0 if len(sys.argv) >= 2 and sys.argv[1] in ("-h", "--help", "--list", "help", "list") else 1)

    act = sys.argv[1]
    app = sys.argv[2] if len(sys.argv) > 2 else None
    ok, out = send_gui_action(act, app)
    if ok:
        print(f"✓ Injected OmniVim action '{act}' successfully")
    else:
        print(f"✗ Failed: {out}", file=sys.stderr)
        sys.exit(1)

# ======== 노트 ========
# 1 AppleScript 키 코드표
#   설명: macOS key code 번호 표다: Escape 53, F1 122, F2 120, F6 97, F9 101, F12 111, Return 36, Space 49. 문자가 아니라 가상 키 번호라 F키와 Esc는 keystroke가 아니라 key code로 보낸다.
#   개념: key code
# 2 통합 단축키 액션표
#   설명: 액션 이름을 AppleScript 호출 한 가지(key code 또는 keystroke)와 수식키로 옮긴다. 줄 끝 주석은 대응하는 JetBrains 단축키 이름이다. configs의 키맵과 같은 체계를 유지해야 한다.
#   관련: configs/jetbrains/Unified-Master-Keymap.xml, configs/vscode/keybindings.json
# 3 macOS 가드
#   설명: osascript가 있는 macOS에서만 동작한다. 그 밖에서는 예외 대신 (False, 이유)를 돌려줘 호출자(omnivim_ai의 대역과 같은 규약)가 처리한다.
#   관련: scripts/omnivim_ai.py
# 4 osascript 실행
#   설명: AppleScript는 -e 인자로 넘기고 종료 코드 0이면 stdout, 아니면 stderr를 돌려준다. 접근성(Accessibility) 권한이 없으면 여기서 실패한다.
#   개념: macOS 접근성 권한
# 5 활성화 후 0.1초 대기
#   설명: 대상 앱을 앞으로 가져온 직후 키를 보내면 이전 창이 입력을 받는다. 짧게 기다려 순서를 보장한다.
# 6 수식키 목록 문법
#   설명: 수식키가 여럿이면 AppleScript는 using {a, b} 형태의 리스트를 요구한다. 하나면 using a 이다.
# 7 따옴표와 역슬래시 이스케이프
#   설명: AppleScript 문자열 리터럴 안에 들어가는 문자라 " 와 \ 는 앞에 역슬래시를 붙여 써야 한다.
#   개념: 이스케이프
# 8 CLI 진입점
#   설명: 인자 없이 부르면 사용법과 액션 목록을 보이고 종료 코드 1, help류 인자면 0이다. 실패하면 stderr와 종료 코드 1이다.
#   관련: scripts/omnivim_ai.py (gui 서브커맨드)
