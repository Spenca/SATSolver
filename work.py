def frthRuleP1(s):
	for z in range(1, 10):
		for i in range(3):
			for j in range(3):
				for x in range(1, 4):
					for y in range(1, 4):
						for k in range(y+1, 4):
							s += '-' + str(3 * i + x) + str(3 * j + y) + str(z) + ' ' + '-' + str(3 * i + x) + str(3 * j + k) + str(z) + ' 0\n'
	return s

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