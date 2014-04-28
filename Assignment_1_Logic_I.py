# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# General Information

# <markdowncell>

# This is the first exercise in the KI course. You will have to implement a few algorithms from the lecture. The assignment will be graded, but it should also serve for you to understand the concepts more deeply and experiment and play around with the ideas. You can add code and cells at any point in the notebook; the only important thing for the grading to work is that you don't change the function names. The signature of the functions (the meaning and order of function arguments and return values is given, and should not be changed). Please do not use special ipython functionality, such as [ipython magics](http://ipython.org/ipython-doc/dev/interactive/tutorial.html).
# 
# Practical help with the assignments will be available in moodle and during the tutorial sessions, which will be anounced on moodle and on the KI website.
# 
# Some of the exercises will not get a visible grade on the course website, and will only be graded after the assignment deadline. Also, the grades might change slightly if we realize that our evaluation was not optimal.

# <headingcell level=1>

# The GSAT algorithm

# <markdowncell>

# In this exercise, you will implement an algorithm to find an approximate solution for the 3-CNF problem, that is, the problem of finding a satisfying assignment for a logical sentence of the form 
# $$
# \left(P \vee Q \vee \neg S\right) \wedge \left(R \vee T \vee \neg P\right) \wedge \left(R \vee T \vee \neg S\right).
# $$
# 
# The GSAT algorithm is an instance of a class of algorithms called [*Local Search Algorithms*](http://en.wikipedia.org/wiki/WalkSAT), which explore the state space of boolean assignments to variables by considering a locally optimal, or *greedy* change to that assignment.
# 
# 3-CNF formulas are in CNF form, and each clause contains exactly 3 literals. The GSAT algorithm starts with a random truth assignment to the symbols, and then tries to find a satisfying assignment by changing one truth value at a time. The symbol to be changed is selected such that the maximum number of clauses is satisfied after each step. If there are multiple variables that satisfy the same number of clauses, the decision between them is arbitrary.
# 
# Since the trajectory of the state (the truth assignments to each variable in each step of the algorithm) depends heavily on the initial state, the algorithm is restarted several times with different initial states.
# 
# The algorithm performance is influenced by two important parameters: $C$, the number of clauses, and $N$, the number of proposition symbols.

# <headingcell level=2>

# Representing 3-CNF problems

# <markdowncell>

# For this exercise, 3-CNFs are represented as a set of clauses, where each clause consists of two sets: The first one contains the indices of the variables in the clause that are nonnegated; the second one the indices for the variables that appear negated. The state is simply a list of boolean values, of length N. 
# 
# For the example given above, that would be:

# <codecell>

state = [False, False, True, True, False]

# variables in the order (P, Q, R, S, T)
problem = [
           ({0, 1}, {3, }),
           ({2, 4}, {0, }),
           ({2, 4}, {3, })
           ]
           

# <headingcell level=2>

# Complexity

# <markdowncell>

# Which complexity class does the problem of satifisbility of 3-CNF formulas belong to? Select the most concise answer. Return a string from your function.

# <codecell>

def three_cnf_complexity():
    return 'very, very hard'

# <markdowncell>

# How many evaluations have to be made in every step of the algorithm (assuming that the satisfiability of a clause can be checked in 1 step)? Return a sympy function in the variables $N$ and $C$.
# \todo{Must the function be callable?}
# <codecell>

from sympy import var
var('N C')
N = Symbol('N'), 'Number of proposition symbols'
C = Symbol('C'), 'Number of clauses'
def gsat_step_complexity():
    return N * C
# worst case: need to check all values first to see which change satisfies the
# most clauses 
# <markdowncell>

# Is this algorithm complete? Return True or False.
# todo
# <codecell>

def gsat_complete():
    return True

# <headingcell level=2>

# Generating Problems

# <markdowncell>

# Generate random instances of 3-CNF problems, given C and N. Note that the representation of the positive and negative literals for each clause as sets does not allow clauses like $P \wedge P \wedge Q$. Your random problems should always have 3 literals in the set representation.

# <codecell>
N = 4

def generate_random_problem(C, N):
    # Draw 3 symbol indices
    # Draw 3 boolean values
    # Associate them to the indices
    problem = None
    return problem

# <markdowncell>

# Can you think of a simple way to simplify the problem in cases where clauses are tautological?
# Write a function that simplifies the problem accordingly.
# [ In logic, a tautology (from the Greek word ταυτολογία) is a formula which is true in every possible interpretation ]
# <codecell>
# \todo{Do you consider things like $(P \lor Q \lor \neg P$ or should they already be avoided when the problem is created?}
def simplify_three_cnf(problem):
	simplified_problem = problem
    return simplified_problem

simplify_three_cnf(problem)

# <headingcell level=2>

# Implementing GSAT

# <markdowncell>

# Write a function that generates the initial state for a 3-CNF SAT problem. It should be random, so that calling it at multiple times gives different results.

# <codecell>

def get_initial_state(C, N):
    return None

# <markdowncell>

# Now, write a function that evaluates the truth value of a clause, and returns whether it is satisfied:

# <codecell>

def eval_clause(clause, state):
    return None

# <markdowncell>

# Building on this, add a function that evaluates a whole 3-CNF formula:

# <codecell>

