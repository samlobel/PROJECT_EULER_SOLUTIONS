


# def prime_sieve(max_num):
# 	primes = 
# 	start = 2

from math import sqrt

# def largest_prime_factor(num):
# 	# square_root = int(sqrt(num))
# 	# print square_root
# 	i = num - 2
# 	while i > 0:
# 		if num % i == 0 :
# 			# print num
# 			return i
# 		i -= 1
# 		if i % 1000 == 0:
# 			print i
# 			pass


def largest_prime_factor(num, i):
	# i = 2
	if i >= num:
		return i
	while True:
		if num % i == 0:
			print i
			divided = num / i
			return largest_prime_factor(divided, i)
		i += 1

largest = largest_prime_factor(13195, 2)
print "largest is " + str(largest)


largest = largest_prime_factor(600851475143, 2)
print "largest is " + str(largest)




# print largest_prime_factor(600851475143)


