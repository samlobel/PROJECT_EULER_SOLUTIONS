

"""
This looks easy as hell
"""


def create_constant(max_digit):
	a = [str(i) for i in range(1, max_digit+1)]
	b = ''.join(a)
	return b

# a = create_constant(1000000)

def solve():
	a = create_constant(1000000)
	ans = int(a[0])*int(a[9])*int(a[99])*int(a[999])*int(a[9999])*int(a[99999])*int(a[999999])
	print ans
	return ans
# print a

solve()

