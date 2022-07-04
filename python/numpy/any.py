from numpy import random as ran
from matplotlib import pyplot
b = ran.randint(1,5,3)
print(b)
a = ran.uniform(1,45,6)
print(a)
pyplot.hist(a)
pyplot.show()
