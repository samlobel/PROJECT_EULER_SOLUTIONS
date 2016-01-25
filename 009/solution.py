# Let's see if there's anything 


def solve():
	i_squares = [(i,i**2) for i in range(1000)]
	just_squares = [i**2 for i in range(1000)]
	square_set = set(just_squares)
	sq_map = {}
	for a in i_squares:
		sq_map[a[1]]=a[0]

	for p in range(2,1000):
		for q in range(p):
			if p**2 + q**2 in square_set:
				c = sq_map[p**2+q**2]
				print str(p) + " " + str(q) + " " + str(c)
				if not c:
					raise Exception("fuzzy logic")
				total = p + q + c
				if total == 1000:
					return (p,q,c,p*q*c,total)

print solve()


