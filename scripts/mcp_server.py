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

logging.basicConfig(level=logging.INFO, stream=sys.stderr, format="[OmniVim-MCP] %(message)s")

engine = OmniVimAI()

TOOLS = [
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


def handle_tool_call(name: str, args: dict) -> str:
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


def main():
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
                    "protocolVersion": "2024-11-05",
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
            # Client acknowledgement, no response required
            pass

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
                        "code": -32603,
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
            if req_id is not None:
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
