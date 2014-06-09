" Vundle
set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/vimfiles/bundle/vundle/
let path='~/vimfiles/bundle'
call vundle#rc(path)
" let Vundle manage Vundle, required
Bundle 'dahu/vim-fanfingtastic'
Bundle 'inside/vim-grep-operator'
Bundle 'jeetsukumaran/vim-buffergator'
Bundle 'justinmk/vim-sneak'
Bundle 'mtth/scratch.vim'
Bundle 'scrooloose/nerdcommenter'
Bundle 'scrooloose/nerdtree'
Bundle 'svermeulen/vim-easyclip'
Bundle 'tpope/vim-eunuch'
Bundle 'tpope/vim-fugitive'
Bundle 'tpope/vim-repeat'
Bundle 'tpope/vim-sensible'
Bundle 'tpope/vim-surround'
Bundle 'tpope/vim-unimpaired'
Bundle 'godlygeek/tabular'
Plugin 'gmarik/vundle'


filetype plugin indent on     " required

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
	set clipboard=unnamed
else
	set clipboard=unnamedplus
	"tmux-runner
	let g:VtrStripLeadingWhitespace = 0
	let g:VtrClearEmptyLines = 0
	let g:VtrAppendNewline = 1"" 
	let g:VtrUseVtrMaps = 1
end 


" grepping
set grepprg=git\ grep\ -i\ -F\ -n\ --break\ --untracked\ --all-match\ $*

" Filter buffer by regexp and display in a new scratch buffer.
function! Filter(pattern)
  if !empty(a:pattern)
    let save_cursor = getpos(".")
    let orig_ft = &ft
    " append search hits to results list
    let results = []
    execute "g/" . a:pattern . "\\c/call add(results, getline('.'))"
    call setpos('.', save_cursor)
    if !empty(results)
      " put list in new scratch buffer
      Scratch!
      execute "setlocal filetype=".orig_ft
      call append(1, results)
      1d  " delete initial blank line
    endif
  endif
endfunction

" Abbreviations
iab <expr> TG strftime("%y%m%d%H%M%S")
iab opn \operatorname{ }<Left><Left> 
iab cal \mathcal{}<Left><Left> 
ab  grp call GitGrep('-e ')<Left><Left>
" leader maps
nmap 	 <silent> <leader>gf :split <cfile><cr>
nnoremap <silent> <Leader>f :call Filter(input("Search for: "))<CR>
nnoremap <silent> <Leader>F :call Filter(@/)<CR>
nmap     <silent> <Leader>s <plug>SubstituteOverMotionMap
nmap <leader>g <Plug>GrepOperatorOnCurrentDirectory
vmap <leader>g <Plug>GrepOperatorOnCurrentDirectory
nmap <leader><leader>g <Plug>GrepOperatorWithFilenamePrompt
vmap <leader><leader>g <Plug>GrepOperatorWithFilenamePrompt

" Other mappings
noremap <silent> <F4> :let @+=expand("%:p:r")<CR>
nnoremap <Space> q:?

" sneak motion
nmap <Tab> <Plug>Sneak_s
nmap <BS>  <Plug>Sneak_S
xmap <Tab> <Plug>Sneak_s
xmap <BS>  <Plug>Sneak_S
omap <Tab> <Plug>Sneak_s
omap <BS>  <Plug>Sneak_S

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

" tabs and indent
set smartindent
set tabstop=4
set shiftwidth=4
set expandtab

" searching
set mousemodel=extend "shift-LeftClick a word to search forwards, or Shift-RightClick to search backwards
set incsearch
set smartcase
set ignorecase 

" line wrapings
set wrap linebreak nolist "use gj and gk to move by screen lines

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
