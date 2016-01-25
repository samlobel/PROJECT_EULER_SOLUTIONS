

"""
This shouldn't be too hard. For each denominator, we can find 
a minimum, we can find a maximum, and we can filter if two things
have common factors.
"""


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


def is_coprime(a,b):
	af = factorize(a)
	for f in af:
		if f % b == 0:
			return False
	return True
		# bf = set(factorize(b))
	# c = af.intersection(bf)
	# if len(c):
	# 	return False
	# else:
	# 	return True

# print is_coprime(27,37)


def find_min_max(den):
	bottom = den / 3.0
	top = den / 2.0
	toreturn_b = None
	toreturn_t = None
	# print bottom
	# print int(bottom)
	# if bottom == int(bottom):
	# 	toreturn_b = int(bottom) + 1
	# else:
	# 	toreturn_b = int(bottom)
	toreturn_b = int(bottom) + 1
	# if top == int(top):
	# 	toreturn_t = int(top) -1
	# else:
	# 	toreturn_t = int(top)

	toreturn_t = int(top) - 1

	return toreturn_b,toreturn_t

# print find_min_max(100)

def r_primes_in_between(den):
	mi,ma = find_min_max(den)
	
	to_return = [True for i in range(mi, ma+1)]
	for i in range(mi, ma+1):
		if is_coprime(i, den):
			# to_return.append(i)
			to_return[i] = False
		# to_return.append((i + 0.0)/ den)
	return to_return


# print r_primes_in_between(100)


def count_total(top_num):
	i = 0
	k = []
	for j in range(4,top_num+1):
		betweens = r_primes_in_between(j)
		len_b = len(betweens)
		i+= len_b
		print j
		# k.extend(betweens)
	return i

a =  count_total(12000)
print a
print len(a)
s = set(a)
print len(s)







