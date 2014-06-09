" delete all lines not containing useful content (i.e. no vocals or no formula or no datetag)
v/a\|e\|i\|\o\|\$\|(/d
" replace all occurences of selection by searching first for selection (* command) and afterwards opening a replace dialog
vmap <leader>z *<ESC>:%s///g<left><left>
" convert ipython notebooks
!start ipython nbconvert apr.ipynb --to html --template output_toggle_html 
!start ipython nbconvert --to=latex --template=latex_nocode.tplx --post=pdf notebook.ipynb
