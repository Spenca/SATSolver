import sys

txt = sys.argv[1]
output = sys.argv[2]
count = 0
avg = 0
with open(txt) as f:
    with open(output, "w") as f1:
        for line in f:
            if "CPU time" in line:
				count = count + 1
				f1.write(line)
				#f1.write("puzzle:" + str(count) + ' \n' + line + '\n')

