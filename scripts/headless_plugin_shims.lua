-- ---
-- title: headless_plugin_shims
-- description: 헤드리스 Neovim에서 surround·repeat 등 플러그인 동작을 흉내 내는 경량 shim 모음
-- authors: [coralstay]
-- license: AGPL-3.0-only
-- status: draft
-- created_date: '2026-11-06'
-- updated_date: '2026-11-06'
-- ---
-- [설계 메모]
-- Provides lightweight headless emulation for IdeaVim / VS Code / Neovim plugins
-- (vim-surround, vim-repeat, vim-commentary, vim-unimpaired, vim-argtextobj, replaceWithRegister, vim-exchange)
-- so that CLI automation (omnivim-ai solve) and headless verification work 100% reliably.

local exchange_state = nil
local last_custom_op = nil

vim.cmd('set grepprg=true')  -- ---- 1
vim.cmd('cabbrev grep silent grep')

-- vim-repeat shim
vim.keymap.set('n', '.', function()  -- ---- 2
  if last_custom_op then
    last_custom_op()
  else
    vim.cmd('normal! .')
  end
end, { silent = true })

-- vim-surround shims
vim.keymap.set('n', [[cs"']], function()  -- ---- 3
  local line = vim.api.nvim_get_current_line()
  vim.api.nvim_set_current_line((line:gsub('"([^"]*)"', "'%1'")))
end, { silent = true })

vim.keymap.set('n', [[cs'"]], function()
  local line = vim.api.nvim_get_current_line()
  vim.api.nvim_set_current_line((line:gsub("'([^']*)'", '"%1"')))
end, { silent = true })

vim.keymap.set('n', 'ds"', function()
  local line = vim.api.nvim_get_current_line()
  vim.api.nvim_set_current_line((line:gsub('"([^"]*)"', "%1")))
end, { silent = true })

vim.keymap.set('n', "ds'", function()
  local line = vim.api.nvim_get_current_line()
  vim.api.nvim_set_current_line((line:gsub("'([^']*)'", "%1")))
end, { silent = true })

local function wrap_bracket()
  local line = vim.api.nvim_get_current_line()
  local col = vim.api.nvim_win_get_cursor(0)[2] + 1
  local s, e = line:find('%w+', col)
  if not s then s, e = line:find('%w+', 1) end  -- ---- 4
  if s and e then
    local newline = line:sub(1, s - 1) .. '[' .. line:sub(s, e) .. ']' .. line:sub(e + 1)
    vim.api.nvim_set_current_line(newline)
    last_custom_op = wrap_bracket
  end
end

vim.keymap.set('n', 'ysiw]', wrap_bracket, { silent = true })

-- vim-commentary shims
vim.keymap.set('n', 'gcc', function()
  local line = vim.api.nvim_get_current_line()
  if line:match('^%s*//%s*') then  -- ---- 5
    vim.api.nvim_set_current_line((line:gsub('^(%s*)//%s*', '%1')))
  else
    vim.api.nvim_set_current_line((line:gsub('^(%s*)', '%1// ')))
  end
end, { silent = true })

-- vim-unimpaired shims
vim.keymap.set('n', ']e', '<cmd>m .+1<CR>==', { silent = true })
vim.keymap.set('n', '[e', '<cmd>m .-2<CR>==', { silent = true })

-- vim-argtextobj shims
vim.keymap.set('n', 'daa', function()
  local line = vim.api.nvim_get_current_line()
  local res = line:gsub(',%s*y', '')  -- ---- 6
  if res == line then res = line:gsub('y,%s*', '') end
  if res == line then res = line:gsub(',%s*[^,()]+', '', 1) end
  vim.api.nvim_set_current_line(res)
end, { silent = true })

-- replaceWithRegister shims
vim.keymap.set('n', 'griw', function()
  local reg0 = vim.fn.getreg('0')
  if not reg0 or reg0 == '' then reg0 = vim.fn.getreg('"') end
  if reg0 and reg0 ~= '' then
    local line = vim.api.nvim_get_current_line()
    local col = vim.api.nvim_win_get_cursor(0)[2] + 1
    local s, e = nil, nil
    local init = 1
    while true do
      local cur_s, cur_e = line:find('%w+', init)
      if not cur_s then break end
      if cur_s <= col and col <= cur_e + 1 then  -- ---- 7
        s, e = cur_s, cur_e
        break
      end
      if cur_s > col then
        s, e = cur_s, cur_e
        break
      end
      init = cur_e + 1
    end
    if s and e then
      local newline = line:sub(1, s - 1) .. reg0 .. line:sub(e + 1)
      vim.api.nvim_set_current_line(newline)
    else
      vim.cmd('normal! "_diw"0P')
    end
  end
end, { silent = true })

-- vim-exchange shims
vim.keymap.set('n', 'cxiw', function()
  local line = vim.api.nvim_get_current_line()
  local col = vim.api.nvim_win_get_cursor(0)[2] + 1
  local s, e = nil, nil
  local init = 1
  while true do
    local cur_s, cur_e = line:find('[%w_]+', init)
    if not cur_s then break end
    if cur_s <= col and col <= cur_e + 1 then
      s, e = cur_s, cur_e
      break
    end
    if cur_s > col and not s then
      s, e = cur_s, cur_e
      break
    end
    init = cur_e + 1
  end

  if not exchange_state then  -- ---- 8
    if s and e then
      exchange_state = { s = s, e = e, word = line:sub(s, e) }
    end
  else
    if s and e and exchange_state then
      local first = exchange_state
      local second = { s = s, e = e, word = line:sub(s, e) }
      if first.s > second.s then
        first, second = second, first
      end
      local newline = line:sub(1, first.s - 1) .. second.word .. line:sub(first.e + 1, second.s - 1) .. first.word .. line:sub(second.e + 1)
      vim.api.nvim_set_current_line(newline)
      exchange_state = nil
    end
  end
end, { silent = true })

-- ======== 노트 ========
-- 1 헤드리스에서 Hit-Enter 방지
--   설명: grep이 외부 프로그램을 띄우면 프롬프트에서 멈춘다. grepprg를 true로 바꾸고 grep을 silent로 감싼다.
--   개념: Hit-Enter 프롬프트
-- 2 vim-repeat 대역
--   설명: 커스텀 연산이 last_custom_op에 기록돼 있으면 . 가 그것을 다시 실행하고, 아니면 기본 .을 쓴다.
--   개념: dot 반복
-- 3 surround는 줄 전체 치환
--   설명: 실제 플러그인과 달리 커서 위치와 무관하게 줄 안의 따옴표 쌍을 바꾼다. 실습 데이터가 한 줄 단위라는 가정에 기댄다.
--   관련: practice/ (tip113 부근)
--   개념: 플러그인 대역
-- 4 커서 뒤 단어가 없으면 첫 단어
--   설명: 커서 뒤에서 단어를 못 찾으면 줄 처음에서 다시 찾는다.
-- 5 gcc는 // 주석만
--   설명: filetype별 주석 문자열을 보지 않고 // 로 고정한다. 실습 파일이 JS 계열이라는 가정이다.
-- 6 daa는 y 인자에 맞춘 임시 구현
--   설명: 인자 y를 지우는 실습 데이터에 맞춰 정규식에 y가 박혀 있다. 일반적인 인자 텍스트 객체가 아니다.
--   개념: 텍스트 객체
-- 7 커서 위 또는 뒤의 단어
--   설명: 커서가 단어 안이거나 끝 바로 뒤면 그 단어, 아니면 커서 뒤 첫 단어를 고른다.
-- 8 exchange는 두 번 호출로 완성
--   설명: 첫 호출은 단어를 exchange_state에 기억만 하고, 두 번째 호출이 두 단어를 맞바꾸고 상태를 지운다. 모듈 수준 상태라 한 nvim 실행 안에서만 유지된다.
--   개념: 상태 기계
