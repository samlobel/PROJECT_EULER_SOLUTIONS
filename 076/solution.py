

"""
Sets will be sets of tuples, each 99 long, where each pos is the number of times
you see that.


Since it takes lets say 13 times tp multiply by 10, it's going to be
like 10^8 at least (probably higher) by the end. So we really can't
do much meaningful stuff with iteration.
For mine, looking at a tuple takes at least 100 steps, which means we'd
be sitting here for a long time

"""


# def make_first_val(target_sum, max_sum):
# 	first = [0 for i in range(max_sum-1)]
# 	first[0]=1
# 	first[target_sum - 2] = 1
# 	tup = tuple(first)
# 	return tup

def make_add_one_set(set_below):
	# print set_below
	new_set = set()
	for tup in set_below:
		# print tup
		l = list(tup)
		l[0]+=1
		t = tuple(l)
		new_set.add(t)
	return new_set

def given_tuple_make_shift_gen_set(tup):
	# print tup
	new_set = set()
	for i, v in enumerate(tup):
		if v != 0:
			l = list(tup)
			l[i]-=1
			l[i+1]+=1
			t = tuple(l)
			new_set.add(t)
	return new_set


def given_set_below_create_new_set(set_below):
	new_set = set()
	# new_set.add(make_first_val(target_sum, max_sum))
	add_one_set = make_add_one_set(set_below)
	# print add_one_set
	new_set = new_set.union(add_one_set)
	for t in set_below:
		new_set = new_set.union(given_tuple_make_shift_gen_set(t))
	# return new_set
	# difference = set.difference(set_below, new_set)
	# print len(difference)
	# print len(new_set) - len(set_below)
	return new_set


def from_seed_go_up_to(max_num):
	adds_to_two = [0 for i in range(max_num-1)]
	adds_to_two[0]=2
	s = set([tuple(adds_to_two)])
	for i in range(max_num-2):
		s = given_set_below_create_new_set(s)
		# print "\n"
		print len(s)
	return len(s)

print from_seed_go_up_to(40)



	# first = [0 for i in range(max_sum-1)]
	# first[0]=1
	# first[target_sum - 1] = 1
	# tup = tuple(first)
	# new_set.add(tup)


"""
I feel like the only two ways it may work are either combinatorics or 
some sort of DFS, starting with 1 1 1 1 1 1 ...

Maybe have 100 seeds, with all 0s to no zeros. And then see how you 
"""


