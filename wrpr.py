from matplotlib.pyplot import scatter
from matplotlib.pyplot import plot
from matplotlib.pyplot import axis
from numpy import hstack
from numpy import insert

def _scatter(p_i, color='b'):
        """
	'Wrapper arund scatter allowing matrix input'
        'Projects into the Cartesian x-z plane'
        'Points: p_i'
        """
	if p_i.size <= 3:
		s = scatter(p_i[0], p_i[-1], c=color)
	else:
		s = scatter(p_i[:,0], p_i[:, -1], c=color)
	axis('equal')
        return s

def _line(p_i, color='b'):
        """
	'Wrapper arund plot drawing close lines '
        'Projects into the Cartesian x-z plane'
        'Points: p_i'
        """
	s = plot(hstack((p_i[:,0], p_i[0, 0])),
		hstack((p_i[:,-1], p_i[0, -1])),
		c=color)
	axis('equal')
        return s

def _arrow(T, V, color='b', label=''):
	"""
	Draw arrows
	'Tail: T'
	'Head: O+V'
	from numpy import array
	close()
	figure()
	T = array([0, 0])
	plot(1, 1, label='Point')
	_arrow(T, array([2, 1]), label='arrow')
	legend()
	grid()
	axis([-3,3,-3,3])
	"""
	a = arrow(T[0], T[1], V[0], V[1],
			head_width = 0.05, head_length = 0.1,
			length_includes_head = True,
			color=color)
	plot([T[0], T[0] + V[0]], [T[1], T[1] + V[1]],
			color = color,
			label = label)
	axis('equal')
        return a

def _3D(p_i):
    """
    'Add a pseudo y-Coordinate to each point'
    'Coordinates of points: '; Symbol('p_i')
    """
    return insert(p_i, 1, zeros(p_i.shape[0]), axis=1)
