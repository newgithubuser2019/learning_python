import csv
with open("csvfile.csv", "w", newline="") as csvfile:
	csvvar = csv.writer(csvfile, delimiter=",")
	csvvar.writerow(["dsd", "csdds", "fde"])
	csvvar.writerow(["ds3d", "csdd3s", "f3de"])
	csvvar.writerow(["dfsd", "cs33dds", "fc3de"])