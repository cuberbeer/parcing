import requests
from bs4 import BeautifulSoup as BS

page = 1

#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
#reg_url = "https://www.avito.ru/sankt-peterburg/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&rn=25934"
#req = requests.get(url=reg_url, headers=headers) 
#print (req)
while True:
    r = requests.get("https://spb.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/" + str (page))
    html = BS (r.content, "html.parser")
    items = html.select("._93444fe79c--wrapper--W0WqH > ._93444fe79c--container--Povoi _93444fe79c--cont--OzgVc")
    if (len(items)):
        for el in items:
            title = el.select(".caption > a")
            print (title[0].text)
        page += 1
    else:
        break