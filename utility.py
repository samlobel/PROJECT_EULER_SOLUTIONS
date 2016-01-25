

def make_fib_list_less_than(num):
	s_1 = 1
	s_2 = 2
	to_return = [1,2]
	while True:
		s_3 = s_2 + s_1
		if s_3 > num:
			break
		to_return.append(s_3)
		s_1 = s_2
		s_2 = s_3
	print to_return
	return to_return


def make_n_fibs(n):
	if n < 1:
		raise Exception("Bad!")
	if n == 1:
		return [1]
	if n == 2:
		return [1,1]

	fibs = [1,1]

	for i in xrange(0,n-2):
		fibs.append(fibs[-1]+fibs[-2])

	return fibs



def factorial(n):
	mult = 1
	for i in range(1,n+1):
		mult *= i
	return mult


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





if __name__ == '__main__':
	pass
	# print prime_seive(2000)
	# print factorize(1004)
	# print len(prime_seive(5000000))
	# print make_n_fibs(10)
