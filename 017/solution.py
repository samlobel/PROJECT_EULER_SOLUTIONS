

"""
First I'll try it the counting way, then I'll generate.
"""

one=3
two=3
three=5
four=4
five=4
six=3
seven=5
eight=5
nine=4
ten=3
eleven=6
twelve=6
thirteen=8
fourteen=8
fifteen=7
sixteen=7
seventeen=9
eighteen=8
nineteen=8
twenty=6
thirty=6
forty=5
fifty=5
sixty=5
seventy=7
eighty=6
ninety=6
hundred=7
def one_to_ninety_nine():
	single_digits = (one+two+three+four+five+six+seven+eight+nine)
	single_digits = 9*single_digits
	teens = (ten+eleven+twelve+thirteen+fourteen+fifteen+sixteen+seventeen+eighteen+nineteen)
	prefixes = 10*(twenty + thirty + forty + fifty + sixty + seventy + eighty + ninety)
	return single_digits + prefixes + teens

print one_to_ninety_nine()

def one_to_one_thousand():
	single_digits = (one+two+three+four+five+six+seven+eight+nine)
	otonn = one_to_ninety_nine()
	hundreds = single_digits + (9 * hundred)
	hundreds_ands = (single_digits * 99) + hundred*99*9 + 3*99*9 + one_to_ninety_nine()*9
	thousand = 11

	return otonn + hundreds + hundreds_ands + thousand

print one_to_one_thousand()






# def map(num_lt_100):


# def solve():
