
# It's gotta start positive, meaning that b has to be > 0.
# Also, b has to be prime.

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



def given_a_b_find_n(a,b, prime_set):
	n = 0

	while True:
		ans = n**2 + a*n + b
		
		if ans not in prime_set:
			return (n - 1)
		n+=1


prime_list = prime_seive(2000000)
primes = set(prime_list)
# print primes

print "primes created"

plt1000 = prime_seive(1000)

ans = [[(given_a_b_find_n(a,b, primes),a,b) for a in range(-999, 1000)] for b in plt1000]
# sorted_ans = list(reversed(sorted(ans)))
flattened = [i for j in ans for i in j]
sorted_ans = list(reversed(sorted(flattened)))
print sorted_ans[0]
print sorted_ans[1]
real_ans =  sorted_ans[0]
print real_ans[1]*real_ans[2]

# print ans

# print given_a_b_find_n(1,41, primes)