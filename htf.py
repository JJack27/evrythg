from struct import unpack
from sys import argv
"""
Parse Surfboard log files
"""
f = str(argv[1])
P = dict()
P['4'] = lambda v: ('%s, %s, %+3.3f\n' %(v[0], v[2], unpack('<f', v[-1].decode('hex'))[0] * 60)) 
P['2'] = lambda v: ('%s, %s, %+3d\n'   %(v[0], v[2], unpack('<h', v[-1].decode('hex'))[0]))
P['1'] = lambda v: ('%s, %s, %+3d\n'   %(v[0], v[2], unpack('<?', v[-1].decode('hex'))[0]))

o = open(f.replace('txt', 'csv'), 'w')
with open(f) as i:
    for l in i:
        v = [v.replace('0x', '').strip() for  v in l.split(',')]
        s = P[v[-2]](v)
        # print s
        o.write(s)
o.close()
