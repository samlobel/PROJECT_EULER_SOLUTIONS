

def is_palindrome(num):
	str_num = str(num)
	l_num = len(str_num)
	for i in range(l_num):
		if str_num[i] != str_num[l_num - i - 1]:
			return False
	return True


print is_palindrome(1000)
print is_palindrome(1001)

def brute_force_palindrome():
	palindromes = []
	for i in xrange(1000):
		for j in xrange(1000):
			mult = i * j
			if is_palindrome(mult):
				palindromes.append(mult)
	sort = sorted(palindromes)
	print sort
	last = sort[-1]
	print last
	return last


brute_force_palindrome()
