f = ['https://raw.githubusercontent.com/svermeulen/vim-easyclip/master/doc/easyclip.txt', 'https://raw.githubusercontent.com/tpope/vim-fugitive/master/doc/fugitive.txt']
from os import system
for f_ in f:
	system('curl -o %s %s' %(f_.rpartition('/')[-1], f_))
