



"""
The general idea here is that I need to first find the percent chance
that one of the digits has a 1 in it, which is (1-0.5^N) where N is the
number of things that have been OR operated together.
Then, given that chance, I find the likelihood they all are, which is
(1-0.5^N)^32

But the confusing part, which I just though of, is that it's not
that there's a 1, it's that they're all zero and the last one is a
1. In other words, there's only one configuration that works.
So, it's easy. It's just 0.5^n. So, it becomes (0.5^n)^32 is the chance
at any given n. So, expectation value is sum([n*(0.5**n)**32 for n in range(max_x)])

What's wrong with this? 

The chance of it being the first one is 0.5^32.
Oh, I guess the chance of it being the second one and not the first one is

So, the chance of being some N is that all but one of them has at least one
1 in it, and then one has all zeros and then a 1.
In other words, it's 32 * (1-0.5^N)^31 * (0.5^N) chance it's n.


One more time through the logic. We want to check how likely it is that it's the
first time you have all ones. So it's the chance that 31 of them have a one 
somewhere, and one of them has all zeros and then a 1.
So, the first one should have 31 spots that have a 1, which is 0.5^31. And then
one spot that also has a 1. I think maybe it's because the only 1 option also
fits with the other.


Another way to do it is that the chance is (1 - 0.5**N)^32 - (chance before)



"""


def single(n, so_fars):
	n_part = (1-0.5**n)**32
	new = n_part - sum(so_fars)
	so_fars.append(new)

so_fars = []
for i in range(0,100):
	single(i, so_fars)
print so_fars
print sum(so_fars)

expected_vals = [p*prob for (p,prob) in enumerate(so_fars)]
print expected_vals
print sum(expected_vals)

# def single(n):
# 	return n*(0.5**n)**32

# def solve(to_n):
# 	return sum([n*(0.5**n)**32 for n in range(to_n+1)])


# def single(n):
# 	return 32.0*((1-(0.5**n))**31)*(0.5**n)

# a = []
# print 0.5**32
# print "\n"
# for i in range(1,100):
# 	r = single(i)
# 	print r
# 	a.append(r)

# print sum(a)

# for i in range(1,100):
# 	print single(i)
# print solve(1)