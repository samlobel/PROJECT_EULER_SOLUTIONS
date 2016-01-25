

# Thoughts: I need to figure out how to double the amount of factors every time.
# First thing is generating a list of prime numbers. Second thing is adding
# numbers to it to double it, while increasing it by as little as possible.

# So, first I'd do 2. Then, I'd do 3. That's 6, which has 1,2,3,6=4. If I add 5,
# it has 8. But, if I add 2*2, it has 8 also. So, I have 2*2*2*3 with 8. And then
# 16, I add 5 because it's better than adding 9. I figured out which is the smallest
# way to double factors every time, and I did it 4 times for 2^4. 
# Is there a way to do it, just keeping track of how many times you've picked
# each? They all start at 0. Then, the next addition is turning 2 to 1.

# 1 factor is * 2, 3 factors is times 4, 7 factors is * 8. So, to double it, you add
# 2^0 of the primes the first doubling, 2^1 of the prime for the second, 2^3 of the prime
# for the third. So, you end up multiplying it by p^(2^n), where n is how many times you've
# chosen it so far.


"""

You start with a bunch of tuples, of the form (0,p) for all primes up to some number.
[(0,2),(0,3),(0,5),(0,7),(0,11)]
Then you also have one that keep track of how many times bigger something needs to get

We want to double it 500500 times. So, we need to keep track of how many times
we've chosen a particular prime to be doubled. Then, we go down the list and
compute p^(2^n), and see which is smallest, and then we add 1 to it.

"""



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


# print prime_seive(1000)



power_dict = [2**i for i in range(100)]
# print power_dict


def create_tuple_list(max_num):
	prime_list = prime_seive(max_num)
	tuple_list = [[p,0,p] for p in prime_list] 
	# First is next mult, second is count, and third is prime.
	# print tuple_list
	return tuple_list


def find_smallest_two_to_the(power):
	checking_powers = 7
	print "creating list"
	tuple_list = create_tuple_list(7370030) #Calculated after fact
	print "list created"
	most_recent_with_this_power = {}
	for m_r in range(checking_powers):
		most_recent_with_this_power[m_r] = -1

	i = 0
	while i < power:
		min_tuple = [float('inf'), 0, 0]
		pos_of_min_tuple = 0
		for powers in range(checking_powers):
			next_tup = tuple_list[most_recent_with_this_power[powers] + 1]
			if next_tup[0] < min_tuple[0]:
				pos_of_min_tuple = most_recent_with_this_power[powers] + 1
				min_tuple = next_tup
		# min_tuple = min(tuple_list)
		# print min_tuple
		most_recent_with_this_power[min_tuple[1]] = pos_of_min_tuple
		min_tuple[1] = min_tuple[1] + 1
		min_tuple[0] = min_tuple[2] ** power_dict[min_tuple[1]]
		# print min_tuple
		i += 1
	# print tuple_list
	print "tuple list created."
	print "filtering for non-zero"
	print "old length: " + str(len(tuple_list))
	filtered_list = [i for i in tuple_list if i[1]]
	print "new length: " + str(len(filtered_list))
	return filtered_list

	# return tuple_list
		# cur_min = float('inf')
		# cur_index = 0
		# # best_tup = tuple_list[cur_index]
		# best_ind = 0
		# while True:
		# 	curr_tup = tuple_list[cur_index]
		# 	next_val = curr_tup[2]
		# 	if next_val > cur_min:
		# 		# best_tup = tuple_list[cur_index-1]
		# 		# best_ind = cur_index - 1
		# 		break
		# best_ind = cur_index - 1
		# best_tup = tuple_list[best_ind]
		# two_to_the = 

# The next optimization I need to make is that I can check which number
# I just changed, and I'll have something like a :
# Last change to 6: ___, last change to 5: ___, last change to 4: ___
# If I do that up till 15, there's no way it goes over.
# And the beauty of that is that I only need to check 15 spots each time,
# which are the spots right after those, because those would be the ones that
# are next to change.




# def filter_list_by_not_zero(l):
# 	return [i for i in l if l[1]]


def map_filtered_list_to_mults(f_l):
	mapped = [tup[2]**(power_dict[tup[1]]-1) for tup in f_l]
	print mapped[0:10]
	return mapped



def mult_and_mod(mult_list, mod):
	memo = 1
	for m in mult_list:
		memo = memo * m
		memo = memo% mod
	return memo
	# return reduce(lambda x,y:(x*y)%mod,mult_list, 1)








t_l = find_smallest_two_to_the(500500)

print t_l[0:100]
print t_l[-1]
print t_l[-2]
mapped = map_filtered_list_to_mults(t_l)
to_mod_by = 500500507
answer = mult_and_mod(mapped, to_mod_by)
print answer
# print t_l[0:100]
# print t_l[-1]

# 35407281 should be the answer

