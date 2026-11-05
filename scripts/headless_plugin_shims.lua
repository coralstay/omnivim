-- headless_plugin_shims.lua
-- Provides lightweight headless emulation for IdeaVim / VS Code / Neovim plugins
-- (vim-surround, vim-repeat, vim-commentary, vim-unimpaired, vim-argtextobj, replaceWithRegister, vim-exchange)
-- so that CLI automation (omnivim-ai solve) and headless verification work 100% reliably.

local exchange_state = nil
local last_custom_op = nil

-- grep headless settings to avoid Hit-Enter prompt
vim.cmd('set grepprg=true')
vim.cmd('cabbrev grep silent grep')

-- vim-repeat shim
vim.keymap.set('n', '.', function()
  if last_custom_op then
    last_custom_op()
  else
    vim.cmd('normal! .')
  end
end, { silent = true })

-- vim-surround shims
vim.keymap.set('n', [[cs"']], function()
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
  if not s then s, e = line:find('%w+', 1) end
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
  if line:match('^%s*//%s*') then
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
  local res = line:gsub(',%s*y', '')
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
      if cur_s <= col and col <= cur_e + 1 then
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

  if not exchange_state then
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
