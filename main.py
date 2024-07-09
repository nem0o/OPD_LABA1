import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url = 'https://omgtu.ru/news/'

page = requests.get(url, headers=UserAgent().random)
soup = BeautifulSoup(page.text, "html.parser")
block = soup.findAll('div', class_="news-card")

description = ''
for data in block:
    if data.find('h3'):
        description += data.text

with open("news.txt", 'w') as f:
    f.write(description)

