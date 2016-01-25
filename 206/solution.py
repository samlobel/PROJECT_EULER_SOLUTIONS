"""
1_2_3_4_5_6_7_8_9_0

The first thing is, if x^2 ends in a zero and it's a square, x has to
end in a zero. And the first blank must be a zero as well. Then,
if it ends in a 9, it's gotta be a 3 or a 7. 
8_9, ending in a 3 or a 7 ... we've got **(3,7) Can the last digit matter?
103*103=10609. In other words, yes it can. But the digit after it can't.

So, we've got 200 things to try, most of which won't work.


Also, it's a 20 digit number. And I know it ends in a zero. I could just test 
the possibilities.

The first digit effects the first one. The second digit can't effect the first.
The third can't effect the second. 
So, we know it's a ten digit number. I should do it in spurts of 0-100, and see
how it effects the two digits.

The second digit can't effect the first. The third can't effect the second

"""

import re


def match_n(a, n):
	# print n
	# print a
	l = ['1','\d','2','\d','3','\d','4','\d','5','\d','6',\
	'\d','7','\d','8','\d','9','\d','0']
	# if n > len(l):
	# 	raise Exception("too big n")

	l_r = list(reversed(l))
	l_s_r = l_r[0:n]
	l_s = list(reversed(l_s_r))
	s = ''.join(l_s)
	s = '.*'+s+'$'
	# print s
	if re.match(s, a):
		return True
	else:
		return False


for i in range(1,11):
	match_n('1',i)

# print match_n('1155667789900',5)


def recurse(str_so_far):
	if len(str_so_far) == 10:
		str_int = int(str_so_far)
		sq = str_int**2
		if match_n(str(sq), 20):
			print str_so_far
		# print str_so_far
		return 
	for i in range(10):
		new_str = str(i) + str_so_far
		str_int = int(new_str)
		sq = str_int**2
		if match_n(str(sq), len(new_str)):
			recurse(new_str)

recurse('')


def ends_in_three():
	for i in range(0,99):
		j = i*10+3
		k=j*j
		l = int((k % 1000) / 100)
		if l == 8:
			print (j,k)


def ends_in_seven():
	for i in range(0,99):
		j = i*10+7
		k=j*j
		l = int((k % 1000) / 100)
		if l == 8:
			print (j,k)


# ends_in_three()
# ends_in_seven()

def get_min():
	a = 1020304050607080900
	b = a**0.5
	return int(b)

def get_max():
	a = 1929394959697989990
	b = a**0.5
	return int(b)

# print get_min()
# print get_max()

# print get_max() - get_min()


def does_match(a):
	# match_string = '^1\d2\d3\d4\d5\d6\d7\d8\d9\d0$'
	match_string = '^1\d2\d3\d4\d5\d6\d7\d8\d900$'
	# match_one = '^1\d2\d3\d4\d5\d6\d7\d8\d900$'
	return re.match(match_string, str(a))

# if does_match(1020304050607080900):
# 	print "first matches"

# if does_match(2020304050607080900):
# 	print "second matches"


def solve():
	min_num = get_min()
	max_num = get_max()
	print min_num
	print max_num
	return
	min_num_ten = int(min_num / 100) * 100
	for i in range(min_num_ten, max_num, 100):
		a = i + 30
		b = i + 70
		print a
		print b

# solve()




