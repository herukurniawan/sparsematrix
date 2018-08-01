import random
import numpy as np

size = 5
ub = 7
def ranz():
	return [random.randint(1,100) for i in range(0,size)]

def zero():
	return [0]*size
c = ranz()+zero()+zero()+zero()+ranz()

outer = []
counter = 0
for j in range(0,ub*size):
	inner = []
	if j%size == 0:
		pola = [0,ub-1]
		pola.append(counter)
		counter += 1
	for i in range(0,ub):
		if i in pola:
			inner += ranz()
		else:
			inner += zero()
	outer.append(inner)

for i in range(0,len(outer)):
	outer[i][i] = -1 * outer[i][i]

outer = np.array(outer)
sparsity = 1.0 - float(np.count_nonzero(outer))/outer.size
print sparsity
print outer

