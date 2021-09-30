import requests
from bs4 import BeautifulSoup
import csv

HEADERS = {
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru,en;q=0.9',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 YaBrowser/21.8.3.614 Yowser/2.5 Safari/537.36'
    }

URL = 'https://www.michaels.com/shop-categories/categories'

r = requests.get(url = URL, headers = HEADERS)
res = r.text

with open('index.html', 'w', encoding = 'utf-8') as file:
    file.write(res)

with open('index.html', encoding = 'utf-8') as file:
    res = file.read()

soup = BeautifulSoup(res, 'lxml')

#Сollecting brand links
brand_link = soup.find('div', class_ = 'Brand').find('ul', class_ = 'scrollable').find_all('a')

#Collecting brands data
brands = []
for item in brand_link:
    brand_sp = item.find('span', class_ = 'refinement-text')
    try:
        brand = brand_sp.text
        brands.append(brand)
    except Exception as ex:
        continue

#Case-insensitive list sorting
brands = sorted(brands, key=str.casefold)

#Saving brands data to a csv format table
with open('Brands.csv', 'w', newline = '', encoding = 'utf-8') as file:
    writer = csv.writer(file)
    for item in brands:
        writer.writerow([item])