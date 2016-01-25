def faster_seive(max_num):
	num_list = [True for i in range(max_num)]
	num_list[0] = False
	num_list[1] = False

	for i, prime in enumerate(num_list):
		if prime:
			# print i
			for l in range(i*2, max_num, i):
				num_list[l] = False
	new_list = [i for (i, is_prime) in enumerate(num_list) if is_prime==True]
	# print num_list
	return new_list


def solve(max_num):
	primes = faster_seive(max_num)
	s = sum(primes)
	return s

print solve(2000000)