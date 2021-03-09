from matplotlib import pyplot
import random 

xPoints= []
yPoints =[]

xPoints = range(1,100)
yPoints = [random.randint(1,25000) for _ in range(1,100)]

pyplot.plot(xPoints, yPoints)
pyplot.show()
