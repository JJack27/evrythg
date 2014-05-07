from subprocess import Popen
from os import getcwd
from os import environ
from os.path import sep
from os import system
from time import strftime

fn = lambda t: getcwd() + sep + t
fn.__doc__="Create an absolute file path for tag.\nt: time tag"

def _v(t):
    """
    View the tagged image
    t: time tag
    """
    Popen('jpegview %s.png' %(fn(t)))

def _c(t):
    """
    Capture an image for tag
    t: time tag
    """
    Popen('MiniCap -captureregselect -save "%s.png" -exit' %(fn(t)))

def _m(fn):
    """
    Compile latex using pythontex
    """
    cmds = ['pdflatex -interaction=nonstopmode %s > %s',
    'biber %s > %s',
    "C:\Users\mchl\Anaconda\python.exe  %s\pythontex\pythontex\pythontex.py %s > %s" %(environ['HOME'], '%s', '%s'),
    'pdflatex -interaction=nonstopmode %s > %s']
    for c in cmds: 
            cmd = c %(fn, 'log.swp')
            print strftime('%d %b %Y %H:%M:%S: ') + cmd 
            system(cmd)
    print strftime('%d %b %Y %H:%M:%S: Cleaning up')
    ext = ['out', 'log', 'aux']
    for e in ext:
        print('\tRunning rm -f %s.%s' %(fn.split('.')[0], e))
        system('rm -f %s.%s' %(fn.split('.')[0], e))
