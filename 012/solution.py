


def create_triangle_num(n):
	return (n * (n+1))/2

def get_factors(num):
	to_return = []
	for i in xrange(1,int(num**0.5)):
		if num % i == 0:
			to_return.append(i)
			other = int(num/i)
			to_return.append(other)
	return to_return


def solve():
	for i in range(100000):
		t_n = create_triangle_num(i)
		# print t_n
		factors = get_factors(t_n)
		# print factors
		print len(factors)
		if len(factors) > 500:
			print factors
			print len(factors)
			print i
			print t_n
			return

solve()