import csv
with open("csvfile.csv", "r") as csvfile:
	csvvar = csv.reader(csvfile)
	csvlist = []
	for eline in csvvar:
		csvlist += eline
print(csvlist)