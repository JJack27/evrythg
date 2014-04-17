#!/usr/bin/env python
from os import system
from time import strftime
fn = 'clean.tex'
cmds = ['pdflatex -interaction=nonstopmode %s > %s',
"C:\Anaconda\python.exe  C:\Users\Murad\pythontex\pythontex\pythontex.py %s > %s",
'pdflatex -interaction=nonstopmode %s > %s']
for c in cmds: 
	cmd = c %(fn, 'log.swp')
	print strftime('%d %b %Y %H:%M:%S: ') + cmd 
	system(cmd)
system('rm -f *.aux')
system('rm -f *.log')
