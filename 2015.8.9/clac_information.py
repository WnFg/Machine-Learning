import math

def clac_Ent(data):
	sum = len(data)
	map_data = {}
	for i in range(sum):
		if data[i] not in  map_data.keys():
			map_data[data[i]] = 0
		map_data[data[i]] += 1
	shannonEnt = 0.0
	for key in map_data:
		prob = float(map_data[key])/sum
		shannonEnt -= prob*math.log(prob,2)
	return shannonEnt 

def clacNumSplit(data, i, value):
	num = 0
	subLabels = []
	subData = []
	for ret in data:
		if ret[i] == value:
			num += 1
			subLabels.append(ret[-1])
			subData.append(ret[:i] + ret[i+1:])
	return num, subLabels, subData
