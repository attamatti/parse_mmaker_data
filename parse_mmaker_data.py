#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np
import math
try:
	file = open(sys.argv[1],'r').readlines()
	subunit = sys.argv[2]
	nummodels = int(sys.argv[3])
	try:
		colmax = sys.argv[4]
	except:
		colmax = False
except:
	sys.exit('USAGE: parse_mmaker_data.py <log copied from chimera> <subunit name> <color maximum>')

compdic = {}
for i in range(0,nummodels):
	compdic['{0}-{0}'.format(i)]=0

lines = []
n=0
labels_dic = {}
for line in file:
	if 'sequence alignment score' in line:
		m1 = line.split()[4].strip('(#),')
		m2 = line.split()[9].strip('(#),')
		labels_dic[int(m1)] = line.split()[1].split('.')[0]
		rmsd = file[n+8].split()[-1].strip(')')
		compdic[m1+'-'+m2] = rmsd
	n+=1

ckeys = compdic.keys()
ckeys.sort()

valsarray = np.zeros([nummodels,nummodels])
meanscalc = []
for i in compdic:
	x,y = (int(i.split('-')[0]),int(i.split('-')[1]))
	valsarray[x,y] =  float(compdic[i])
	meanscalc.append(float(compdic[i]))
print("output array")
print('Mean: {0}\tSTD: {1}\tSTDERR:{2}\t(not including self-correlations)'.format(np.mean(meanscalc),np.std(meanscalc),np.std(meanscalc)/math.sqrt(0.5*len(meanscalc))))
print valsarray

print labels_dic

if colmax ==False:
	colmax = np.max(valsarray)
plt.matshow(valsarray,cmap='cool',vmin=0,vmax=colmax)
x_pos = range(len(labels_dic))
labels = [labels_dic[x] for x in x_pos]
plt.xticks(x_pos,labels,fontsize='xx-small',rotation='vertical')
plt.yticks(x_pos,labels,fontsize='xx-small')
for y in range(valsarray.shape[0]):
	for x in range(valsarray.shape[1]):
		color = 'k'
		plt.text(x, y, '%.1f' % valsarray[y, x],
		horizontalalignment='center',
		verticalalignment='center',
		fontsize='xx-small',
		color=color)
plt.savefig('{0}_RMSDS.png'.format(subunit))
