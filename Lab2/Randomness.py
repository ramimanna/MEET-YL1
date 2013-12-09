from random import randint
def randomness():
	a = raw_input("Next ")
	b = randint(0,1)
	if a == "n":
		if b == 0:
			print "H"
		elif b == 1:
			print "T"
	randomness()
randomness()
