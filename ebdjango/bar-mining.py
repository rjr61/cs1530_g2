from bs4 import BeautifulSoup
import requests

html = requests.get("http://www.dotheburgh.com/bars/").text
soup = BeautifulSoup(html, 'html.parser')
title_anchors = soup.find_all("a", class_="title")
bar_names = [anchor.contents[0] for anchor in title_anchors]

print(bar_names)