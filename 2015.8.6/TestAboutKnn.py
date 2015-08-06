import matplotlib as mpl
mpl.use('Agg')
import kNN
Data, Labels = kNN.stringToMatrix('datingTestSet.txt')
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)	
from numpy import *
ax.scatter(Data[:,1], Data[:,2],
15.0*array(Labels), 15.0*array(Labels))	
fig.savefig('test.png')	
