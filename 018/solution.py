t = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

def make_array(tri):
	s = tri.split('\n')
	s_2 = [[int(i) for i in l.split(' ')] for l in s]
	return s_2


def array_to_shortest_path(arr):
	parallel = [[0.0 for i in l] for l in arr]
	parallel[0] = arr[0]
	# print parallel
	for i in range(len(arr)-1):
		r_1 = parallel[i]
		r_2 = arr[i]
		for j in range(len(r_1)):
			curr = parallel[i][j]
			pot_1 = arr[i+1][j]
			pot_2 = arr[i+1][j+1]
			new_par_1 = pot_1 + curr
			new_par_2 = pot_2 + curr
			parallel[i+1][j] = max(parallel[i+1][j], new_par_1)
			parallel[i+1][j+1] = max(parallel[i+1][j+1], new_par_2)

	return parallel





tri = make_array(t)
print tri

ans_tri =  array_to_shortest_path(tri)
last_row = ans_tri[-1]
print last_row
biggest = max(last_row)
print biggest



