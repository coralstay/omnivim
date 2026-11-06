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

# macOS AppleScript key codes
# Escape: 53, F1: 122, F2: 120, F6: 97, F9: 101, F12: 111, Return: 36, Space: 49
KEY_CODES = {
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

ACTIONS = {
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
    if not is_macos():
        return False, "Computer Use GUI bridge currently supports macOS via AppleScript."
    if not shutil.which("osascript"):
        return False, "osascript not found on system."

    res = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
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
        lines.append('delay 0.1')

    lines.append('tell application "System Events"')

    using_clause = ""
    if "using" in action:
        u = action["using"]
        if isinstance(u, list):
            using_clause = f' using {{{", ".join(u)}}}'
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
        elif ch == '\\':
            lines.append('  keystroke "\\\\"')
        else:
            lines.append(f'  keystroke "{ch}"')
    lines.append('end tell')
    script = "\n".join(lines)
    return run_applescript(script)

if __name__ == "__main__":
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
