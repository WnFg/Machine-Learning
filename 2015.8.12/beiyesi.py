import math

def clacNum(data):
	n = len(data)
	m = len(data[0])
	ans = []
	prob = []
	for i in range(m):
		ans.append({})
		for j in range(n):
			if data[j][i] not in ans[i].keys():
				ans[i][data[j][i]] = 0
			ans[i][data[j][i]] += 1
	for i in range(m):
		prob.append({})
		for j in ans[i].keys():
			prob[i][j] = float(ans[i][j])/n
	return 	prob	 

	  
def clacProb(data):
	dataLen = len(data)
	m = len(data[0]) - 1
	map_class = {}
	class_prob = {}
	for i in range(dataLen):
		if data[i][-1] not in map_class.keys():
			map_class[data[i][-1]] = []
		map_class[data[i][-1]].append(data[i][:m]) 
	xprob_y	= {} 
	for i in map_class.keys():
		class_prob[i] = float(len(map_class[i]))/dataLen
		xprob_y[i] = clacNum(map_class[i])
	return class_prob, xprob_y	

def f(cp, X, px_y):
#	log()
	i = 0
	ans = 0.0
	for x in X:
		ans += math.log(px_y[i][x], 2)
		i += 1
	return ans + math.log(cp, 2)	

def classifer(data, X):
	class_prob, xprob_y = clacProb(data)
	m = len(X)
	maxProb = -1.0
	for ck in class_prob.keys():
		ret = f(class_prob[ck], X, xprob_y[ck])
		if(ret > maxProb):
			maxProb = ret
			ans = ck
	return ans		

		
