import sys
import subprocess

def runSolver(s):
	if len(sys.argv) > 1 and sys.argv[1] == "1":
		subprocess.check_output(["python", "sud2sat.py", s, "1"])
	else:
		subprocess.check_output(["python", "sud2sat.py", s])
	p = subprocess.Popen(["minisat", "sud2satOutput", "miniSATOutput"], stdout=subprocess.PIPE)
	out, err = p.communicate()

	f = open('top95_miniSATOutput', 'a')
	f.write(out)
	f.close()

	p = subprocess.Popen(["python", "sat2sud.py"], stdout=subprocess.PIPE)
	out, err = p.communicate()

	f = open('top95_sat2sudOutput', 'a')
	f.write(out)
	f.close()

open('top95_miniSATOutput', 'w').close()
open('top95_sat2sudOutput', 'w').close()
s = ""

with open("top95.txt") as test_puzzles:
	for line in test_puzzles:
		runSolver("".join(line.split()))









