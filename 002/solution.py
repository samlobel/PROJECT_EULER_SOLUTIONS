


def make_fib_list_less_than(num):
	s_1 = 1
	s_2 = 2
	to_return = [1,2]
	while True:
		s_3 = s_2 + s_1
		if s_3 > num:
			break
		to_return.append(s_3)
		s_1 = s_2
		s_2 = s_3
	print to_return
	return to_return

def sum_even_fibs(num):
	fibs = make_fib_list_less_than(num)
	evens = [i for i in fibs if i %2==0]
	s = sum(evens)
	print s
	return s


sum_even_fibs(4000000)
