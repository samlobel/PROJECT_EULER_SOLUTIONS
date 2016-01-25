

def make_n_fibs(n):
	if n < 1:
		raise Exception("Bad!")
	if n == 1:
		return [1]
	if n == 2:
		return [1,1]

	fibs = [1,1]

	for i in xrange(0,n-2):
		fibs.append(fibs[-1]+fibs[-2])

	return fibs


print len(str(make_n_fibs(4782)[-1]))