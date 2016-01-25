from time import time
def find_primes_below(max_num):
	prime_list = []
	first = 2
	for i in xrange(2, max_num):
		if i % 1000 == 0:
			print "On " + str(i)
		is_prime = True
		for prime in prime_list:
			if i % prime == 0:
				is_prime = False
				break
		if is_prime:
			prime_list.append(i)
	return prime_list


def fast_find_primes_below(max_num):
	prime_list = []
	num_list = range(2, max_num)
	new_num_list = []
	i = 0
	start = time()
	while len(num_list):
		if i % 100 == 0:
			start = time()
		if (i + 1) % 100 == 0:
			total = time() - start
			print "milliseconds for 100: " + str(total)
		i += 1
		print "length left: " + str(len(num_list))
		first = num_list[0]
		# print first
		prime_list.append(first)
		new_num_list = [num for num in num_list if num%first!=0]
		# for nums in num_list:
		# 	if nums % first ==0:
		# 		num_list.remove(nums)
		num_list = new_num_list
		new_num_list = []
	return prime_list


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

# print faster_seive(1000000)

# def solve(max_num):
# 	prime_list = faster_seive(max_num)
# 	print prime_list[-1]
# 	print "length: " + str(len(prime_list))
# 	for i in xrange(len(prime_list)):
# 		s = sum(prime_list[0: i])
# 		if s > max_num:
# 			print s
# 			print i
# 			return


def longest_chain_given_prime(prime_list, target, starting_point):
	# starting_point = starting_point or 1
	start = 0
	end = 1
	max_start = 0
	max_end = 0
	max_diff = 0
	# sum_sublist = sum(prime_list[start:end])
	sum_sublist = prime_list[0]
	while True:
		# sum_sublist = sum(prime_list[start:end])
		if sum_sublist == target:
			if end - start > max_diff:
				print prime_list[start:end]
				max_diff = end - start
				max_end = end
				max_start = start
				# print (max_start, max_end)
			end += 1
			start += 1
			sum_sublist += prime_list[end]
			sum_sublist -= prime_list[start-1]
		if sum_sublist < target:
			end += 1
			sum_sublist += prime_list[end]
		if sum_sublist > target:
			start += 1
			sum_sublist -= prime_list[start-1]
		if prime_list[end] >= target:
			break
	return (max_diff, max_start, max_end, target)


def solve(max_num):
	prime_list = faster_seive(max_num)
	print prime_list
	# answer = max([longest_chain_given_prime(prime_list, v) for v in prime_list])
	real_longest = (0,0,0,0)
	for p in reversed(prime_list):
		print p
		longest = longest_chain_given_prime(prime_list, p, 1)
		print longest
		real_longest = max(longest, real_longest)
	print real_longest
		

	# print answer
	# for i in range(len(prime_list)):
	# 	l = longest_chain_given_prime(prime_list, prime_list[i])
	# 	print l

# solve(100)


def test_chain_length(l, prime_list, prime_set):
	if l >= len(prime_list):
		# raise Exception("Bad!")
		return (0,0,0,0)
	first = 0
	last = l
	largest = prime_list[-1]
	l_chain = sum(prime_list[first:last])
	while last < len(prime_list):
		if l_chain > largest:
			return (0,0,0,0)
		if l_chain in prime_set:
			return (l, first, last, l_chain)
		l_chain -= prime_list[first]
		l_chain += prime_list[last]
		first += 1
		last += 1
	return (0,0,0,0)


def solve_fast(max_num):
	prime_list = faster_seive(max_num)
	prime_set = set(prime_list)
	answer_list = []
	for i in range(2, 1000):
		# print i
		answer_list.append(test_chain_length(i, prime_list, prime_set))
	print max(answer_list)



solve_fast(1000000)
	# if first_l in prime_set:
	# 	return ()

# def test():
# 	prime_list = faster_seive(1000000)
# 	s = sum(prime_list[0:547])
# 	print s

# test()
	

		# s = sum(prime_list[start:end])
		# if s==target:
		# 	max_end = end
		# 	continue




# Looks like 547 is the longest the prime chain could possibly be. That's how many continuous things go over the limit starting from the beginning.


# def test:

# solve(1000000)



# def solve(max_num):
# 	prime_list = find_primes_below(max_num)
# 	prime_set = set(prime_list)
# 	print len(prime_list)
# 	print prime_list[0:10]


# solve(1000000)

# primes = fast_find_primes_below(1000000)
# print primes
# print len(primes)

# for i in range(1000000):
	# print i
# I think this is the fastest way to calculate primes

