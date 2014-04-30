
def dw(p_i, v_i):
	"""
	'Displaced water particles: coordinates and volumes'
        'Coordinates of particles: '; Symbol('p_i')
	"""
        if any(p_i[:, 2]<= 0):
            w_i = p_i[p_i[:, 2] <= 0, :] # coordinates
            v_w = v_i[p_i[:, 2] <= 0, :] # volumes
	    return w_i, v_w  
        return zeros((1, 3)), 0



def cbcs(p_i, m_i):
	"""
	Center body coordinate system
    	'Coordinates of particles: p_i'
    	'Masses of particles: m_i'
	p_i = array([[0, 0], [0, 1], [1, 1], [1, 0]])
	m_i = ones((p_i.shape[0], 1))
	cbcs(p_i, m_i)
	"""
	return p_i - ccom(p_i, m_i) 

def f_e(v_i, rho_i, v_w):
    """
    'Effective force caused by gravity vs. buoyancy'
    'Volumes of particles: v_i'
    'Density: '; abc.rho
    'Displaced water volume: v_w'
    """
    return (sum(gf(pm(v_i, rho_i)), axis=0) + sum(-gf(pm(v_w)), axis=0))

def tau_e(p_i, v_i, w_i, v_w, rho_i):
	"""
	'Effective torque'
        'Coordinates of particles: p_i'
        'Volumes of particles: v_i'
        'Coordinates displaced water: w_i';
        'Volume displaced water: v_i'
        'Densities of particles: rho_i'
	"""
        return (sum(cross(p_i,  gf(pm(v_i, rho_i))), axis=0) + 
                sum(cross(w_i, -gf(pm(v_w))),      axis=0))

def fat(x, R, p_i, v_i, rho, v= zeros(3)):
    """ 
    'Force and torque'
    'Translation Body to world: x'
    'Rotation Matrix Body to world coordinate system: R'
    'Coordinates of particles: p_i';
    'Volumes of particles: v_i'; 
    'Density: '; abc.rho
    'Velocity: v'
    """ 
    r_i = wsc(p_i, R, x)
    w_i, v_w = dw(r_i, v_i)
    return f_e(v_i, rho, v_w) - 10 *v, tau_e(r_i, v_i, w_i, v_w, rho_i)

def s(x, p, R, l):
	"""
        'State vector'	
        'Translation: x'
        'Linear momentum: p'
        'Rotation Matrix Body to world coordinate system: R'
        'Angular momentum: l'
	"""
	return hstack((x, p, R.flatten(), l))

def d_s(s, t=None):
	"""
        'Change in state vector'	
        'State vector: s'
	"""
        x = s[:3]
        v = s[3:6]  # velocity
        R = s[6:15].reshape((3, 3))
        l = s[15:18]
        f, tau = fat(x, R, b_i, v_i, rho_i, v)
	a = f/args['M'] # acceleration
        return hstack((v, a, zeros(12))) 

'the controll weight'
T = array([[0,  0], [2,  0], [2,  2]])
N = 100
p_i = _3D(uspit(N, T))
v_i = abs(A_T(T)) / N * ones((N, 1))
rho_i = 2* ones(v_i.shape)
T = array([[0,  0], [2,  2], [0,  2]])
p_i = vstack((p_i, _3D(uspit(N, T)))) 
v_i = vstack((v_i, abs(A_T(T)) / N * ones((N, 1)))) 
rho_i = vstack((rho_i, rho_i)) 
p_i += array([-1, 0, 10])
p_i += array([-10, 0, 0])

'the boat'
T = array([[0,  0], [10,  10], [-10,  10]])
N = 1000
p_b = _3D(uspit(N, T))
v_b = abs(A_T(T)) / N * ones((N, 1))
rho_b = 0.5 * ones(v_b.shape)

'plug them together'
v_i = vstack((v_i, v_b))
rho_i = vstack((rho_i, rho_b))
b_i = cbcs(vstack((p_i, p_b)),
	    v_i * rho_i
	   )
args = {'M': sum(pm(rho_i, v_i))}; 'Total mass'
a_0 = 0
z_0 = 0

'visualize'
_scatter(b_i, color=rho_i)

'wrap the force function '
f_b = lambda z : fat(array([0, 0, z]), R_y(a_0), b_i, v_i, rho_i, zeros(3))[0][2]
z = linspace(-20, 20)
plot(z, array([f_b(z_) for z_ in z]))
'Use the simple bisection method'
'search equilibrium'
f_b(-20)
z_0 = bisect(f_b, -10, 10)
print 'z_0',
print z_0
f_r = lambda a: fat(array([0, 0, z_0]), R_y(a), b_i, v_i, rho_i, zeros(3))[1][1]
a = arange(-pi, pi, 0.1)
a_0 = bisect(f_r, -2, 2)
print 'a_0',
print a_0


plot(a, array([f_r(a_) for a_ in a]))

_scatter(wsc(b_i, R_y(a_0),  array([0, 0, z_0])), color=rho_i)
_scatter(wsc(b_i, R_y(-1.74),  array([0, 0, z_0])), color=rho_i)

fat(array([0, 0, z_0]), R_y(a_0), b_i, v_i, rho_i, zeros(3))

x = array([0, 0, 10])
p = zeros(3)
R = R_y(a_0) 
l = zeros(3)

'Simulate'
d_t = 0.1
J = 1000
t = d_t * arange(J)
s_ = s(x, p, R, l)
S = zeros((J, s_.shape[0]))
for j in range(J):
    S[j, :] = s_.copy()
    d_s_ = d_s(s_)
    s_ += d_t * d_s(s_)
f = lambda z_ :fat(array([0, 0, z_]), R, b_i, v_i, rho_i)[0][2]
f(20)
f_z = array([f(z_) for z_ in S[:,2]])
plot(f_z/args['M'])
plot(S[:, 5])
sum(array([f(z_) for z_ in S[:,2]])/args['M'])
f(S[-1, 2])
