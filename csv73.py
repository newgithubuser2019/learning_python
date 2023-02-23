import csv
with open("csvfile.csv", "a", newline="") as csvfile:
	csvvar = csv.writer(csvfile, delimiter=",")
	csvvar.writerow(["NEWadsd", "NEWacsdds", "NEWafde"])
	