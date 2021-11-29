import lxml
import requests
from urllib.request import urlopen
from lxml import etree
from lxml import html
import random
from collections import Counter
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
a1 = 1
b1 = 1
c1 = 1
n_1 = 22
page = requests.get('https://porokhivnytsya.com.ua/2018/12/30/stepan-bandera_quotes/')
print(page)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
_dict0 = soup.find_all('p', text=True)[5:n_1]
if _dict0 != []:
    print('1')
if _dict0 == []:
    print('2')
    
