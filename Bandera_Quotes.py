
import requests
from bs4 import BeautifulSoup

n_1 = 22
page = requests.get("https://porokhivnytsya.com.ua/2018/12/30/stepan-bandera_quotes/",headers={'User-Agent': 'Chrome/23.0.1271.64'})
soup = BeautifulSoup(page.content, 'html.parser')

quotes = soup.find_all('p', text=True)[5:n_1]
