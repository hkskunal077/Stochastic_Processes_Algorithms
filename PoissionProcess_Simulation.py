import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
import seaborn as sns
from numpy import random
import math


def calculatepmf(k,lam,t):
	return (math.exp(-lam*t))*((lam*t)**k)/(math.factorial(k))
data_poisson = poisson.rvs(mu = 5, size = 50)
#mu is lambda of the equation
#print(data_poisson)
print("\nThese are the units of time or time stamps\n")
time_stamps = np.arange(0,50,1)
print(time_stamps)
print("These are the number of arrivals during that latest time interval")
print("\n",data_poisson)

plt.figure(figsize = (20,10))
plt.xticks(time_stamps)
plt.plot(time_stamps, data_poisson, color = 'green', marker = 'o', linestyle = 'dashed')
plt.xlabel('TIME UNITS')
plt.ylabel('NO OF ARRIVALS IN THAT INTERVAL')
plt.show()

sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')
plt.show()
print("\n\n")
print("For Finding probability in Poisson (f(k,lam,t) = (e^-(lam*t))*((lam*t)^n)/(n!)")
#print(calculatepmf(3,5,3))
print("\nLet us take lambda = 5 and K = 3 and fin arrivals in unit time length\n")
Y = poisson(5) 
print (Y.pmf(3))       
      
