#!/usr/bin/env python3
# ---
# title: mcp_server
# description: stdio JSON-RPC 2.0 위에서 omnivim 도구를 MCP 에이전트에 노출하는 MCP 서버
# authors: [coralstay]
# license: AGPL-3.0-only
# status: draft
# created_date: '2026-11-06'
# updated_date: '2026-11-06'
# ---
"""
🥋 OmniVim MCP Server (Model Context Protocol)
Compliant with Anthropic MCP Specification (JSON-RPC 2.0 over stdio).
Allows Claude Desktop, Cursor, Claude Code, and Antigravity agents
to interact with OmniVim tools, run Vim keystrokes, and trigger GUI actions.
"""

import sys
import json
import logging
from pathlib import Path

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from omnivim_ai import OmniVimAI
from computer_use import ACTIONS

logging.basicConfig(level=logging.INFO, stream=sys.stderr, format="[OmniVim-MCP] %(message)s")  # ---- 1

engine = OmniVimAI()

TOOLS = [  # ---- 2
    {
        "name": "omnivim_list_tips",
        "description": "Lists all 144 OmniVim practice tips (Practical Vim 1-123 + Essential Plugins 124-134 + Keymap Drills 135-144) with their completion status.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "chapter": {
                    "type": "string",
                    "description": "Optional chapter filter (e.g. 'ch01', 'Normal Mode')"
                },
                "keyword": {
                    "type": "string",
                    "description": "Optional keyword search query"
                }
            }
        }
    },
    {
        "name": "omnivim_get_tip",
        "description": "Gets full specification for an OmniVim practice tip including instructions, current code, expected result, and recommended keystrokes.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "tip_id": {
                    "type": "integer",
                    "description": "Tip number (1 through 144)"
                }
            },
            "required": ["tip_id"]
        }
    },
    {
        "name": "omnivim_solve_tip",
        "description": "Applies a sequence of Vim keystrokes to a practice exercise, checks if it passes, and returns the grading diff.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "tip_id": {
                    "type": "integer",
                    "description": "Tip number to solve"
                },
                "keystrokes": {
                    "type": "string",
                    "description": "Vim keystrokes to test (e.g. 'A;<Esc>j.j.'). If omitted, uses the recommended solution."
                }
            },
            "required": ["tip_id"]
        }
    },
    {
        "name": "omnivim_apply_vim_keys",
        "description": "Executes arbitrary Vim keystrokes headlessly against any local file using Neovim Lua API.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Absolute or relative path to the target text file"
                },
                "keystrokes": {
                    "type": "string",
                    "description": "Vim keystrokes (e.g. 'ciwreplacement<Esc>', 'dd', 'gUiw')"
                }
            },
            "required": ["file_path", "keystrokes"]
        }
    },
    {
        "name": "omnivim_trigger_gui_action",
        "description": "Triggers a unified OmniVim shortcut (Computer Use) in active JetBrains IDE or VS Code window via macOS Accessibility.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "description": "Action name: compile, run-test, debug, focus-editor, explorer, terminal, format, rename, quickfix, organize-imports, symbol-popup, find-files, grep, recent-files, search-everywhere",
                    "enum": list(ACTIONS.keys())
                },
                "target_app": {
                    "type": "string",
                    "description": "Optional application name (e.g. 'IntelliJ IDEA', 'CLion', 'PyCharm', 'Code')"
                }
            },
            "required": ["action"]
        }
    },
    {
        "name": "omnivim_get_unified_keymap",
        "description": "Retrieves the complete cross-IDE unified keymap matrix for JetBrains and VS Code.",
        "inputSchema": {
            "type": "object",
            "properties": {}
        }
    }
]


