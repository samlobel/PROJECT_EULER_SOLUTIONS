

"""
The only way to do this one is to count up the days, and mark them.

Or, you could do probability, and then guess.

"""


months = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']

mon_map = {
	'JAN':31,
	'FEB':28,
	'MAR':31,
	'APR':30,
	'MAY':31,
	'JUN':30,
	'JUL':31,
	'AUG':31,
	'SEP':30,
	'OCT':31,
	'NOV':30,
	'DEC':31
}

month_map = [31,
	28,
	31,
	30,
	31,
	30,
	31,
	31,
	30,
	31,
	30,
	31
]

def year_is_leap(year):
	if year % 4 == 0:
		if year % 100 != 0:
			return True
		if year % 100 == 0:
			if year % 400 == 0:
				return True
			return False
	return False


def given_date_get_next_date((weekday, date, month, year)):
	new_weekday = weekday + 1
	new_weekday = new_weekday % 7
	new_date = date + 1
	new_year = year
	new_month = month
	days_in_month = month_map[month]
	if month == 1:
		if year_is_leap(year):
			days_in_month += 1
	if new_date >= days_in_month:
		new_month += 1
		new_date = 0
	if new_month >= 12:
		new_year += 1
		new_month = 0
	return (new_weekday, new_date, new_month, new_year)



def day_meets_criteria((weekday, date, month, year)):
	if weekday == 0 and date == 0:
		return True
	return False



def tally():
	curr = (1,0,0,1900)
	count = 0
	total_days = 0
	while not (curr[1] ==20 and curr[2] == 11 and curr[3] == 2000):
		total_days+=1
		if day_meets_criteria(curr):
			count+=1
			print curr
		curr = given_date_get_next_date(curr)
	print "\n\n"
	print curr
	print count
	print total_days
	return count


print tally()




# print day_meets_criteria((4,0,11,1902))


# print given_date_get_next_date((0,27,1,1953))

# print year_is_leap(1952)
# print year_is_leap(2000)
# print year_is_leap(1996)
# print year_is_leap(1997)


