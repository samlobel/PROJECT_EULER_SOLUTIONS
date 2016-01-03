

def mod_ten_for_number(n):
	a = n
	b = n - 1
	while b > 0:
		a = ((a * n) % 10000000000)
		b = b - 1
	return a

print mod_ten_for_number(1)



def sum_functions_up_to(n):
	s = 0
	for i in range(1,n+1):
		s = s + mod_ten_for_number(i)

	return s

print (sum_functions_up_to(1000) % 10000000000)
print sum_functions_up_to(10)

