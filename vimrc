execute pathogen#infect()
call pathogen#helptags()

" Fold Support
set foldmethod=indent
set foldlevel=0
set modelines=1

" Colors and Basic Configuration
colorscheme badwolf  
syntax on
set number
set showcmd
set cursorline
filetype indent on
set wildmenu
set showmatch
set hidden
set directory=/tmp/swapfiles
set laststatus=2

" Tabs
filetype plugin indent on
set tabstop=8 softtabstop=0 expandtab shiftwidth=2 smarttab

" Searching
set incsearch
set hlsearch

" Folding
set foldenable
set foldlevelstart=10
set foldnestmax=10
nnoremap <space> za

" Key Bindins
nnoremap j gj
nnoremap k gk

let mapleader=","
inoremap jk <esc>

nnoremap <leader>ev :vsp $MYVIMRC<CR>
nnoremap <leader>ez :vsp ~/.zshrc<CR>
nnoremap <leader>sv :source $MYVIMRC<CR>

nnoremap <leader>n :NERDTree<CR>
command NT NERDTree

" Random Paranthesis
au VimEnter * RainbowParenthesesToggle
au Syntax * RainbowParenthesesLoadRound
au Syntax * RainbowParenthesesLoadSquare
au Syntax * RainbowParenthesesLoadBraces

map <F7> :tabn <CR>
map <F6> :tabp <CR>

set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

set guioptions-=T
