


def sum_of_squares(max_val):
	first = range(1, max_val+1)
	squares = [i*i for i in first]
	s = sum(squares)
	return s

def square_of_sums(max_val):
	first = range(1, max_val+1)
	s = sum(first)
	squared = s*s
	return squared

diff = square_of_sums(100) - sum_of_squares(100)

print diff
