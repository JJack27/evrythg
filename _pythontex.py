def input(fname):
	with open(str(fname), 'r') as fin:
		print(r'\blockquote{')
    		print(fin.read().decode('utf8'))
		print(r'}')
