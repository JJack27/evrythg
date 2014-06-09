from sympy.printing import latex
from os import system
from IPython.core.display import Image 
ip = get_ipython()
class _latex:
    """
    Print a latex representation with special symbols replaced
    symbol_names: the dictionary containing replacements
    """
    def __init__(self):
        self.symbol_names = dict() 
    def out(self, expr):
        """
        expr: A sympy expression
        """
        if type(expr) == str: return expr
        l = latex(expr, symbol_names=self.symbol_names)
        return l

l = _latex()
_o = lambda e : l.out(e)
_d = l.symbol_names

def _input(fname):
    ''' Insert file content '''
    with open(str(fname), 'r') as fin:
        return fin.read().decode('utf8')

eq = lambda t: _m(_input(str(t))).d()

from IPython.core.display import Math
from IPython.core.display import Latex
from IPython.core.display import display
def MDPL(string): 
    display(Math(string.replace('$', ''))) 
    #print string

def add(x,y): return x+y

def comp_str(listofstrings): return reduce(add,listofstrings)

class _m(object):
   '''''Math Expression object'''''

   def __init__(self, expr):
      '''''init takes arg: list of atoms, each atom being a compilable chunck of LaTeX expression'''''
      if type(expr) == list: self.listofatoms = [_o(e) for e in expr]; return
      if 'sympy' in str(expr): self.listofatoms = _o(expr) ; return
      if type(expr) == str and not ' ' in expr: self.listofatoms = [expr]; return
      self.listofatoms = [' %s ' %e for e in expr.split()] 

   def d(self):
      '''''Displays the content of the expression in mathmode'''''
      MDPL(comp_str(self.listofatoms))
      return self

   def r(self,pos,newstr):
      '''''Replaces an atom with another atom'''''
      MDPL(comp_str(self.colouratoms([pos])))
      self.listofatoms[pos] = newstr
      MDPL(comp_str(self.colouratoms([pos],True)))

   def j(self,positions):
      '''''Join atoms: the input is a list of positions. The new atom is placed at the position of the foremost of the positions'''''
      MDPL(comp_str(self.colouratoms(positions)))
      temp = [ self.listofatoms[i] for i in positions ]
      positions.sort()
      positions.reverse()
      for i in positions: del self.listofatoms[i]
      self.listofatoms.insert(positions[-1],comp_str(temp))
      MDPL(comp_str(self.colouratoms([positions[-1]],True)))

   def s(self,pos,newatoms):
      '''''Splits atoms: replaces an atom in place with multiple sub atoms'''''
      MDPL(comp_str(self.colouratoms([pos])))
      del self.listofatoms[pos]
      templen = len(newatoms)
      while len(newatoms) > 0:
         self.listofatoms.insert(pos,newatoms.pop())
      MDPL(comp_str(self.colouratoms(range(pos, pos+templen),True)))

   def c(self,positions):
      '''''Cancels a bunch of terms: input a list of positions'''''
      MDPL(comp_str(self.colouratoms(positions)))
      positions.sort()
      positions.reverse()
      for i in positions: del self.listofatoms[i]
      self.fullshow()

   def m(self,posini,posfin):
      '''''Move atom at posini to posfin, pushing all others back'''''
      MDPL(comp_str(self.colouratoms([posini])))
      temp = self.listofatoms.pop(posini)
      self.listofatoms.insert(posfin if posfin < posini else posfin-1, temp)
      MDPL(comp_str(self.colouratoms([posfin if posfin < posini else posfin-1],True)))

   def colouratoms(self,positions,labelled=False):
      '''''Returns the list of atoms, but with selected terms coloured'''''
      temp = list(self.listofatoms)
      if labelled:
         self.labelatoms()
         temp = list(self.labeledatoms)
      for i in positions: temp[i] = "\color{red}{"+temp[i]+"}"
      return temp

   def labelatoms(self):
      '''''Label atoms by adding underbraces'''''
      self.labeledatoms = [ "\underbrace{" + self.listofatoms[i] + "}_{" + str(i) + "}" for i in range(len(self.listofatoms)) ]

   def fs(self):
      '''''Shows the content whilst labeling positions'''''
      self.labelatoms()
      MDPL(comp_str(self.labeledatoms))
                                                            
_v = lambda t: Image(filename='%s.png' %t)                              
_v.__doc__="Display Image \n fn: Image"

def _l(fn):
    """
    Include file content and format as latex
    fn: Filename
    """
    ip.set_next_input('%%%%latex \n%s' %_input(fn))


def _f(s):
    """
    Insert a cell below
    s: SList
    """   
    ip.set_next_input(str(s.nlstr))

global _s
# insert shell output in cell below
ip.define_magic('_so', lambda s, l: _f(_s))



