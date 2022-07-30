import requests
from bs4 import BeautifulSoup as BS


flat_url_list = []

r = requests.get("https://spb.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/")
print(r)
result = r.content
soup = BS(result, 'lxml')
list = soup.find_all (class_= '_93444fe79c--link--eoxce')
print (list)


for flat in list:
    flat_page_url = flat.get('href')
    flat_url_list.append(flat_page_url)


with open ('flat_url_list.txt', 'a') as file:
    for line in flat_url_list:
        file.write(f'{line}\n')