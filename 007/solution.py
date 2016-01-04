

def first_num_primes(num):
	list_len = 0
	s = []
	i = 2
	while True:
		is_prime = True
		for n in s:
			if i % n == 0:
				is_prime = False
				break
		if is_prime:
			s.append(i)
			list_len += 1
			# print s
		if list_len == num:
			return i
		i += 1


print first_num_primes(10001)
