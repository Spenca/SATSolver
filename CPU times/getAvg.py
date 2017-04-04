import sys
import re
import math
 
txt = sys.argv[1]
avg = 0
variance = 0
numList = []
with open(txt) as f:
        for line in f:
		   k = re.findall( '\d.\d*', line)
		   if len(k) != 0:
				numList.append(float(k[0]))
				avg = avg + float(k[0])
numList.sort()
length  = len(numList)
avg = str(avg/length)
median = str(numList[length/2])
for index in range(length):
	variance = variance +   math.pow( (numList[index] - float(avg)), 2)
variance = 	str(variance/length)
stdDev = math.sqrt(float(variance))
print('mean: ' + avg)
print('median: ' + median)
print('variance: ' + variance)
print('std. deviation: ' + str(stdDev))			
