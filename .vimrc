set nocompatible              " be iMproved, required
filetype off                  " required
set rtp+=~/vimfiles/bundle/vundle/
let path='~/vimfiles/bundle'
call vundle#rc(path)
" let Vundle manage Vundle, required
Plugin 'gmarik/vundle'
"" list of plugins
Bundle 'tpope/vim-sensible'
Bundle 'tpope/vim-surround'
Bundle 'justinmk/vim-sneak'
Bundle 'tpope/vim-fugitive'
Bundle 'tpope/vim-unimpaired'
Bundle 'scrooloose/nerdtree'
filetype plugin indent on     " required
" Put your stuff after this line

filetype plugin indent on     " required
" Put your stuff after this line

" visuals
colorscheme desert
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
nnoremap <leader>d "=strftime(" %y%m%d%H%M%S")<CR>Pviw"dy
map 	 <leader>gf :split <cfile><cr>
nmap     <leader>a :call GitGrepWord()<CR><CR>

nmap <Tab> <Plug>Sneak_s
nmap <BS>  <Plug>Sneak_S
xmap <Tab> <Plug>Sneak_s
xmap <BS>  <Plug>Sneak_S
omap <Tab> <Plug>Sneak_s
omap <BS>  <Plug>Sneak_S

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
