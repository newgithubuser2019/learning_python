import openpyxl, pprint

countyData = {}

#print("Opening Workbook...")
wb = openpyxl.load_workbook("censuspopdata.xlsx")
sheet = wb["Population by Census Tract"]

tuple(sheet["A2":"D72865"])
for row0fCell0bjects in sheet["A2":"D72865"]:
    for cell0bj in row0fCell0bjects:
        state = sheet["B" + str(cell0bj.coordinate[1:])].value
        county = sheet["C" + str(cell0bj.coordinate[1:])].value
        pop = sheet["D" + str(cell0bj.coordinate[1:])].value
        countyData.setdefault(state, {})
        countyData[state].setdefault(county, {"tracts": 0, "pop": 0})
        countyData[state][county]["tracts"] += 1
        countyData[state][county]["pop"] += int(pop)

#print("Writing Results...")

#resultfile = open("census2010.py", "w")
#resultfile.write("alldata = " + pprint.pformat(countyData))
#resultfile.close()

with open("censuspopdata2.py", "w") as censuspopdata2:
    censuspopdata2.write("alldata = " + pprint.pformat(countyData))
print("Done")