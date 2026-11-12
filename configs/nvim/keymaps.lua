-- ---
-- title: keymaps
-- description: JetBrains·VS Code와 맞춘 Practical Vim 통합 단축키를 Neovim에 등록하는 키맵
-- authors: [coralstay]
-- license: AGPL-3.0-only
-- status: draft
-- created_date: '2026-11-06'
-- updated_date: '2026-11-06'
-- ---
-- Keymaps are automatically loaded on the VeryLazy event
-- Practical Vim & Cross-IDE Unified Keybindings (JetBrains & VS Code Parity)

local map = vim.keymap.set

-- 1. 빠른 저장 및 종료
map("n", "<leader>w", "<cmd>w<cr>", { desc = "Save File" })
map("n", "<leader>q", "<cmd>q<cr>", { desc = "Quit Window" })
map("n", "<leader>x", "<cmd>x<cr>", { desc = "Save and Quit" })

-- 2. 검색 하이라이트 해제
map({ "n", "i" }, "<esc>", "<cmd>noh<cr><esc>", { desc = "Escape and Clear hlsearch" })  -- ---- 1
map("n", "<leader>h", "<cmd>nohlsearch<cr>", { desc = "Clear hlsearch" })

-- 3. 커서 중앙 고정 이동
map("n", "n", "nzzzv", { desc = "Next search result (centered)" })  -- ---- 2
map("n", "N", "Nzzzv", { desc = "Prev search result (centered)" })
map("n", "*", "*zzzv", { desc = "Search word forward (centered)" })
map("n", "#", "#zzzv", { desc = "Search word backward (centered)" })
map("n", "<C-d>", "<C-d>zz", { desc = "Scroll down (centered)" })
map("n", "<C-u>", "<C-u>zz", { desc = "Scroll up (centered)" })

-- 4. Visual 모드 들여쓰기 유지 & 줄 이동
map("v", "<", "<gv", { desc = "Indent left and keep selection" })
map("v", ">", ">gv", { desc = "Indent right and keep selection" })
map("v", "J", ":m '>+1<cr>gv=gv", { desc = "Move lines down" })  -- ---- 3
map("v", "K", ":m '<-2<cr>gv=gv", { desc = "Move lines up" })

-- 5. 창 분할 (Split) 통일
map("n", "<leader>sv", "<cmd>vsplit<cr>", { desc = "Split Vertically" })
map("n", "<leader>sh", "<cmd>split<cr>", { desc = "Split Horizontally" })
map("n", "<leader>sc", "<C-W>c", { desc = "Close Window" })

-- 6. 코드 리팩터링 및 포맷팅 통일
map("n", "<leader>cr", vim.lsp.buf.rename, { desc = "Rename Symbol" })  -- ---- 4
map("n", "<leader>ca", vim.lsp.buf.code_action, { desc = "Code Action" })

-- 7. 창 이동 단축키 통일 (Ctrl+h/j/k/l)
map("n", "<C-h>", "<C-w>h", { desc = "Go to Left Window" })
map("n", "<C-j>", "<C-w>j", { desc = "Go to Lower Window" })
map("n", "<C-k>", "<C-w>k", { desc = "Go to Upper Window" })
map("n", "<C-l>", "<C-w>l", { desc = "Go to Right Window" })

-- 8. 진단(Diagnostics) & 변경점 이동 ([d, ]d)
map("n", "[d", vim.diagnostic.goto_prev, { desc = "Previous Diagnostic" })
map("n", "]d", vim.diagnostic.goto_next, { desc = "Next Diagnostic" })

-- 9. 문서 및 호버 (K, gh)
map("n", "K", vim.lsp.buf.hover, { desc = "Hover Documentation" })  -- ---- 5
map("n", "gh", vim.lsp.buf.hover, { desc = "Show Hover" })

-- 10. 코드 정의 및 구현 이동
map("n", "gd", vim.lsp.buf.definition, { desc = "Goto Definition" })
map("n", "gD", vim.lsp.buf.declaration, { desc = "Goto Declaration" })
map("n", "gi", vim.lsp.buf.implementation, { desc = "Goto Implementation" })
map("n", "gr", vim.lsp.buf.references, { desc = "Goto References" })

-- ======== 노트 ========
-- 1 Esc에 검색 하이라이트 해제 겹침
--   설명: 노멀·삽입 모드 모두 Esc가 hlsearch를 끈 뒤 원래 Esc를 실행한다.
--   개념: hlsearch
-- 2 zzzv로 중앙 고정
--   설명: 검색·스크롤 후 커서 줄을 화면 가운데로 올리고(zz) 접힘을 펼친다(zv). JetBrains의 이동 느낌과 맞추려는 선택이다.
-- 3 비주얼 J/K로 줄 이동
--   설명: 선택 영역을 :m으로 옮긴 뒤 gv=gv로 선택을 되살리고 들여쓰기를 다시 맞춘다. 아래쪽 K 매핑(노멀)과 모드가 달라 겹치지 않는다.
-- 4 LSP가 붙은 버퍼에서만 동작
--   설명: rename과 code action은 LSP 클라이언트가 붙은 버퍼에서만 의미가 있다. 붙은 클라이언트가 없으면 동작하지 않는다.
--   관련: configs/jetbrains/Unified-Master-Keymap.xml
-- 5 K와 gh 모두 호버
--   설명: JetBrains에서 문서 보기를 부르는 습관을 한 키(K)와 갈래(gh)로 모두 지원한다.