def eval_three_cnf(problem, state):
    return None

# <headingcell level=3>

# Stopping Condition

# <markdowncell>

# Write a function that checks if a solution has been found. It should return True if the alforithm is done, and False otherwise.

# <codecell>

def am_i_done(problem, state):
    return 42

# <headingcell level=2>

# Putting together the algorithm

# <markdowncell>

# Write a function that runs one chain of GSAT for a given maximum number of iterations `max_iter`. It should return the best encountered state and whether the algorithm succeeded in finding a satisfying assignment or not, and it should return as early as possible.

# <codecell>

def run_gsat_chain(problem, state, max_iter):
    for _ in xrange(max_iter):
        pass

    final_state = 0
    success = bool(13 % 1)
    return final_state, success

N, C = 10, 4
run_gsat_chain(simplify_three_cnf(generate_random_problem(N, C)), get_initial_state(N, C), 100)

# <markdowncell>

# Now, write a function that generates an initial state for the multiple chains (at most `max_n_chains` of them), runs them, and returns `success` and a satisfying assignment if there was one, or else the best assignment that was found for the latter.

# <codecell>

def run_gsat(problem, max_iter, max_n_chains):
    success = bool(round(random.random()))
    satisfying_assignment = 42 if success else 17
    return success, satisfying_assignment

run_gsat(simplify_three_cnf(generate_random_problem(N, C)), 0, 0)

# <headingcell level=2>

# Experiment

# <markdowncell>

# Experiment! Generate random problems of different sizes by varying $C$ and $N$ for your assignment function and use the timing functions of python to check the runtimes of the algorithm for different problems, and determine what feasible values for `max_iter` and `max_n_chains` could be. Make a plot of typical runtimes and their statistics (`np.mean` and `np.median` can be useful here) versus the algorithm parameters.
# 
# Timing a function works like so:
# 
# ```
# def foo():
#     pass
# 
# import timeit
# timeit.timeit(foo)    
# ```

# <codecell>

import timeit
def foo():
    pass

timeit.timeit(foo)

# <headingcell level=1>

# Propositional Pacman

# <markdowncell>

# In this exercise you are going to implement part of a propositional system for a Pacman Agent. Given the limitations of propositional logic, it is going to be a very simple system, but it should serve to illustrate the concept.
# 
# The point of this exercise is to use propositional logic lo localize both the ghost and the one piece of Pacman food in a 4x4 map. This is made difficult by the fact that Pacman can not see further than one step in the grid, so he does not have access to the full state, but his perception consists of 
# 
# - a delicious smell if he is in a square adjacent to a piece of food
# - a chill when he is in a square adjacent to a ghost.
# 
# For this exercise, we are only interesed in one single piece of information - that is, if it is safe for Pacman to move to the square (2, 2) based on the imformation he has already perceived. This information is represented in the state, which contains a label for each quare of the grid, which is one of `Chill_i_j` if the square $(i, j)$ is chilly, `-Smell_i_j` if there was no chill, and `NotVisited_i_j` if Pacman hasn't been there yet. This is an example state:
# 
# ```
# ['-Chill_0_0',
#  'NotVisited_0_1',
#  'NotVisited_0_2',
#  '-Chill_0_3',
#  'NotVisited_1_0',
#  '-Chill_1_1',
#  'Chill_1_2',
#  '-Chill_1_3',
#  '-Chill_2_0',
#  'NotVisited_2_1',
#  'NotVisited_2_2',
#  'Chill_2_3',
#  '-Chill_3_0',
#  'NotVisited_3_1',
#  'Chill_3_2',
#  '-Chill_3_3'] ```
# 
# The state can be visualized rudimentarily with the `show_state` function given below - for this example state it looks like this:
# 
# ```
# [['0', '.', '.', '0'],
#  ['.', '0', 'S', '0'],
#  ['0', '.', 'G', 'S'],
#  ['0', '.', 'S', '0']]
# ```
# 
# Please provide a function that, based on this state description, returns one of the labels `Safe_2_2`, `Unsafe_2_2` or `Ghost_2_2`, which tell if there cannot be a ghost, there could maybe be a ghost, or there certainly is a ghost, for the square (2, 2). 
# In the example, the return value should be `Ghost_2_2`, because from the three chilly squares surrounding the target square, it is clear that the ghost has to be there.
# 
# Your solution should work on  propositional level, i.e. you should not have to parse the positions out of the state symbols, but rather write rules that work on the state directly.

# <codecell>

import pprint
def show_state(state, ghost_pos=None):
    """Show the state graphically, and the position of the ghost, if it is known"""
    chars = {'Chill': 'S', 
             '-Chill': '0',
             'NotVisited': '.'}
    
    ss = [range(4) for _ in range(4)]
    for s in state:
        c, i, j = s.split('_')
        ss[int(i)][int(j)] = chars[c]
    if ghost_pos:
        ss[ghost_pos[0]][ghost_pos[1]] = 'G'

    pprint.pprint(ss)

show_state(state, ghost_pos)

# <codecell>

def is_2_2_safe(state):
    """a function that determines in a propositional way if it safe to move to the (2, 2) square."""
    if 1:
        return 'Safe_2_2'
    elif 2:
        return 'Ghost_2_2'
    else:
        return 'Unsafe_2_2'



