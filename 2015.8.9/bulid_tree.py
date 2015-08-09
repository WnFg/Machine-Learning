from ChooseBestFeature import *
from clac_information import *

def majorLab(data):
	mapList = {}
	for vote in data:
		if vote[-1] not in mapList.keys():
			mapList[vote[-1]] = 0
		mapList[vote[-1]] += 1
	maxVote = 0
	for ret in mapList:
		if mapList[ret] > maxVote:
			maxVote = mapList[ret]
			maxLabel = ret			
	return maxLabel, maxVote

def check(data):
	num = len(data)
	label, num_label = majorLab(data)
#	print num_label
	if num == num_label:
		a = 1
	else:
		a = 0
	return a, label

def buildTree(data, n):
	isOneFeat, label = check(data)
#	print n, isOneFeat
	if n == 0 or isOneFeat == 1:
		return label
	bestFeat = chooseBestFeature(data)
	myTree = {bestFeat:{}}
#myTree[]
	S = set()
	for ret in data:
		feature = ret[bestFeat]
		if feature not in S:
			S.add(feature)
			q, w, e = clacNumSplit(data, bestFeat, feature)
			t = n - 1
			myTree[bestFeat][feature] = buildTree(e, t)
	return myTree
		
