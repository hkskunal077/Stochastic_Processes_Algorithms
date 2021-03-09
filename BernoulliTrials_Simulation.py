import numpy
from scipy.stats import binom

#Number of trials 
n = float(input("Enter number of Bernoulli Trials to be performed\n"))

prob_success = [0.3, 0.6, 0.9]
for p in prob_success:
  print("\nProbability of Success ",p,"Case" )
  #These are independent of rvs but only depends on probability of success and number of trials 
  theoretical_mean = n*p 
  theoretical_variance = n*p*(1-p)
  print("Theoretically Calculated Mean and Variance are",theoretical_mean," and ",theoretical_variance, "\n")

  #Calculating using Library and Verifying
  random_vars = [numpy.random.binomial(n,p) for i  in range(1000000)]
  library_mean = numpy.average(random_vars)
  library_variance = numpy.var(random_vars)
  print("Calculated Mean and variance are",library_mean," and ",library_variance,"\n")

  #relative error calculation in percentage
  error_mean = ((theoretical_mean-library_mean)/theoretical_mean)*100
  error_variance = ((theoretical_variance-library_variance)/theoretical_variance)*100

  print("Errors in Mean and Variance are ", error_mean," and ", error_variance,"\n\n")





