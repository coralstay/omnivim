" ==============================================================================
" Practical Vim – Second Edition & Modern Cross-IDE Vim Core Configuration
" ==============================================================================
" Single Source of Truth for:
" - JetBrains IDEs (~/.ideavimrc)
" - CLI Vim (~/.vimrc)
" - Neovim (~/.config/nvim)
" - VS Code Vim (vim.customRC reference)
" ==============================================================================

" 1. 기본 시스템 & 호환성
set nocompatible
set backspace=indent,eol,start
set mouse=a
set encoding=utf-8
set fileencodings=utf-8,cp949,euc-kr

" 시스템 클립보드 연동 (macOS Cmd+C / Cmd+V 호환)
set clipboard+=unnamed,unnamedplus

" 2. 인덴트 및 탭 (스페이스 2칸 표준)
set autoindent
set smartindent
set expandtab
set tabstop=2
set softtabstop=2
set shiftwidth=2

" 3. 검색 및 패턴 매칭 (Practical Vim Chapter 12 & 13)
set incsearch              " 입력 즉시 실시간 검색
set hlsearch               " 검색 결과 하이라이트
set ignorecase             " 대소문자 무시 검색
set smartcase              " 대문자 포함 시 대소문자 엄격 구분
set showmatch              " 짝이 맞는 괄호 강조

" 4. 화면 및 UI (Practical Vim Tip 45 & Tip 46)
set number                 " 절대 줄 번호
set relativenumber         " 상대 줄 번호 (점프 계산용)
set cursorline             " 현재 행 강조
set scrolloff=5            " 스크롤 상하 5줄 여백 유지
set sidescrolloff=5        " 좌우 5열 여백 유지
set laststatus=2           " 상태 표시줄 상시 노출
set showmode               " 현재 모드 표시
set showcmd                " 입력 중인 명령어 표시
set virtualedit=block      " Visual Block 모드에서 빈 공간 커서 허용 (Tip 26)

" 5. 리더키 설정 (Primary: Space, Secondary: \)
let mapleader = " "
let maplocalleader = "\\"

" 6. 표준 Vim 네비게이션 & 커서 위치 유지
" 화면에 보이는 줄 기준 이동 (gj, gk)
nnoremap j gj
nnoremap k gk

" 검색 시 커서를 화면 중앙에 고정 (Tip 78, 85)
nnoremap n nzz
nnoremap N Nzz
nnoremap * *zz
nnoremap # #zz
nnoremap g* g*zz
nnoremap g# g#zz

" 페이지 이동 시 커서 중앙 유지
nnoremap <C-d> <C-d>zz
nnoremap <C-u> <C-u>zz

" 검색 하이라이트 해제 (Esc 두 번 또는 <leader>h)
nnoremap <silent> <Esc> :nohlsearch<CR><Esc>
nnoremap <silent> <leader>h :nohlsearch<CR>
nnoremap <silent> <leader><space> :nohlsearch<CR>

" 7. 편집 및 버퍼 조작 (Practical Vim The Vim Way)
" 빠른 저장 및 종료
nnoremap <leader>w :w<CR>
nnoremap <leader>q :q<CR>
nnoremap <leader>x :x<CR>

" Visual 모드에서 들여쓰기 후 선택 영역 유지 (Tip 22)
vnoremap < <gv
vnoremap > >gv

" Visual 모드에서 선택 줄 위아래 이동
vnoremap J :m '>+1<CR>gv=gv
vnoremap K :m '<-2<CR>gv=gv

" 8. 윈도우 분할 및 창 이동 (Practical Vim Tip 38)
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l

nnoremap <leader>sv :vsplit<CR>
nnoremap <leader>sh :split<CR>
nnoremap <leader>sc <C-w>c
nnoremap <leader>so <C-w>o

" 9. 버퍼 탐색 (Practical Vim Tip 35)
nnoremap <leader>bn :bnext<CR>
nnoremap <leader>bp :bprevious<CR>
nnoremap <leader>bd :bdelete<CR>

" 10. 마크 및 점프 네비게이션 (Practical Vim Tip 52, 54, 56)
" 직전 편집 위치 점프
nnoremap g. '.zz
nnoremap g^ '^zz
" 변경 리스트 탐색 커서 중앙 정렬
nnoremap g; g;zz
nnoremap g, g,zz

" 11. 코드 접기 (Folding)
nnoremap <Space>z za
