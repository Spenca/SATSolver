import sys
import re
 
txt = sys.argv[1]
count = 0
avg = 0
with open(txt) as f:
        for line in f:
		   k = re.findall( '\d.\d*', line)
		   if len(k) != 0:
				count = count + 1
				avg = avg + float(k[0])
print(avg/count)				
