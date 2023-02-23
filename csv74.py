import json
listname = [1, 2, 3]
with open("jsontestfile.json", "w") as jsontestfile:
	json.dump(listname, jsontestfile)