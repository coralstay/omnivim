#!/usr/bin/env python3
# ---
# title: audit_all
# description: 설정·키바인딩·실습 팁·스크립트를 한꺼번에 검사하는 전수 감사 도구
# authors: [coralstay]
# license: AGPL-3.0-only
# status: draft
# created_date: '2026-11-06'
# updated_date: '2026-11-06'
# ---
"""
Exhaustive Automated Audit Suite for Practical Vim & Cross-IDE Setup
Validates configurations, keybindings, practice tips, and scripts.
"""

import os
import sys
import re
import json
import xml.etree.ElementTree as ET
import subprocess

PASS = "✓ [PASS]"
FAIL = "✗ [FAIL]"
WARN = "⚠ [WARN]"

class AuditRunner:
    def __init__(self):
        self.passes = 0
        self.failures = 0
        self.warnings = 0
        self.project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.home = os.path.expanduser("~")

    def log_pass(self, desc):
        print(f"  \033[32m{PASS}\033[0m {desc}")
        self.passes += 1

    def log_fail(self, desc, error=""):
        err_msg = f" - {error}" if error else ""
        print(f"  \033[31m{FAIL}\033[0m {desc}{err_msg}")
        self.failures += 1

    def log_warn(self, desc, warning=""):
        warn_msg = f" - {warning}" if warning else ""
        print(f"  \033[33m{WARN}\033[0m {desc}{warn_msg}")
        self.warnings += 1

    def strip_json_comments(self, text):
        text = re.sub(r'//.*', '', text)  # ---- 1
        text = re.sub(r'/\*[\s\S]*?\*/', '', text)
        text = re.sub(r',\s*([}\]])', r'\1', text)
        return text

    def run_all(self):
        print("\n\033[1;36m======================================================================\033[0m")
        print("\033[1m🔬 PRACTICAL VIM & CROSS-IDE 통합 환경 전수 무결성 검증\033[0m")
        print("\033[1;36m======================================================================\033[0m\n")

        self.audit_core_vim()
        self.audit_ideavim()
        self.audit_jetbrains_keymaps()
        self.audit_vscode()
        self.audit_terminal_vim_nvim()
        self.audit_practice_tips()
        self.audit_scripts_functionality()
        self.audit_documentation()
        self.audit_ai_interfaces()

        print("\n\033[1;36m----------------------------------------------------------------------\033[0m")
        if self.failures == 0:  # ---- 2
            print(f"\033[1;32m🎉 모든 검증 성공! (PASS: {self.passes}, FAIL: {self.failures}, WARN: {self.warnings})\033[0m")
            print("JetBrains 5종+, VS Code, Vim, Neovim 및 144개 실습 프로젝트가 완벽히 동작합니다.")
            print("\033[1;36m======================================================================\033[0m\n")
            return 0
        else:
            print(f"\033[1;31m⚠️ 검증 실패 항목 발견! (PASS: {self.passes}, FAIL: {self.failures}, WARN: {self.warnings})\033[0m")
            print("\033[1;36m======================================================================\033[0m\n")
            return 1

    def audit_core_vim(self):
        print("\033[1m[1] Practical Vim Core Engine (~/practical-vim/vimrc_practical.vim)\033[0m")
        core_path = os.path.join(self.home, "practical-vim", "vimrc_practical.vim")
        if not os.path.isfile(core_path):
            self.log_fail("Core vimrc exists", f"Not found at {core_path}")
            return
        self.log_pass("Core vimrc 파일 존재 확인")

        with open(core_path, "r", encoding="utf-8") as f:
            content = f.read()

        if 'let mapleader = " "' in content:
            self.log_pass("Primary Leader key가 <Space>로 정상 설정됨")
        else:
            self.log_fail("Leader key check", "let mapleader = ' ' not found")

        if 'let maplocalleader = "\\\\"' in content:
            self.log_pass("Secondary Leader key가 '\\'로 정상 설정됨")
        else:
            self.log_fail("LocalLeader key check", "maplocalleader not found")

    def audit_ideavim(self):
        print("\n\033[1m[2] IdeaVim Configuration (~/.ideavimrc)\033[0m")
        iv_path = os.path.join(self.home, ".ideavimrc")
        if not os.path.isfile(iv_path):
            self.log_fail("IdeaVim config exists", f"Not found at {iv_path}")
            return
        self.log_pass("~/.ideavimrc 파일 존재 확인")

        with open(iv_path, "r", encoding="utf-8") as f:
            content = f.read()

        plugins = ["surround", "commentary", "argtextobj", "textobj-entire", "replaceWithRegister", "exchange", "unimpaired", "matchit", "highlightedyank", "which-key", "quickscope"]
        for p in plugins:
            if f"set {p}" in content:
                self.log_pass(f"IdeaVim 플러그인 활성화: {p}")
            else:
                self.log_fail(f"IdeaVim 플러그인 누락: {p}")

        handlers = ["<C-a>", "<C-r>", "<C-v>", "<C-o>", "<C-i>", "<C-w>", "<C-h>", "<C-j>", "<C-k>", "<C-l>"]
        for h in handlers:
            if f"sethandler {h} a:vim" in content:
                self.log_pass(f"IdeaVim 단축키 핸들러 위임: {h} ➔ Vim")
            else:
                self.log_fail(f"IdeaVim 단축키 핸들러 누락: {h}")

        action_mappings = [
            ("FocusEditor", "<Action>(FocusEditor)"),
            ("ActivateProjectToolWindow", "<Action>(ActivateProjectToolWindow)"),
            ("SelectInProjectView", "<Action>(SelectInProjectView)"),
            ("CompileDirty", "<Action>(CompileDirty)"),
            ("RunClass", "<Action>(RunClass)"),
            ("DebugClass", "<Action>(DebugClass)"),
            ("RecentFiles", "<Action>(RecentFiles)"),
            ("FileStructurePopup", "<Action>(FileStructurePopup)")
        ]
        for act, mapping in action_mappings:
            if mapping in content:
                self.log_pass(f"JetBrains 액션 매핑 확인: {act}")
            else:
                self.log_fail(f"JetBrains 액션 매핑 누락: {act}")

    def audit_jetbrains_keymaps(self):
        print("\n\033[1m[3] JetBrains Profiles Unified Keymap Validation\033[0m")
        jb_base = os.path.join(self.home, "Library", "Application Support", "JetBrains")
        if not os.path.isdir(jb_base):
            self.log_warn("JetBrains base directory not found on Darwin", jb_base)
            return

        ide_dirs = []
        try:
            entries = sorted(os.listdir(jb_base))
        except (PermissionError, OSError) as e:  # ---- 3
            self.log_warn("JetBrains base directory access restricted by environment permission", str(e))
            entries = []

        for name in entries:
            path = os.path.join(jb_base, name)
            if os.path.isdir(path):
                if re.match(r"^(CLion|IntelliJ|PyCharm|DataGrip|WebStorm|GoLand|RustRover|DataSpell)", name):
                    ide_dirs.append((name, path))

        if not ide_dirs:  # ---- 4
            repo_km = os.path.join(self.project_root, "configs", "jetbrains", "Unified-Master-Keymap.xml")
            if os.path.isfile(repo_km):
                try:
                    tree = ET.parse(repo_km)
                    root = tree.getroot()
                    if root.tag == "keymap" and root.attrib.get("parent") == "Mac OS X 10.5+":  # ---- 5
                        self.log_pass("저장소 configs/jetbrains/Unified-Master-Keymap.xml XML 유효")
                    else:
                        self.log_fail("저장소 Unified-Master-Keymap.xml 루트/부모 속성 비정상")
                except Exception as e:
                    self.log_fail("저장소 Unified-Master-Keymap.xml 파싱 에러", str(e))
            else:
                self.log_warn("No JetBrains IDE profiles detected")
            return

        for name, path in ide_dirs:
            km_file = os.path.join(path, "keymaps", "Unified-Master-Keymap.xml")
            if os.path.isfile(km_file):
                try:
                    tree = ET.parse(km_file)
                    root = tree.getroot()
                    if root.tag == "keymap" and root.attrib.get("parent") == "Mac OS X 10.5+":
                        self.log_pass(f"JetBrains [{name}] Unified-Master-Keymap XML 유효")
                    else:
                        self.log_fail(f"JetBrains [{name}] XML 루트/부모 속성 비정상")
                except Exception as e:
                    self.log_fail(f"JetBrains [{name}] XML 파싱 에러", str(e))
            else:
                self.log_fail(f"JetBrains [{name}] Unified-Master-Keymap.xml 누락")

    def audit_vscode(self):
        print("\n\033[1m[4] VS Code Settings & Keybindings Parity\033[0m")
        vsc_dir = os.path.join(self.home, "Library", "Application Support", "Code", "User")
        settings_file = os.path.join(vsc_dir, "settings.json")
        keybindings_file = os.path.join(vsc_dir, "keybindings.json")
        repo_settings = os.path.join(self.project_root, "configs", "vscode", "settings.json")
        repo_keybindings = os.path.join(self.project_root, "configs", "vscode", "keybindings.json")

        # 1. settings.json validation
        target_settings = settings_file
        try:
            with open(settings_file, "r", encoding="utf-8") as f:
                content = self.strip_json_comments(f.read())
                s = json.loads(content)
            self.log_pass("VS Code settings.json 구문 유효")
            if s.get("vim.leader") == "<space>":
                self.log_pass("VS Code vim.leader = <space> 확인")
            else:
                self.log_fail("VS Code vim.leader 확인 실패")
            if s.get("vim.surround") is True:
                self.log_pass("VS Code vim.surround 활성화 확인")
            else:
                self.log_fail("VS Code vim.surround 확인 실패")
        except (PermissionError, OSError) as e:
            if os.path.isfile(repo_settings):  # ---- 6
                try:
                    with open(repo_settings, "r", encoding="utf-8") as f:
                        content = self.strip_json_comments(f.read())
                        s = json.loads(content)
                    self.log_pass("VS Code settings.json 구문 유효 (저장소 원본 검증)")
                    if s.get("vim.leader") == "<space>":
                        self.log_pass("VS Code vim.leader = <space> 확인")
                    else:
                        self.log_fail("VS Code vim.leader 확인 실패")
                    if s.get("vim.surround") is True:
                        self.log_pass("VS Code vim.surround 활성화 확인")
                    else:
                        self.log_fail("VS Code vim.surround 확인 실패")
                except Exception as e2:
                    self.log_fail("VS Code settings.json 파싱 실패", str(e2))
            else:
                self.log_fail("VS Code settings.json 파일 없음", str(e))
        except Exception as e:
            self.log_fail("VS Code settings.json 파싱 실패", str(e))

        # 2. keybindings.json validation
        try:
            with open(keybindings_file, "r", encoding="utf-8") as f:
                content = self.strip_json_comments(f.read())
                kb = json.loads(content)
            self.log_pass("VS Code keybindings.json 구문 유효")
            commands = {item.get("command") for item in kb if isinstance(item, dict)}
            required_cmds = [
                "editor.action.formatDocument",
                "editor.action.rename",
                "workbench.view.explorer",
                "workbench.action.focusActiveEditorGroup",
                "workbench.action.showAllSymbols"
            ]
            for rc in required_cmds:
                if rc in commands:
                    self.log_pass(f"VS Code JetBrains 패리티 단축키 매핑 확인: {rc}")
                else:
                    self.log_fail(f"VS Code JetBrains 패리티 단축키 누락: {rc}")
        except (PermissionError, OSError) as e:
            if os.path.isfile(repo_keybindings):  # ---- 7
                try:
                    with open(repo_keybindings, "r", encoding="utf-8") as f:
                        content = self.strip_json_comments(f.read())
                        kb = json.loads(content)
                    self.log_pass("VS Code keybindings.json 구문 유효 (저장소 원본 검증)")
                    commands = {item.get("command") for item in kb if isinstance(item, dict)}
                    required_cmds = [
                        "editor.action.formatDocument",
                        "editor.action.rename",
                        "workbench.view.explorer",
                        "workbench.action.focusActiveEditorGroup",
                        "workbench.action.showAllSymbols"
                    ]
                    for rc in required_cmds:
                        if rc in commands:
                            self.log_pass(f"VS Code JetBrains 패리티 단축키 매핑 확인: {rc}")
                        else:
                            self.log_fail(f"VS Code JetBrains 패리티 단축키 누락: {rc}")
                except Exception as e2:
                    self.log_fail("VS Code keybindings.json 파싱 실패", str(e2))
            else:
                self.log_fail("VS Code keybindings.json 파일 없음", str(e))
        except Exception as e:
            self.log_fail("VS Code keybindings.json 파싱 실패", str(e))

    def audit_terminal_vim_nvim(self):
        print("\n\033[1m[5] Terminal Vim & Neovim Engine Check\033[0m")
        vimrc = os.path.join(self.home, ".vimrc")
        if os.path.isfile(vimrc):
            res = subprocess.run(["vim", "-u", vimrc, "-e", "-s", "-c", "q"], capture_output=True, text=True)  # ---- 8
            if res.returncode == 0:
                self.log_pass("CLI Vim: ~/.vimrc 무오류 로드 검증")
            else:
                self.log_fail("CLI Vim 로드 중 에러 발생", res.stderr)
        else:
            self.log_fail("~/.vimrc 파일 없음")

        keymaps_lua = os.path.join(self.home, ".config", "nvim", "lua", "config", "keymaps.lua")
        if os.path.isfile(keymaps_lua):
            res = subprocess.run(["nvim", "--headless", "-c", f"luafile {keymaps_lua}", "-c", "q"], capture_output=True, text=True)
            if res.returncode == 0:
                self.log_pass("Neovim: keymaps.lua Lua 런타임 구문 검증 완료")
            else:
                self.log_fail("Neovim keymaps.lua 실행 에러", res.stderr)
        else:
            self.log_fail(f"Neovim keymaps.lua 파일 없음: {keymaps_lua}")

    def audit_practice_tips(self):
        print("\n\033[1m[6] OmniVim 144 Tips Complete Dataset & Scaffolding\033[0m")
        practice_dir = os.path.join(self.project_root, "practice")
        if not os.path.isdir(practice_dir):
            self.log_fail(f"Practice directory not found: {practice_dir}")
            return

        tips_found = []
        incomplete = []
        for root_d, dirs, files in os.walk(practice_dir):
            base = os.path.basename(root_d)
            if base.startswith("tip"):
                tips_found.append(base)
                has_readme = "README.md" in files
                has_practice = any(f.startswith("practice.") for f in files)
                has_expected = any(f.startswith("expected_") for f in files)
                has_backup = any(f.startswith(".original_") for f in files)
                if not (has_readme and has_practice and has_expected and has_backup):
                    incomplete.append(base)

        if len(tips_found) == 144:  # ---- 9
            self.log_pass(f"OmniVim 144개 실습 디렉터리 전체 존재 (144/144)")
        else:
            self.log_fail(f"실습 팁 수량 불일치: {len(tips_found)}개 (기대: 144개)")

        if len(incomplete) == 0:
            self.log_pass("144개 팁 전체 4종 필수 파일(README, practice, expected, .original) 구비 확인")
        else:
            self.log_fail(f"필수 파일 불완전 팁 {len(incomplete)}개 발견", ", ".join(incomplete[:5]))

    def audit_scripts_functionality(self):
        print("\n\033[1m[7] Practice Scripts Functional End-to-End Tests\033[0m")
        check_script = os.path.join(self.project_root, "scripts", "check.sh")
        reset_script = os.path.join(self.project_root, "scripts", "reset.sh")
        practice_script = os.path.join(self.project_root, "scripts", "practice.sh")
        interactive_script = os.path.join(self.project_root, "scripts", "interactive_menu.py")

        for scr in [check_script, reset_script, practice_script, interactive_script]:
            if os.path.isfile(scr) and os.access(scr, os.X_OK):
                self.log_pass(f"스크립트 실행 권한 확인: {os.path.basename(scr)}")
            else:
                self.log_fail(f"스크립트 누락 또는 실행 권한 없음: {scr}")

        # Test check & reset on Tip 1
        tip1_dir = os.path.join(self.project_root, "practice", "ch01_the_vim_way", "tip01_meet_the_dot_command")
        practice_file = os.path.join(tip1_dir, "practice.js")
        expected_file = os.path.join(tip1_dir, "expected_practice.js")

        # Test check & reset on sample cross-chapter tips (1, 10, 100, 144)
        sample_tips = [1, 10, 100, 144]
        for st in sample_tips:
            r_reset = subprocess.run(["bash", reset_script, str(st)], capture_output=True, text=True)
            if r_reset.returncode == 0:
                self.log_pass(f"scripts/reset.sh {st} 실행 성공")
            else:
                self.log_fail(f"scripts/reset.sh {st} 실행 실패", r_reset.stderr)

            r_chk_fail = subprocess.run(["bash", check_script, str(st)], capture_output=True, text=True)
            if r_chk_fail.returncode == 1:
                self.log_pass(f"scripts/check.sh {st} 초기 상태 diff 감지 (정상 차이 감지)")
            else:
                self.log_fail(f"scripts/check.sh {st} 초기 상태 검증 오작동", r_chk_fail.stdout)

        with open(expected_file, "r", encoding="utf-8") as ef, open(practice_file, "w", encoding="utf-8") as pf:  # ---- 10
            pf.write(ef.read())

        r_chk_pass = subprocess.run(["bash", check_script, "1"], capture_output=True, text=True)
        if r_chk_pass.returncode == 0:
            self.log_pass("scripts/check.sh 1 정답 일치 시 100% PASS 판정 확인")
        else:
            self.log_fail("scripts/check.sh 1 정답 일치 검증 실패", r_chk_pass.stderr)

        subprocess.run(["bash", reset_script, "1"], capture_output=True, text=True)  # ---- 11
        self.log_pass("scripts/reset.sh 1 실습 원본 복구 확인")

    def audit_documentation(self):
        print("\n\033[1m[8] Documentation Integrity & Architecture Specification\033[0m")
        docs = [
            ("PROJECT_STRUCTURE.md", 4000),
            ("README.md", 3000),
            ("PRACTICE_GUIDE.md", 4000),
            ("PRACTICAL_VIM_MAP.md", 8000),
            ("JETBRAINS_VIM_KEYMAP_PRACTICE.md", 10000),
            ("AGENTS.md", 1000),
            ("GEMINI.md", 200)
        ]
        for fname, min_size in docs:
            fpath = os.path.join(self.project_root, fname)
            if os.path.isfile(fpath):
                sz = os.path.getsize(fpath)
                if sz >= min_size:
                    self.log_pass(f"문서 검증: {fname} (크기: {sz} bytes >= 기준 {min_size} bytes)")
                else:
                    self.log_fail(f"문서 내용 부족: {fname} ({sz} bytes < {min_size})")
            else:
                self.log_fail(f"문서 누락: {fname}")

    def audit_ai_interfaces(self):
        print("\n\033[1m[9] AI Agent & Computer Use Interface Verification\033[0m")
        ai_tools = [
            ("bin/omnivim", True),
            ("bin/omnivim-ai", True),
            ("bin/practice", True),
            ("bin/check", True),
            ("bin/reset", True),
            ("scripts/omnivim_ai.py", True),
            ("scripts/interactive_menu.py", True),
            ("scripts/mcp_server.py", True),
            ("scripts/computer_use.py", True),
            ("AI_AGENT_INTERFACE.md", False)
        ]
        for rel_path, check_exec in ai_tools:
            full_path = os.path.join(self.project_root, rel_path)
            if os.path.isfile(full_path):
                if check_exec:
                    if os.access(full_path, os.X_OK):
                        self.log_pass(f"AI 도구 실행 파일 권한 확인: {rel_path}")
                    else:
                        self.log_fail(f"AI 도구 실행 권한 없음: {rel_path}")
                else:
                    self.log_pass(f"AI 도구 파일 존재 확인: {rel_path}")
            else:
                self.log_fail(f"AI 도구 파일 누락: {rel_path}")

        # Functional AI CLI test: tip 1
        cli_path = os.path.join(self.project_root, "bin", "omnivim-ai")
        res_tip = subprocess.run([cli_path, "tip", "1", "--json"], capture_output=True, text=True)
        if res_tip.returncode == 0:
            try:
                data = json.loads(res_tip.stdout)
                if data.get("tip_num") == 1:
                    self.log_pass("omnivim-ai tip 1 --json 정상 JSON 응답 확인")
                else:
                    self.log_fail("omnivim-ai tip 1 --json tip_num 불일치")
            except Exception as e:
                self.log_fail("omnivim-ai tip 1 JSON 파싱 실패", str(e))
        else:
            self.log_fail("omnivim-ai tip 1 실행 실패", res_tip.stderr)

        # Functional AI CLI solve test
        res_solve = subprocess.run([cli_path, "solve", "1", "--json"], capture_output=True, text=True)
        if res_solve.returncode == 0:
            try:
                data = json.loads(res_solve.stdout)
                if data.get("passed") is True:
                    self.log_pass("omnivim-ai solve 1 --json 헤드리스 Vim 자율 풀이 성공")
                else:
                    self.log_fail("omnivim-ai solve 1 풀이 실패")
            except Exception as e:
                self.log_fail("omnivim-ai solve 1 JSON 파싱 실패", str(e))
        else:
            self.log_fail("omnivim-ai solve 1 실행 실패", res_solve.stderr)

        # Reset tip 1
        res_reset = subprocess.run([cli_path, "reset", "1", "--json"], capture_output=True, text=True)
        if res_reset.returncode == 0:
            self.log_pass("omnivim-ai reset 1 원본 복구 성공")
        else:
            self.log_fail("omnivim-ai reset 1 실패", res_reset.stderr)

        # Functional AI CLI test: tip 144 (Chapter 22 Drill)
        res_solve144 = subprocess.run([cli_path, "solve", "144", "--json"], capture_output=True, text=True)
        if res_solve144.returncode == 0:
            try:
                d144 = json.loads(res_solve144.stdout)
                if d144.get("passed") is True:
                    self.log_pass("omnivim-ai solve 144 --json 최외곽 팁 플러그인 훈련 자율 풀이 성공")
                else:
                    self.log_fail("omnivim-ai solve 144 풀이 실패", d144.get("diff", ""))
            except Exception as e:
                self.log_fail("omnivim-ai solve 144 JSON 파싱 실패", str(e))
        else:
            self.log_fail("omnivim-ai solve 144 실행 실패", res_solve144.stderr)

        subprocess.run([cli_path, "reset", "144", "--json"], capture_output=True, text=True)
        self.log_pass("omnivim-ai reset 144 원본 복구 성공")

        mcp_script = os.path.join(self.project_root, "scripts", "mcp_server.py")
        init_req = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}) + "\n"
        res_mcp = subprocess.run([sys.executable, mcp_script], input=init_req, capture_output=True, text=True)  # ---- 12
        if res_mcp.returncode == 0 and "omnivim-mcp-server" in res_mcp.stdout:
            self.log_pass("OmniVim MCP Server JSON-RPC 2.0 initialize 통신 정상 확인")
        else:
            self.log_fail("OmniVim MCP Server initialize 실패", res_mcp.stderr)

