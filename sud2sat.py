#There is at least one number in each entry
def fstRule(s):
	for x in range(1, 10):
		for y in range(1, 10):
			for z in range(1, 10):
				s += str(x) + str(y) + str(z) + ' '
			s += '0\n'
	return s


#Each number appears at most once in each row
def sndRule(s):
	for y in range(1,10):
		for z in range(1,10):
			for x in range(1,9):
				for i in range(x+1,10):					
					s += '-' + str(x) +str(y) + str(z) + ' '  + '-' + str(i) + str(y) + str(z)  + ' 0\n'
	return s

#Each number appears at most once in each column
def thrdRule(s):
	for x in range(1, 10):
		for z in range(1, 10):
			for y in range(1, 9):
				for i in range(y+1, 10):
					s += '-' + str(x) + str(y) + str(z) + ' ' + '-' + str(x) + str(i) + str(z) + ' 0\n'
	return s

#Each number appears at most once in each 3x3 sub-grid (part 1)
def frthRuleP1(s):
	for z in range(1, 10):
		for i in range(3):
			for j in range(3):
				for x in range(1, 4):
					for y in range(1, 4):
						for k in range(y+1, 4):
							s += '-' + str(3 * i + x) + str(3 * j + y) + str(z) + ' ' + '-' + str(3 * i + x) + str(3 * j + k) + str(z) + ' 0\n'
	return s

#Each number appears at most once in each 3x3 sub-grid (part 1)
def frthRuleP2(s):
	for z in range(1, 10):
		for i in range(3):
			for j in range(3):
				for x in range(1, 4):
					for y in range(1, 4):
						for k in range(x+1, 4):
							for l in range(1, 4):
								s += '-' + str(3 * i + x) + str(3 * j + y) + str(z) + ' ' + '-' + str(3 * i + k) + str(3 * j + l) + str(z) + ' 0\n'
	return s	

#Each number in a provided Sudoku instance encoding appears in appropriate cell
def sudRule(s, sudoku):
	for i, c in enumerate(sudoku):
		try:
			cInt = int(c)
			if cInt > 0:
				s += str(int(i) / 9 + 1) + str(int(i) % 9 + 1) + c + ' 0\n'
		except ValueError:
			continue
	return s

testSud = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
s = sudRule(frthRuleP2(frthRuleP1(thrdRule(sndRule(fstRule('p cnf 729 8829\n'))))), testSud)

f = open('testSAT', 'w')
f.write(s)
f.close()