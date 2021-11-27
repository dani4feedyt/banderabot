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
page = requests.get('https://porokhivnytsya.com.ua/2018/12/30/stepan-bandera_quotes/')
soup = BeautifulSoup(page.content, 'html.parser')
_dict1 = soup.find_all('p')[5:37]
i = 0
_dict0 = []
while i <= 30:
    for dct in _dict1:
        dct1 = _dict1[i].get_text()
        i += 1
        _dict0.append(dct1) 
print (random.choice(_dict0))

