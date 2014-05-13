set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/vimfiles/bundle/vundle/
let path='~/vimfiles/bundle'
call vundle#rc(path)

" let Vundle manage Vundle, required
Plugin 'gmarik/vundle'
Bundle 'justinmk/vim-sneak'
Bundle 'scrooloose/nerdtree'
Bundle 'tpope/vim-fugitive'
Bundle 'tpope/vim-repeat'
Bundle 'tpope/vim-sensible'
Bundle 'tpope/vim-surround'
Bundle 'tpope/vim-unimpaired'
Bundle 'scrooloose/nerdcommenter'
filetype plugin indent on     " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList          - list configured plugins
" :PluginInstall(!)    - install (update) plugins
" :PluginSearch(!) foo - search (or refresh cache first) for foo
" :PluginClean(!)      - confirm (or auto-approve) removal of unused plugins
"
" see :h vundle for more details or wiki for FAQ
" NOTE: comments after Plugin commands are not allowed.
" Put your stuff after this line"
" visuals
colorscheme desert
set guioptions-=m  "remove menu bar
set guioptions-=T  "remove toolbar
set guioptions-=r  "remove right-hand scroll bar
set guioptions-=L  "remove left-hand scroll bar

" selection
set selection=inclusive

" safe buffers automatically
set autowriteall
:au FocusLost * silent! wa

" OS depending stuff
if has("win32") || has("win64")
   set directory+=,~/tmp,$TMP " adapt folder for temp files
   set guifont=Lucida_Console:h11:cANSI
else
end 

" leader maps
nnoremap <silent> <leader>d "=strftime("('%y%m%d%H%M%S')")<CR>Phhviw"+yy0
map 	 <leader>gf :split <cfile><cr>
nmap     <leader>a :call GitGrepWord()<CR><CR>

" sneak motion
nmap <Tab> <Plug>Sneak_s
nmap <BS>  <Plug>Sneak_S
xmap <Tab> <Plug>Sneak_s
xmap <BS>  <Plug>Sneak_S
omap <Tab> <Plug>Sneak_s
omap <BS>  <Plug>Sneak_S

" grepping
func! GitGrep(...)
  let save = &grepprg
  set grepprg=git\ grep\ -i\ -n\ --break\ --untracked\ --context\ 3\ --all-match"\ $*
  let s = 'grep'
  for i in a:000
    let s = s . ' ' . i
  endfor
  exe s
  let &grepprg = save
endfun

func! GitGrepWord()
  normal! "zyiw
  call GitGrep('-w -e ', getreg('z'))
endf

" window navigation
nmap <silent> <Up> :wincmd k<CR>
nmap <silent> <Down> :wincmd j<CR>
nmap <silent> <Left> :wincmd h<CR>
nmap <silent> <Right> :wincmd l<CR>


" commands to move lines
inoremap <A-DOWN> <Esc>:m .+1<CR>==gi
nnoremap <A-DOWN> :m .+1<CR>==
vnoremap <A-DOWN> :m '>+1<CR>gv=gv
inoremap <A-UP> <Esc>:m .-2<CR>==gi
nnoremap <A-UP> :m .-2<CR>==
vnoremap <A-UP> :m '<-2<CR>gv=gv

" some additional mappings
nnoremap <Space> :
nnoremap <S-Space> q:?
vnoremap Y "+y

" searching
set smartcase

" insert mode mappings
"" line modifications
inoremap CC <esc>c
inoremap SS <esc>s
inoremap DD <esc>dd
inoremap UU <esc>u
inoremap YY <esc>V"+y
""quick movements
inoremap II <esc>i
inoremap AA <esc>a
inoremap OO <esc>o
