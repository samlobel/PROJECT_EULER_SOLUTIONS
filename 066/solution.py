
from time import time


def prime_seive(max_num):
	num_list = [i%2==1 for i in range(max_num)]
	num_list[0] = False
	num_list[1] = False
	num_list[2] = True


	for i, prime in enumerate(num_list):
		if prime:
			# print i
			for l in range(i*3, max_num, i*2):
				num_list[l] = False
	new_list = [i for (i, is_prime) in enumerate(num_list) if is_prime==True]
	# print num_list
	return new_list



def create_non_square_list(max_n):
	l = [i for i in range(1, max_n+1) if i**0.5 != int(i**0.5)]
	return l


def satisfies_eq(x,y,d):
	ans = x**2 - (d * (y**2))
	if ans == 1:
		return (True, None)
	elif ans > 1:
		return (False, "GT")
	else:
		return (False, "LT")


def square_set(max_num):
	return set([i**2 for i in range(1, max_num+1)])


# print "making sqs"
# # square_set(int(10e7))
# print "made sqs"

def factorize(n):
	i = 2
	factors = []
	n_rem = n
	while True:
		if n_rem == 1:
			return factors
		if n_rem % i == 0:
			factors.append(i)
			n_rem = n_rem / i
		else:
			i+=1



def fast_find_xy(d):
	"""
	(n)(nd-2)=y^2
	(n)(nd+2)=y^2
	n is never going to be gotten by the other side, so it has to be 
	n^2. There's nothing about being prime needed!

	Not true. The reason it was true before is that d has to cleanly
	divide one or the other. But if it's not prime, they can split the
	factors. So it no longer has to be nd.

	But every number is n*c where c is the largest prime factor.
	And when you look at it like that:  Say d=c*e
	How about largest prime factor without a pair.

	(a)(a-2) = c*e*y^2			a/c*(a-2)=e*y^2. So, a must be a multiple of 
	c. Call a=nc 		and the analysis is the same as before. So, now,
	can the e have n as a factor?
	"""

	n=2
	while True:
		nsq = n**2
		v1 = nsq*(nsq-2)
		v2 = nsq*(nsq+2)
		v1srt = v1**0.5
		v2srt = v2**0.5
		if (v1srt == int(v1srt)):
			return n*d-1
		if (v2srt == int(v2srt)):
			return n*d+1
		n+=1

		# if (y1_sqd**0.5 == int(y1_sqd**0.5)):
		# 	print n
		# 	print y1_sqd
		# 	return n*d-1
		# if (y2_sqd**0.5 == int(y2_sqd**0.5)):
		# 	print n
		# 	print y2_sqd
		# 	return n*d+1

	# factors = factorize(d)
	# largest_factor = factors[-1]

	# print largest_factor

# fast_find_xy(63)
# fast_find_xy(99)
# fast_find_xy(100)

print fast_find_xy(2)

# def solve():
# 	for i 

def find_x_y_for_prime(d):
	"""
	One more time, because I'm stupid. If I look at (x+1)(x-1) + 1 -dy^2 = 1
	(x+1)(x-1)=dy^2
	(x+1)(x-1)/d=y^2.
	So, x+1=nd or x-1=nd. And, it's also y^2. Does that give me anything?
	So, we get rid of one prime factor. We're left with n, and (x-1).
	Let's say it was x+1=nd. So we have n(x-1)=y^2.


	Final thing, I want to see if n*(n*d+2) is prime or whatever.
	And since we have n*d-2, and it has to be a square, and we also have a 
	factor of n there, that means that 
	n*d+2 can't have a factor of n in it, which means that the n must
	pair with itself. So, n must be a square! That makes this a lot better.

	extract x from n.
	x=nd+1 or nd-1

	"""
	n = 1
	while True:
		# x1 = n * d * d + 1
		# x2 = n * d * d- 1
		"""(nd)(nd+2)/d   or   (nd)(nd-2)/d
			 n*(nd+2) = y^2
		"""
		y1_sqd = n**2*(n**2*d+2)
		y2_sqd = n**2*(n**2*d-2)
		if (y1_sqd**0.5 == int(y1_sqd**0.5)):
			print n
			print y1_sqd
			return n*d-1
		if (y2_sqd**0.5 == int(y2_sqd**0.5)):
			print n
			print y2_sqd
			return n*d+1

		n+=1
		# print n

# find_x_y_for_prime(61)
	# pass

# ps = prime_seive(1000)
# s = []
# for p in ps:
# 	print "\n"
# 	print p
# 	a = find_x_y_for_prime(p)
# 	s.append((a,p))
# 	print "\n"
# # print s
# s_s = list(reversed(sorted(s)))
# print s_s

def get_all(max_n):
	answers = []


