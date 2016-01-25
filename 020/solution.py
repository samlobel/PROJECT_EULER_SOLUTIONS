


def factorial(n):
	mult = 1
	for i in range(1,n+1):
		mult *= i
	return mult


num = factorial(100)

str_num = str(num)

sum_digits = 0
for i in str_num:
	sum_digits += int(i)

print sum_digits

