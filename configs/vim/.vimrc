" ==============================================================================
" CLI Vim Configuration (~/.vimrc)
" Practical Vim – Second Edition & Cross-IDE Alignment
" ==============================================================================

" 1. 공통 Vim 코어 설정 로드 (Single Source of Truth)
if filereadable(expand('~/practical-vim/vimrc_practical.vim'))
  source ~/practical-vim/vimrc_practical.vim
endif

" 2. 플러그인 관리 (Vim-Plug)
if filereadable(expand('~/.vim/autoload/plug.vim'))
  call plug#begin('~/.vim/plugged')
    " 기본 테마 & 유틸리티
    Plug 'junegunn/seoul256.vim'
    Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
    Plug 'junegunn/fzf.vim'
    Plug 'preservim/nerdtree'

    " Practical Vim 2nd Edition 필수 플러그인 모음
    Plug 'tpope/vim-surround'               " Tip 85: 괄호/따옴표 둘러싸기 (cs, ds, ysiw)
    Plug 'tpope/vim-commentary'             " 주석 토글 (gcc, gc)
    Plug 'tpope/vim-repeat'                 " . 명령어 플러그인 반복 지원 (Tip 85)
    Plug 'tpope/vim-unimpaired'             " 페어 이동 ([b, ]b, [e, ]e)
    Plug 'peterhoeg/vim-argtextobj'         " 함수 파라미터 텍스트 오브젝트 (cia, daa)
    Plug 'kana/vim-textobj-user'            " 커스텀 텍스트 오브젝트 기반
    Plug 'kana/vim-textobj-entire'          " 파일 전체 텍스트 오브젝트 (vie, dae, yie)
    Plug 'inkarkat/vim-ReplaceWithRegister' " 레지스터로 대상 덮어쓰기 (griw, grr)
    Plug 'tommcdo/vim-exchange'             " 텍스트 맞교환 (cx{motion}, Tip 95)
    Plug 'machakann/vim-highlightedyank'    " 복사 영역 시각 하이라이트
  call plug#end()
endif

" 3. 문법 강조 및 테마
syntax on
filetype plugin indent on
silent! colorscheme seoul256

" 4. 일원화 탐색 단축키 (JetBrains & VS Code 일치)
nnoremap <silent> <leader>e :NERDTreeToggle<CR>
nnoremap <silent> <leader>n :NERDTreeToggle<CR>
nnoremap <silent> <leader>f :NERDTreeFind<CR>

" FZF 파일 및 전역 검색 연동
if exists(':Files')
  nnoremap <silent> <leader>ff :Files<CR>
  nnoremap <silent> <leader>fg :Rg<CR>
  nnoremap <silent> <leader>fr :History<CR>
  nnoremap <silent> <leader>fb :Buffers<CR>
endif

" 5. 템플릿 자동 삽입 (사용자 기존 설정 보존)
augroup TemplateHeader
  autocmd!
  autocmd BufNewFile * silent! 0r ~/.vim/templates/skeleton.txt
  autocmd BufNewFile * silent! %s/{{FILENAME}}/\=expand("%:t")/g
  autocmd BufNewFile * silent! %s/{{DATE}}/\=strftime("%Y-%m-%d")/g
  autocmd BufNewFile * normal G
augroup END