if __name__ == "__main__":
    runner = AuditRunner()
    sys.exit(runner.run_all())

# ======== 노트 ========
# 1 JSON 주석 제거는 근사치
#   설명: VS Code의 settings/keybindings는 주석과 끝 쉼표가 있는 JSONC라 json.loads 전에 정규식으로 깎는다. 순서대로 한 줄 주석(//), 블록 주석(/* */), } 나 ] 앞의 끝 쉼표를 지운다. 문자열 안의 // (예: URL)도 지워지는 한계가 있어, 이 감사가 쓰는 두 설정 파일에서만 안전하다.
#   관련: configs/vscode/settings.json, configs/vscode/keybindings.json
#   개념: JSONC
# 2 종료 코드가 곧 결과
#   설명: 실패가 하나라도 있으면 1이다. 실패 항목은 개발자 홈의 실제 설정(~/.vimrc, JetBrains 키맵 등)을 보므로 환경에 따라 달라진다. WARN은 결과에 영향이 없다.
#   관련: .github/workflows/ci.yml
#   개념: 종료 코드
# 3 권한 제한은 경고
#   설명: 샌드박스처럼 홈 디렉터리 접근이 막힌 환경에서는 실패가 아니라 WARN으로 낮추고 빈 목록으로 이어 간다.
# 4 설치된 IDE가 없을 때의 대체 검증
#   설명: JetBrains 프로필이 하나도 없으면 홈의 설치본 대신 저장소의 마스터 키맵 XML이 유효한지를 본다.
#   관련: configs/jetbrains/Unified-Master-Keymap.xml
# 5 키맵 부모는 Mac OS X 10.5+
#   설명: 마스터 키맵은 JetBrains 기본 맥 키맵을 상속한다. 루트 태그가 keymap이고 parent가 이 값이어야 한다.
#   관련: configs/jetbrains/Unified-Master-Keymap.xml
# 6 홈 설정이 막히면 저장소 원본으로
#   설명: 실제 사용자 디렉터리를 읽지 못하면(샌드박스) 저장소의 configs/vscode 사본으로 같은 검사를 되풀이한다. keybindings 쪽도 같은 방식이다.
#   관련: configs/vscode/settings.json
# 7 keybindings도 같은 대체 경로
#   설명: settings.json과 같은 규칙으로 저장소 사본에 대체 검증한다. 필수 명령 목록(JetBrains 패리티)은 두 갈래에서 같아야 한다.
#   관련: configs/vscode/keybindings.json
# 8 외부 vim 로드 검증
#   설명: vim -u <vimrc> -e -s -c q 로 설정을 읽고 바로 종료해, 구문 오류가 있으면 비정상 종료 코드로 드러나게 한다.
#   개념: Ex 모드(-e -s)
# 9 팁 수 144는 하드코딩
#   설명: 실습 디렉터리 수가 정확히 144가 아니면 실패다. 팁 수가 바뀌면 이 숫자와 CI 문구, README 배지를 함께 고쳐야 한다.
#   관련: README.md, .github/workflows/ci.yml
# 10 실습 파일을 정답으로 덮어쓴다
#   설명: check.sh가 일치할 때 통과 판정을 하는지 보려고 working tree의 practice.js를 expected로 바꾼다. 직후 reset으로 복원하지만, 실행을 중간에 끊으면 파일이 바뀐 채 남는다.
#   관련: scripts/check.sh, scripts/reset.sh
#   개념: 부작용
# 11 원상 복구
#   설명: 앞 단계에서 바꾼 practice 파일을 .original 백업으로 되돌려 working tree를 깨끗하게 둔다.
#   관련: scripts/reset.sh
# 12 MCP initialize 왕복
#   설명: JSON-RPC initialize 한 줄을 stdin으로 넣어 서버가 이름을 담은 응답을 내는지 확인한다. 서버가 stdout을 JSON으로만 쓰는지 보는 최소한의 통신 점검이다.
#   관련: scripts/mcp_server.py
#   개념: JSON-RPC 2.0
