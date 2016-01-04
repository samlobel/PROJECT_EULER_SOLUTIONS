

# def prime_given_all_primes_below(set_of_primes, n):
	
# 	for num in set_of_primes:
# 		if n % num == 0:
# 			return False
# 	return True

# def all_primes_below(n):
# 	starter_set = set([2])
# 	for i in range(3,n,2):
# 		if prime_given_all_primes_below(starter_set, i):
# 			starter_set.add(i)
# 	return starter_set

# print all_primes_below(100)


def sieve(n):
	a = range(2, n)
	# return a
	# b = set(a)
	primes = []
	while len(a) > 0:
		b = a[0]
		isPrime = True
		for p in primes:
			if b % p == 0:
				isPrime = False
				break
		if isPrime:
			primes.append(b)
			newList = []
			for q in a:
				if not q % b == 0:
					newList.append(q)
			a = newList
	return primes



def isPrimeGivenSieve(s, n):
	for i in s:
		if i * i > n:
			return True
		if n % i == 0:
			return False
	return True


s = sieve(3939)

print isPrimeGivenSieve(s, 47)

def biggestInSum(n):
	s = sieve(n)
	print s
	a = 0
	m = 0
	for i in s:
		print a
		a += i
		if isPrimeGivenSieve(s, a):
			m = a
	return m


print biggestInSum(3945)






# print sum(sieve(3939))
