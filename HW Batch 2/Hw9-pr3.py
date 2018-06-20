#Sara D'Alessandro
#Homework #9

import csv 

csvdata = []

outfile = open("SAT_ANALYSIS.txt", "w")

f = open('2012_SAT_Results.csv', "r")
#reader = csv.reader(csvfile)
#for line in reader:
	#csvdata.append(line)

reader = csv.reader(f)
for row in reader:
	print(row, file=outfile)

for i in csvdata:
	print(i)

def getkey(item):
	return item[0]

csvdata.sort(key=getkey)

for i in csvdata:
	print (i)

f.close()

