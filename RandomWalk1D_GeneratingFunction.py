# import random
# import numpy as np 
# from matplotlib import pyplot as plt

# prob_set = [0.4, 0.2, 0.4]
# start_j = 0
# sum_value = 0
# x_array = [i for i in range(101)]

# y_array = []
# step_pos = 0
# step_no = 0
# step_neg = 0

# for i in range(len(x_array)):
# 	y_inst = random.choice([-1,0,1])
# 	if y_inst == 1:
# 		step_pos += 1
# 	elif y_inst == -1:
# 		step_neg += 1
# 	else:
# 		step_no += 1

# 	y_array.append(sum_value + y_inst)
# 	sum_value += y_inst

# plt.plot(x_array, y_array, linestyle = '--', marker = 'o', color = 'green')
# plt.xlabel('Nth Step')
# plt.ylabel('Random Walk in 1-D integer lattice (Unrestricted)')
# plt.show()


#Now according to Central Limit Theorem
#For large number of movements, process can be modelled as 
#a Bell Curve or Normal Distribution 
# import math
# def prob(n,k):
# 	req = math.erf((k+1)/math.sqrt(n)) - math.erf((k-1)/math.sqrt(n))
# 	print(math.erf((k+1)/math.sqrt(n)))
# 	print()
# 	print(math.erf((k-1)/math.sqrt(n)))
# 	return req
# print(prob(45,10))

#Now according to theory of 
#Probability Generating Function 
from math import comb
def gfunction(p,q,z):
	
	return p*z + (1-p-q) + q*(z**(-1))

def generatingfunc_prob(p,q,n,k,z):
	#using probability generating function 
	Gz = gfunction(p,q,z)
	#From this calculated Gz we need the 
	#Coefficients of (Z^K)*(S*N)
	#Which will be (P^N)(NC((N-K)/2))
	r = int((n-k)/2)
	ReqCoeff = pow(p,n)*(comb(n, r))
	print("The probability of being at a state ",k, " after ", n, " steps is ", ReqCoeff)

generatingfunc_prob(0.4,0.4,45,10,2)
#generatingfunc_prob(0.4,0.4, 10, 10,2)