def for_d_x_find_y(d,x):
	# Important things: If d is even, x MUST be odd. Because d*y^2 is even, and 1 is odd.
	# if D is odd, and y is odd, x must be even
	# if D is odd, and y is even, x must be odd.
	# If x and y share any factors, then you could factor them out
	# and it would say for example 3*(x^2-dy^2)=1, or x^2-dy^2=0.3333, which
	# is impossible. So x and y must be coprime
	# Now I'm getting to the meat of it.
	# Also, since D>1, y<x always.
	"""
	It looks like I'll never get the answer with computation. Is there a strictly
	dominating thing I can do? Is one answer always going to be bigger than
	another? If it has the smaller one as a factor, maybe? What happens when
	I prime factorize things? Especially D.

	I found a pretty neat property, that it looks like prime numbers usually have
	their x root as n*d-1=x. So 19 has 170, and 19*9-1=170.

	What happens if I put n*d-1 in for x? I get n^2d^2-2nd+1-dy^2=1,
	n^2d^2-2nd-dy^2=0
	divide by d, get n^2d-2n-y^2=0

	There's something more that I can't quite tease out. It's something
	to do with factors. Because 33 goes to 23,4. And 23 is +1 of 22, which is 2*11.
	and 44 is 199, which is 18*11+1
	So, it's always within 1 of something, but I don't know what...
	Is y predictable at all? I don't think so.


	Let's say that d is prime. And let's say that x is n*d + or - 1
	29: (9801, 1820)
	9802/29= 338
	338 = 2,13,13
	In other words, it's y=2*13^2. And, 
	9802=2,13,13, 29.
	and 1820 is 
	1820:2,2,5,91
	and 9801=3,3,3,3,11,11. But maybe importantly, it's a square.
	

	Let's do 13.
	13: (649, 180)
	


	The plot thickens.


	I should have thought about this more before starting. That's probably true
	with a lot of things. If I replace x with either a+1 or a-1, it becomes
	a lot cleaner.
	a^2 + 2a + 1 -dy^2 = 1  -->    a^2 + 2a = dy^2  -->  a^2/d+2a/d = y^2
	In other words, it looks sort of like d must divide a. Is there any way
	that d doesn't divide a but it divides a^2+2a? Well, it's really 
	(a)(a+2), and it needs to divide one of them. Which is really nice, because
	a is one less than x, and this is one less or one more than a, which is the
	empirical thing I thought before. In other words, we can really well narrow
	down values of x, then find y, and see if it's an integer! That's not so bad
	is it.

	It's more of a way to go from d to x, not the other way around. 
	So, if d is anything, a * (a+2) has got to divide it, and then maybe we
	can find a y.

	It's easy if d is prime. Then you just look at multiples of d for either
	a or a+2. So, we can really call those (x-1)(x+1). 
	n*d = x + 1  or n*d = x-1. Then you solve for y.

	If it's not prime, you've got the scary problem that some factors could come
	from one and some from the other. Maybe I should just do the prime ones
	as a start.

	"""
	pass

def better_find_xy(d):
	if d**0.5 == int(d**0.5):
		raise Exception("calling on square number " + str(d))
	x=1
	y=1
	i=0
	while True:
		i+=1
		if i > 100000:
			return float('inf'), float('inf')
		# if i %10000 == 0:
		# 	print x,y
		# sat, where = satisfies_eq(x,y,d)
		# if sat:
		# 	return x,y
		# if where='GT'
		ans = x**2 - (d * (y**2))
		if ans == 1:
			return x,y
		elif ans < 1:
			# print "x"
			x+=1
		else:
			# print "y"
			y+=1





def for_d_find_x_y(d):
	if d**0.5 == int(d**0.5):
		raise Exception("calling on square number " + str(d))

	x = 1
	y = 1
	while True:
		x += 1
		y=0
		while True:
			sat, where = satisfies_eq(x,y,d)
			if sat:
				return x,y
			if where=='GT':
				y+=1
				continue
			elif where=='LT':
				break
			else:
				raise Exception("WHAAT?")

# print for_d_find_x_y(101)

def create_dict(up_to_d):
	d = {}
	for i in create_non_square_list(up_to_d):
		print i
		x,y = better_find_xy(i)
		# print "d: %d, x: %d, y: %d" % (i,x,y)
		d[i] = (x,y)
	return d


# print create_dict(61)



def test():
	t_1 = time()
	print "starting first"
	for_d_find_x_y(29)
	t_2 = time()
	print "done with first, starting second"
	better_find_xy(29)
	t_3 = time()
	print "time for old one: " + str(t_2 - t_1)
	print "time for new one: " + str(t_3 - t_2)

# test()




# print create_non_square_list(10)
# print create_non_square_list(100)


