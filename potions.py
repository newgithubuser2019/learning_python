import csv
with open("potions.csv") as potions:
	varpotions = csv.reader(potions)
	listpotions = []
	for eline in varpotions:
		listpotions += eline
indexvar1 = listpotions.index("Draught of Peace")
indexvar2 = indexvar1 + 1
print(listpotions[indexvar2])