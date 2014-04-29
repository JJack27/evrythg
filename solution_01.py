# RL_3.py
import RL_3 as syms 
from numpy import arange
from numpy import ones
from numpy import zeros
from numpy import vstack
from numpy import array
from numpy.linalg import norm
from numpy import tile
from matplotlib.pyplot import plot
from matplotlib.pyplot import axis
from matplotlib.pyplot import grid
from matplotlib.pyplot import xlabel
from matplotlib.pyplot import title
from matplotlib.pyplot import legend
from matplotlib.pyplot import savefig
from matplotlib.pyplot import close

def _input(fname):
	with open(str(fname), 'r') as fin:
		print(r'\emph{')
    		print(fin.read().decode('utf8'))
		print(r'}')

r = vstack((ones((6,1)), zeros((6,1)), tile(array([[1], [0]]), (3, 1)))).flatten()
s = 12 # start of alternating target
def estimate():
	q_k = [0] 
	for i in range(r.shape[0]):
		q_   =  q_k[-1] 
		q_  += alpha[i] * (r[i] - q_)	
		q_k.append(q_)
	return array(q_k)
# assume that time indices start at 1
def plot_r(r):
	k = arange(r.shape[0])+1
	plot(k, r, '-o', color = '0.75', # grey
	label = 'Target')
	xlabel('$k$')
a=0.5
def plot_q_k(k=arange(r.shape[0]+1)+1, alpha=a):
	plot(k, q_k, 'bo', 
	label = 'Estimate')
	title(r'$\alpha$ = %s' %(alpha))

def setup_figure(r):
	close('all')
	plot_r(r)
	grid()
	axis(ymin = -0.1, ymax= 1.1)

setup_figure(r)
alpha = a * ones(r.shape)
q_k = estimate()
ef = lambda : norm(r[s:] - q_k[s:-1])**2
e = {a: ef()}
plot_q_k()
legend()
savefig('140423111519.pdf')

def t_140423105502():
	print(r"\begin{center}")
	print (r"\begin{tabular}{c|c}")
	print  (r"$k$ & $Q_k$ \\ \hline")
	for k_ in [6, 10, 20]:
		print (r'%s & %s \\' %(k_, (lambda k : -0.5**k + 1)(k_)))
	print (r"\end{tabular}")
	print(r"\end{center}")

setup_figure(r)
a = 1.0/8 
alpha = a * ones(r.shape)
q_k = estimate()
e[a] = ef()
plot_q_k(alpha=a)
legend()
savefig('140424090951.pdf')

setup_figure(r)
a = 1.0
alpha = a * ones(r.shape)
q_k = estimate()
e[a] = ef()
plot_q_k(alpha = a)
legend()
savefig('140424090205.pdf')

def t_140424090951():
	print(r"\begin{center}")
	print(r"\begin{tabular}{c|c}")
	print(r"$\alpha$ & $\epsilon$ \\ \hline")
	for k in e.keys():
		print(r"%s & %s\\" %(k, e[k]))
	print(r"\end{tabular}")
	print(r"\end{center}")

setup_figure(r)
a = "1/k"
alpha = array([1./(k_+1) for k_ in range(r.shape[0])])
q_k = estimate()
plot_q_k(alpha = a)
legend()
savefig('140424105951.pdf')



A = [-0.5, 1.5, 2.0, 2.5]
fn = '140424135248%s.pdf' 
r = r[:6]
_fn = lambda a_ :(fn %a_).replace(".", "_", 1)
for a_ in A:
	setup_figure(r)
	alpha = a_ * ones(r.shape[0])
	q_k = estimate()
	axis(ymin = 1.1 * min(min(q_k), min(r)), ymax= 1.1 * max(max(q_k), max(r)))
	plot_q_k(k=arange(r.shape[0]+1)+1,alpha=a_)
	legend()
	savefig(_fn(a_))
	# raw_input("Press Enter to continue...")

def f_140424135248():
	for a_ in A:
		print(r'\begin{figure}[ht]')
		print(r'\includegraphics[width=\textwidth]{%s}'%(_fn(a_)))
		print(r'\end{figure}')
		print('\n')
