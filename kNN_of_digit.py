import os
from kNN import *
from numpy import *
def inPut(filename):
	fr = open(filename,'r')

	ans = zeros((1,1024))
#	print zeros(1,2) 
	for i in range(32):
		line = fr.readline()
		for j in range(32):
			ans[0,i*32+j] = int(line[j])
	return ans		

#testVector = inPut('0_0.txt')
#print testVector[0,0:20]

def read_dir(dirname):
	Labels = []
	fileList = os.listdir(dirname)
	m = len(fileList)
	trainMat = zeros((m,1024))
	for i in range(m):
		filename = fileList[i]
		fileStr = filename.split('.')[0]
		classNum = int(fileStr.split('_')[0])
		Labels.append(classNum)
		trainMat[i,:] = inPut('trainingDigits/%s' % filename)
	return trainMat, Labels

def handwriteClass(dir_1, dir_2):
	trainMat, Labels = read_dir(dir_1)
	testMat, tLabels = read_dir(dir_2)
	n = len(testMat)
#m = len(trainMat)
	errorCount = 0.0
	for i in range(n):
		testLabel = classify0(testMat[i,:], trainMat, Labels, 3)
		if (testLabel != tLabels[i]): errorCount += 1.0
	print "the number of errors: %d" % errorCount
	print "the error rate: %f" % (errorCount/float(n))							   
handwriteClass('trainingDigits', 'testDigits')

