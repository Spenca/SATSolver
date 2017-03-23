#There is at least one number in each entry
def fstRule(s):
	for x in range(1, 10):
		for y in range(1, 10):
			for z in range(1, 10):
				s += str(x) + str(y) + str(z) + ' '
			s += '0\n'
	return s

#Each number appears at most once in each column
def thrdRule(s):
	for x in range(1, 10):
		for z in range(1, 10):
			for y in range(1, 9):
				for i in range(y+1, 10):
					s += '-' + str(x) + str(y) + str(z) + ' ' + '-' + str(x) + str(i) + str(z) + ' 0\n'
	return s