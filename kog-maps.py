from bs4 import BeautifulSoup
from requests import get
from time import time
from sys import argv
from json import dumps

start_time = time()
maps = []
html = get("https://kog.tw/get.php?p=maps&p=maps").text
soup = BeautifulSoup(html, "html.parser")

map_div: BeautifulSoup
for map_div in soup.find_all("div", class_="card mb-4 box-shadow"):
    details: list[BeautifulSoup] = map_div.find_all("li", class_="list-group-item")
    maps.append({
        "name": map_div.find("h4").text,
        "star": len(details[0].find_all("i", class_="bi bi-star-fill")),
        "category": details[1].text,
        "points": int(details[2].text.split(" ", 1)[0]),
        "creator": details[3].text
    })

if ("--json" in argv):
    with open("maps.json", "w") as f:
        f.write(dumps(maps, indent=2))
        f.close()
else:
    print(dumps(maps, indent=2))
print(f"Completed in {time() - start_time:0.5f} seconds.")
