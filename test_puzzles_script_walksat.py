import sys
import subprocess

def runSolver(s):
	if len(sys.argv) > 1 and sys.argv[1] == "1":
		subprocess.check_output(["python", "sud2sat.py", s, "1"])
	else:
		subprocess.check_output(["python", "sud2sat.py", s])
	p = subprocess.Popen(["./Walksat_v51/walksat", "sud2satOutput", "miniSATOutput"], stdout=subprocess.PIPE)
	out, err = p.communicate()

	f = open('test_puzzles_miniSATOutput', 'a')
	f.write(out)
	f.close()

	p = subprocess.Popen(["python", "sat2sud.py"], stdout=subprocess.PIPE)
	out, err = p.communicate()

	f = open('test_puzzles_sat2sudOutput', 'a')
	f.write(out)
	f.close()

open('test_puzzles_miniSATOutput', 'w').close()
open('test_puzzles_sat2sudOutput', 'w').close()
s = ""

with open("test_puzzles.txt") as test_puzzles:
	lineNum = 1
	for line in test_puzzles:
		if lineNum % 10 == 1:
			lineNum += 1
			continue
		s += line
		if lineNum % 10 == 0:
			s = "".join(s.split())
			runSolver(s)
			s = ""
		lineNum += 1