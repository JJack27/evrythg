from subprocess import Popen # for windows
from os import system # for linux
from os import getcwd
from os import environ
from os.path import sep
from os import system
from time import strftime
from sys import platform
fn = lambda t: getcwd() + sep + t
fn.__doc__="Create an absolute file path for tag.\nt: time tag"
    
def _v(t):
    """
    View the tagged image
    t: time tag
    """
    if platform == 'linux2':
        system('feh %s.png &' %(fn(t)))
    else:
        Popen('jpegview %s.png' %(fn(t)))

def _c(t):
    """
    Capture an image for tag
    t: time tag
    """
    if platform == 'linux2':
        system('scrot -s %s.png &' %(fn(t)))
    else:
        Popen('MiniCap -captureregselect -save "%s.png" -exit' %(fn(t)))
def _m(fn):
    """
    Compile latex using pythontex
    """
    fn = fn.split('.')[0]
    cmds = ['pdflatex -interaction=nonstopmode %s.tex > %s',
    'biber %s > %s',
    "%s  %s\pythontex\pythontex\pythontex.py %s.tex > %s" %(environ['PYTHON'], environ['HOME'], '%s', '%s'),
    'pdflatex -interaction=nonstopmode %s.tex > %s']
    for c in cmds: 
            cmd = c %(fn, 'log.swp')
            print strftime('%d %b %Y %H:%M:%S: ') + cmd 
            system(cmd)
    print strftime('%d %b %Y %H:%M:%S: Cleaning up')
    ext = ['out', 'log', 'aux']
    for e in ext:
        print('\tRunning rm -f %s.%s' %(fn.split('.')[0], e))
        system('rm -f %s.%s' %(fn, e))
