import math


def primecheck(start):
	primed = 0
	counter = 2
	k = 2
	#check = 0
	while primed < start:
		check = 0
		while k <= math.sqrt(counter):
			if counter % k == 0:
				check += 1
				k += 1
			else:
				k += 1
			if check == 0:
				print counter
				primed += 1
				
		counter += 1
		if primed == start:
			break
				
primecheck(6)