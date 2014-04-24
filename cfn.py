#!/usr/bin/python
import os
import sys
files = os.listdir(os.getcwd())
for f in files:
    if ' ' in f or '-' in f and not 'pythontex' in f:
	    print 'Renaming file: %s' %f
	    os.rename(f, f.replace(' ', '_').replace('-','_'))

