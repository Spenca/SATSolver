def genSudoku(s):
	output = ''
	for i in s.read().split(" "):
		try:
			if int(i) > 0:
				output += i[2]
				if (len(output) - output.count('\n')) % 9 == 0:
					output += '\n'
		except ValueError:
			continue
	print output

genSudoku(open("miniSATOutput", "r"))