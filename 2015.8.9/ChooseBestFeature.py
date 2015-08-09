from clac_information import *

def chooseBestFeature(data):
	sumData = len(data)
	sumFeature = len(data[0]) - 1
#Labels = []
#	for ret in data:
#		Labels.append(ret[-1])
#	oldEntropy = clacEnt(Labels)
	maxEntropy = -1
	for i in range(sumFeature):
		newEntropy = 0.0
		featureList = [ret[i] for ret in data]
		valueSet = set(featureList)
		for value in valueSet:
			subNum, subList, subData = clacNumSplit(data, i, value)
			prob = float(subNum)/float(sumData)
			newEntropy += prob*clac_Ent(subList)
		if maxEntropy == -1 or maxEntropy < newEntropy :
			maxEntropy = newEntropy
			bestFeat = i
	return bestFeat		
