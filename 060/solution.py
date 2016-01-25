

def prime_seive(max_num):
	num_list = [True for i in range(max_num)]
	num_list[0] = False
	num_list[1] = False

	for i, prime in enumerate(num_list):
		if prime:
			# print i
			for l in range(i*2, max_num, i):
				num_list[l] = False
	new_list = [i for (i, is_prime) in enumerate(num_list) if is_prime==True]
	# print num_list
	return new_list


def is_prime_given_sets(target, primes, prime_set, big_primes, big_not_primes):
	biggest = primes[-1]
	if target > biggest ** 2:
		return False
	if target < biggest:
		return target in prime_set
	else:
		# print "too big for wonderland"
		if target in big_primes:
			return True
		if target in big_not_primes:
			return False
		for p in primes:
			if target % p == 0:
				big_not_primes.add(target)
				return False
		big_primes.add(target)
		print "sneakily caught " + str(target)
		return True


		# for p in primes:
		# 	if target % p == 0:



def make_pairs(max_num):
	print "seiving"
	primes = prime_seive(max_num)
	print "done seiving"
	print "starting rest"
	# print primes
	last_digit_num = primes[-1]
	# print last_digit_num
	# good_max = 10**(last_digit_num / 2)
	# print good_max
	p_set = set(primes)
	pairs = []
	big_primes = set()
	big_not_primes = set()
	pair_set = set()
	for p in primes:
		for q in primes:
			# if q > good_max:
			# 	break
			if q > p:
				break
			p_str = str(p)
			q_str = str(q)
			one_way = p_str + q_str
			other_way = q_str + p_str
			one_way_int = int(one_way)
			other_way_int = int(other_way)
			# if (one_way_int > last_digit_num) or (other_way_int > last_digit_num):
			# 	break
			if is_prime_given_sets(one_way_int, primes, p_set, big_primes, big_not_primes) \
				and is_prime_given_sets(other_way_int, primes, p_set, big_primes, big_not_primes):
				pair_set.add((q,p))
			# if one_way_int in p_set and other_way_int in p_set:
			# 	pairs.append((q,p))
		# if p > good_max:
		# 	break
	# print pairs
	print "ending rest"
	pairs = sorted(list(pair_set))
	return pairs
	# return pairs


# up_to = 1000000

# seived = prime_seive(up_to)
# print len(seived)

# paired =  make_pairs(up_to)
# s_pairs = sorted(paired)
# # print s_pairs


def pairs_to_filtered_list(pairs):
	s = set()
	for p1,p2 in pairs:
		s.add(p1)
		s.add(p2)
	l = list(s)
	l_s = sorted(l)
	return l_s

# f_l = pairs_to_filtered_list(s_pairs)
# print f_l
# print len(f_l)

def pairs_to_dict(pair_list):
	dict_to_return = {}
	for pair in pair_list:
		p1,p2 = pair
		if p1 not in dict_to_return:
			dict_to_return[p1] = set()
		if p2 not in dict_to_return:
			dict_to_return[p2] = set()
		dict_to_return[p1].add(p2)
		dict_to_return[p2].add(p1)
	return dict_to_return

# d = pairs_to_dict(s_pairs)
# print "\n\n\n"
# print d

def dict_up_to(max_num):
	pairs = make_pairs(max_num)
	# print pairs
	d = pairs_to_dict(pairs)
	return d


def dict_to_triset_list(pair_dict):
	tri_dict = {}
	tri_list = []
	for key in pair_dict:
		key_set = pair_dict[key]
		for key_pairs in key_set:
			those_sets = pair_dict[key_pairs]
			for t in those_sets:
				if t in key_set:
					tri = (key, key_pairs, t)
					tri_list.append(tri)
	return tri_list





# tri_l = dict_to_triset_list(d)

# def filter_pairs_by_count(pairs, min_n):
# 	counter = {}
# 	for p1,p2 in pairs:
# 		if p1 not in counter:
# 			counter[p1]=0
# 		if p2 not in counter:
# 			counter[p2]=0
# 		if 

def filter_dict_by_size(d, min_size):
	new_d = {}
	for k in d:
		if len(d[k]) >= min_size:
			new_d[k] = d[k]
	return new_d



def tri_l_to_filtered_list(tri_l):
	s = set()
	for a in tri_l:
		s.add(a[0])
		s.add(a[1])
		s.add(a[2])
	return sorted(list(s))

# f_l_tri = tri_l_to_filtered_list(tri_l)
# print len(f_l_tri)

# print f_l_tri

def triset_list_to_tuple_dict(tri_l):
	d = {}
	for p1,p2,p3 in tri_l:
		if p1 not in d:
			d[p1] = set()
		if p2 not in d:
			d[p2] = set()
		if p3 not in d:
			d[p3] = set()
		t1 = tuple(sorted((p1,p2)))
		t2 = tuple(sorted((p1,p3)))
		t3 = tuple(sorted((p2,p3)))
		d[p1].add(t3)
		d[p2].add(t2)
		d[p3].add(t1)
	return d

# if 

# tri_d = triset_list_to_tuple_dict(tri_l)
# print tri_d


# def tri_d_to_quad_list(tri_d):
# 	quad_l = []
# 	for key in tri_d:
# 		key_set = tri_d[key]
# 		for p1,p2 in key_set:
# 			key_p1_set = tri_d[p1]
# 			key_p2_set = tri_d[p2]


# Once I have the tuple list, and the tuple dict, I can probably
# do something like a BFS. For every prime, if it leads to something,
# from there I'll go to another place. If it can get back to the first one
# on the second try, it's a tri. Third, it's a quad, fourth it's a quint.
# On every step I also need to see if it matches with the things before it. 


def dict_to_n_list(pair_dict, n, so_far, answers):
	if len(so_far) == n:
		answers.add(tuple(sorted(so_far)))
		return
	for p in pair_dict:
		s = pair_dict[p]
		should_add = True
		for seen in so_far:
			if seen not in s:
				should_add = False
				break
		if should_add:
			new_so_far = list(so_far)
			new_so_far.append(p)
			dict_to_n_list(pair_dict, n, new_so_far, answers)
	return


# seived = 
from time import time


up_to = 10000
n_len = 4
time_to_make_start = time()
print "making dict"
d = dict_up_to(up_to)
d_filt = filter_dict_by_size(d, n_len)
print len(d)
print len(d_filt)

start = time()

print "time to make: " + str(start-time_to_make_start)
print "dict made, making answer set"
# important_stuff = [(3, 37, 67, 5923), (23, 311, 677, 827), (3, 37, 67, 2377), (7, 19, 97, 3727), (3, 7, 109, 673), (7, 19, 97, 4507)]
# important = set([i for j in important_stuff for i in j])
# print important
answer_set = set()
for p in d_filt:
	dict_to_n_list(d_filt, 5, [p], answer_set)

print answer_set
print "time taken: " + (str(time()-start))

# It's too big, I can't do it :(   I don't know what to do here, that stunk.
	



# dict_to_three_list = dict_to_n_list(pair_dict)













		











# Once we have the pairs, we need to see how they match up.



