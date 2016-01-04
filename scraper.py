import os
import requests
def make_number_three_digits(num):
	int_num = int(num)
	if num < 0:
		raise Exception("Bam!")
	if num < 10:
		val =  "00" + str(int_num)
		return val
	if num < 100:
		val = "0" + str(int_num)
		return val
	if num < 1000:
		return str(int_num)

	raise Exception("Boom!")


def test():
	for i in range(1,500):
		str_num = make_number_three_digits(i)
		print str_num

# test()

def activate():
	for i in range(1,20):
		str_num = make_number_three_digits(i)
		if not os.path.isdir(str_num):
			os.makedirs(str_num)
		r = requests.get('https://projecteuler.net/problem=' + str(i))
		t = r.text
		print t
		a = open(os.path.join(str_num,'HTML.html'), 'w')
		a.write(t)
		a.close()

activate()

		
