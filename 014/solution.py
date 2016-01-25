

def make_chain(n):
	curr = n
	chain = set([curr])
	while curr != 1:
		# print curr
		if curr % 2 == 0:
			curr = int(curr / 2)
		else:
			curr = 3 * curr + 1
		chain.add(curr)
	return chain


# print make_chain(13)


def test_chains(max_num):
	should_test = [True for i in range(max_num)]
	should_test[0] = False
	length_dict = {}
	for i in reversed(range(max_num)):
		test_this = should_test[i]
		if test_this:
			chain = make_chain(i)

			for l in chain:
				if l < max_num:
					should_test[l] = False

			len_chain = len(chain)
			length_dict[i] = len_chain
	return length_dict

l_d = test_chains(1000001)

m = max([(l_d[k], k) for k in l_d])
print m





