from subprocess import Popen
from os import getcwd
from os.path import sep

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

