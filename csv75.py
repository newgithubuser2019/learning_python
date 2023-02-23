import json
with open("jsontestfile.json", "r") as jsontestfile:
	var1 = json.load(jsontestfile)
print(var1)