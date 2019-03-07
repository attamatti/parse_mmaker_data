#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np

try:
	file = open(sys.argv[1],'r').readlines()
	subunit = sys.argv[2]
	try:
		colmax = sys.argv[3]
	except:
		colmax = False
except:
	sys.exit('USAGE: parse_mmaker_data.py <log copied from chimera> <subunit name> <color maximum>')

compdic = {'0-0':0,'1-1':0,'2-2':0,'3-3':0,'4-4':0,'5-5':0,'6-6':0,'7-7':0,'8-8':0}
lines = []
n=0
for line in file:
	if 'sequence alignment score' in line:
		m1 = line.split()[4].strip('(#),')
		m2 = line.split()[9].strip('(#),')
		rmsd = file[n+8].split()[-1].strip(')')
		compdic[m1+'-'+m2] = rmsd
	n+=1

ckeys = compdic.keys()
ckeys.sort()
for i in ckeys:
	print(i,compdic[i])

valsarray = np.zeros([9,9])
print valsarray
print len(compdic)
for i in compdic:
	x,y = (i.split('-')[0],i.split('-')[1])
	print compdic[i]
	valsarray[x,y] =  compdic[i]
print valsarray

if colmax ==False:
	colmax = np.max(valsarray)
plt.matshow(valsarray,cmap='cool',vmin=0,vmax=colmax)
x_pos = range(0,9)
plt.xticks(x_pos,x_pos,fontsize='xx-small')
y_pos = range(0,9)
plt.yticks(y_pos,y_pos,fontsize='xx-small')
for y in range(valsarray.shape[0]):
	for x in range(valsarray.shape[1]):
		color = 'k'
		plt.text(x, y, '%.1f' % valsarray[y, x],
		horizontalalignment='center',
		verticalalignment='center',
		fontsize='xx-small',
		color=color)
plt.ylabel('class #')
plt.savefig('{0}_RMSDS.png'.format(subunit))