def handle_tool_call(name: str, args: dict) -> str:  # ---- 3
    if name == "omnivim_list_tips":
        res = engine.list_tips(chapter=args.get("chapter"), keyword=args.get("keyword"))
        return json.dumps(res, ensure_ascii=False, indent=2)

    elif name == "omnivim_get_tip":
        tip_id = args.get("tip_id")
        res = engine.inspect_tip(tip_id)
        return json.dumps(res, ensure_ascii=False, indent=2)

    elif name == "omnivim_solve_tip":
        tip_id = args.get("tip_id")
        keys = args.get("keystrokes")
        res = engine.solve_tip(tip_id, keys=keys)
        return json.dumps(res, ensure_ascii=False, indent=2)

    elif name == "omnivim_apply_vim_keys":
        fpath = args.get("file_path")
        keys = args.get("keystrokes")
        ok, out = engine.execute_vim_keys(fpath, keys)
        return json.dumps({"success": ok, "file": fpath, "result": out}, ensure_ascii=False, indent=2)

    elif name == "omnivim_trigger_gui_action":
        action = args.get("action")
        app = args.get("target_app")
        from computer_use import send_gui_action
        ok, msg = send_gui_action(action, target_app=app)
        return json.dumps({"success": ok, "action": action, "app": app, "message": msg}, ensure_ascii=False, indent=2)

    elif name == "omnivim_get_unified_keymap":
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
        return json.dumps(km, ensure_ascii=False, indent=2)

    else:
        return json.dumps({"error": f"Unknown tool '{name}'"})


def main():  # ---- 4
    logging.info("OmniVim MCP Server starting over stdio...")
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        try:
            req = json.loads(line)
        except Exception as e:
            logging.error(f"JSON parse error: {e}")
            continue

        req_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})

        if method == "initialize":
            res = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "protocolVersion": "2024-11-05",  # ---- 5
                    "capabilities": {
                        "tools": {}
                    },
                    "serverInfo": {
                        "name": "omnivim-mcp-server",
                        "version": "1.0.0"
                    }
                }
            }
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

        elif method == "notifications/initialized":
            pass  # ---- 6

        elif method == "tools/list":
            res = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "tools": TOOLS
                }
            }
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

        elif method == "tools/call":
            tool_name = params.get("name")
            tool_args = params.get("arguments", {})
            try:
                text_output = handle_tool_call(tool_name, tool_args)
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [
                            {
                                "type": "text",
                                "text": text_output
                            }
                        ]
                    }
                }
            except Exception as e:
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {
                        "code": -32603,  # ---- 7
                        "message": str(e)
                    }
                }
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

        elif method == "ping":
            res = {"jsonrpc": "2.0", "id": req_id, "result": {}}
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

        else:
            if req_id is not None:  # ---- 8
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {
                        "code": -32601,
                        "message": f"Method not found: {method}"
                    }
                }
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()

if __name__ == "__main__":
    main()

# ======== 노트 ========
# 1 로그는 stderr로
#   설명: stdout은 JSON-RPC 응답 전용이다. 로그가 stdout에 섞이면 클라이언트가 프레임을 파싱하지 못하므로 stderr로 보낸다.
#   개념: stdio 전송
# 2 공개 도구 목록
#   설명: tools/list가 그대로 돌려주는 JSON Schema 목록이다. handle_tool_call의 분기 이름과 1:1로 맞아야 한다.
#   개념: JSON Schema
# 3 도구 호출 분배
#   설명: 도구 이름으로 OmniVimAI 엔진 메서드에 연결하고 결과는 JSON 문자열로 돌려준다. 모르는 이름은 error JSON이다.
#   관련: scripts/omnivim_ai.py
# 4 stdio 서버 진입점
#   설명: 한 줄에 JSON-RPC 요청 하나를 읽고 응답 한 줄을 stdout에 쓴다(줄 단위 JSON).
#   관련: scripts/audit_all.py (initialize 왕복 점검)
#   개념: JSON-RPC 2.0
# 5 프로토콜 버전
#   설명: MCP 사양 2024-11-05 판에 맞춘 값이다. 클라이언트와 협상이 필요해지면 여기를 바꾼다.
# 6 알림에는 응답하지 않는다
#   설명: notifications/initialized는 클라이언트의 확인 알림이라 id가 없고 응답을 쓰면 안 된다.
#   개념: JSON-RPC 알림
# 7 도구 예외는 -32603
#   설명: 도구 실행 중 예외는 JSON-RPC 내부 오류 코드로 응답해 서버가 죽지 않게 한다.
# 8 id 있는 요청만 오류 응답
#   설명: 모르는 메서드라도 id가 없는 알림이면 침묵한다. id가 있으면 -32601을 돌려준다.
#   개념: JSON-RPC 오류 코드
