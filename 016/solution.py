
# pretty easy in python
def solve():
	num = 2**1000
	str_num = str(num)
	a = reduce(lambda x,y:int(x)+int(y), str_num, 0)
	print a

solve()