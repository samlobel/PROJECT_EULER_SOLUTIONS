


# GAMEPLAN:
# First, only examine things that are between 2/7 3/7. That limits things a good deal.
# That means that I can multiply things by n/n and say, for this denominator, I
# only need the closest ones to 3/7.

# This isn't that hard. I really only need the one that's less.

# def factorize(a):
# 	factors = []
# 	while True:


# def relatively_prime(a,b):
# 	pass

def find_smallest_that_is_less_than(den):
	if den % 7 == 0:
		# return (0, den)
		return False
	round_down = int(den*3/7)
	return ((round_down + 0.0)/den, round_down, den)

def test():
	a = [find_smallest_that_is_less_than(i) for i in range(10,100)]
	print a

def list_to(max_den):
	a = []
	for i in xrange(10, max_den):
		smallest = find_smallest_that_is_less_than(i)
		if smallest:
			a.append(smallest)
	return a


def solve(max_den):
	l = list_to(max_den)
	l_filtered = [i for i in l if i]
	s = list(reversed(sorted(l_filtered)))
	return s

print solve(1000001)[0:100]
print (3.0/7)



