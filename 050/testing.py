


from time import time
from random import random

a = time()

for i in xrange(10):
	x = [random() for j in range(1000000)]


print str(time() - a)