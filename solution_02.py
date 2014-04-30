A = [] # Actions
S = [] # States
R = [] # Rewards

140430083858
# initialize
S = ['A'] 
A = []
R = []

A.append('back') 
R.append(0)
S.append('A')

A.append('back') 
R.append(0)
S.append('A')



140430090145
# initialize
S = ['A'] 
A = []
R = []

A.append('forward') 
R.append(1)
S.append('A')

A.append('forward') 
R.append(-1)
S.append('B')

A.append('forward') 
R.append(+1)

140430090212
cf. 140430084615
gamma = 0.5
G_0 = 1 + 0.5 * -1 + 0.5**2 * 1

140430090659
$v_{pi_1}(B) = 1$

140430094553
cf. 140430095413
