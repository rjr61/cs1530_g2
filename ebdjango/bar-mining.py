## First search using:
# https://plcbplus.pa.gov/pub/Default.aspx?PossePresentation=LicenseSearch
# License-Type: All
# License-Status: Active
# County: Allegheny
# Zip Code: 15213

## Second download the page source to `license-data.txt`

from bs4 import BeautifulSoup
import re, json

f = open("license-data.txt", "r")
contents = f.read()
soup = BeautifulSoup(contents, 'html.parser')
name_anchors = soup.find_all(id=re.compile("Premise_"))
names = [anchor.find("b").contents[0] for anchor in name_anchors]

print(names)

# with open('all_locations.json', 'w', encoding='utf8') as outfile:
#    json.dump(names, outfile)

## Third run using `python bar-mining.py`