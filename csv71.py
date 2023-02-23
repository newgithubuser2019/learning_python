import csv
with open("potions.csv", "r") as csvfile:
	csvvar = csv.reader(csvfile)
	csvlist = []
	for eline in csvvar:
		csvlist += eline
print(csvlist)