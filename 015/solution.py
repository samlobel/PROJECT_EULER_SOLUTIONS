

"""
This is a fun one to do in your head. There's a neat way to think about 
problems like this. There must be 40 moves, 20 of 1 type and 20 of another.
So, it becomes the question, if I had 40 buckets, how many ways could I put
20 beads in them? The other 20 beads are sort of forced where they go.


So, it's just 40*39*38*37 ...*21 is the ways I can drop them, and then
there are 2^20 inconsistancies.
40!/(20!)^2

"""

def factorial(n):
	m = 1
	for i in range(1,n+1):
		m*=i
	return m

# print factorial(5)

def solve(r):
	return factorial(r*2)/(factorial(r)**2)
	# mult = 1
	# for i in range(r, r*2):
	# 	print i
	# 	mult*=i
	# return mult

print solve(20)