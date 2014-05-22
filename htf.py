from struct import unpack
"""
Parse Surfboard log files
Hex \to Float
"""
with open("2014_05_22_14_49_42.txt") as f:
    for l in f:
        v = [v.replace('0x', '').strip() for  v in l.split(',')]
        if len(v[-1]) < 4: continue
        print ('%s \t %s \t %+f)' %(v[0], v[2], unpack('<f', v[-1].decode('hex'))[0] * 60))
