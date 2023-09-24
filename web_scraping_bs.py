# import os.path
# from collections import defaultdict
# import string
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
import sys

import requests
from bs4 import BeautifulSoup

# url = "https://www.revisor.mn.gov/laws/2014/0/Session+Law/Chapter/294/"
# url = "https://nostarch.com/"
url = "https://trudvsem.ru/vacancy/search?_page=1&_titleType=VACANCY_NAME&_title=%D0%B1%D1%83%D1%85%D0%B3%D0%B0%D0%BB%D1%82%D0%B5%D1%80&_regionIds=3100000000000&_publishDateType=ALL"
r = requests.get(url, headers={'User-agent': 'your bot 0.1'})
print("\nStatus code:", r.status_code)  # A status code of 200 indicates a successful response
r.raise_for_status()
c = r.content
soup = BeautifulSoup(c, "html.parser")

# ------------------------------------------------------------------------------------------------------------------------------------------
"""
#  Use a defaultdict with an empty list because it eases the DataFrame creation
expense_lines = defaultdict(list)
funding_lines = defaultdict(list)
funding = False

def convert_num(val):
    # Convert the string number value to a float
    # Remove all extra whitespace
    # Remove commas
    # If wrapped in (), then it is negative number
    val = string.strip(val).replace(",","").replace("(","-").replace(")","")
    return float(val)

#  After looking at the data, we can see that the summary has a div id we can use
summary = soup.find("div", {"class":"bill_section appropriations", "id": "laws.1.1.0"})

#  Get all the tables in the summary
tables = summary.find_all('table')

#  The first table is not useful header info
#  The second table contains all we need (the list is 0 indexed)
data_table = tables[1]

# Go through each row of the table and pull out our data
for row in data_table.find_all("tr"):
    cells = row.find_all("td")
    #  Ignore lines that don't have 3 cells of data because it is just spacing
    if len(cells) == 3:
        line = (string.strip(cells[0].text), convert_num(cells[2].text))
        #  Once we get to the total line we start getting the funding lines
        if line[0] == "TOTAL":
            funding = True
            #  We don't want to capture the total because we can calc it
            continue
        if funding:
            funding_lines[line[0]].append(line[1])
        else:
            expense_lines[line[0]].append(line[1])

#  Create the DataFrame using from_dict
expense_df = pd.DataFrame.from_dict(expense_lines,orient='index')
funding_df = pd.DataFrame.from_dict(funding_lines,orient='index')
#  Label our column
expense_df.rename(columns={0: 'Amount'}, inplace=True)
funding_df.rename(columns={0: 'Amount'}, inplace=True)

print(expense_df.head())
"""

# ------------------------------------------------------------------------------------------------------------------------------------------
# summary = soup.find("div", {"class":"bill_section appropriations", "id": "laws.1.1.0"})
# elements = soup.select("div", {"class":"item-list"})
elements = soup.select("div", {"class": "item row"})
print(type(elements))

if len(elements) > 0:
    for i in range(0, len(elements)):
        # print(elements[i].attrs)
        print(elements[i].getText())
