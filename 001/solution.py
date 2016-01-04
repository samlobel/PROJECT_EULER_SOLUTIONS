

def solve():
	mults = [i for i in range(1000) if i%3==0 or i%5==0]
	s = sum(mults)
	print s


solve()