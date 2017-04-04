def genSudoku(s):
	output = ''
	for i in s.read().split(" "):
		try:
			if int(i) > 110:
				if int(i[1]) == 0 or int(i[2]) == 0:
					continue
				output += i[2]
				if (len(output) - output.count('\n')) % 9 == 0:
					output += '\n'
		except ValueError:
			continue
	print output

genSudoku(open("miniSATOutput", "r"))