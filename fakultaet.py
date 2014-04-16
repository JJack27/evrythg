def iterativ (n) :
	"""
	Iteratively compute $n!$ 
	"""
	r = 1
	for i in xrange (1 , n +1) :
		r *= i
	return r

def rekursiv (n) :
	"""
	Recursively compute $n!$ 
	"""
	if n == 0:
	return n * rekursiv (n -1)
        return 1


if __name__ == ' __main__':
	print rekursiv (int(sys.argv[1]))

