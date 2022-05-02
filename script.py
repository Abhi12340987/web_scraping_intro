import requests
from bs4 import BeautifulSoup

#r = requests.get("http://pythonhow.com/example.html")
r = requests.get("http://www.pyclass.com/example.html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})


tent = r.content
#print(tent)


scrap = BeautifulSoup(tent, "html.parser")

#print(scrap.prettify())

all = scrap.find_all("div", {"class": "cities"})

#print(all)

all[0].find_all("h2")[0].text

for item in all:
    print(item.find_all("p")[0].text)