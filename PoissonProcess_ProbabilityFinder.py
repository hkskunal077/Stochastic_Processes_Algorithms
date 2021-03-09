import numpy as np 
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
import math

def calculatepmf(k,lam,t):
	return (math.exp(-lam*t))*((lam*t)**k)/(math.factorial(k))

x_values = random.poisson(lam =2, size = 50)
print(x_values)

sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')
plt.show()


print("For Finding probability in Poisson (f(k,lam,t) = (e^-(lam*t))*((lam*t)^n)/(n!)")

print(calculatepmf(5,5,3))
