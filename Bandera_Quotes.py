import lxml
import requests
from urllib.request import urlopen, Request
import urllib.request
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
pag = Request('https://porokhivnytsya.com.ua/2018/12/30/stepan-bandera_quotes/',  headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(pag).read()
page = webpage.decode('utf-8')
soup = BeautifulSoup(page, 'html.parser')
_dict0 = soup.find_all('p', text=True)[5:n_1]
print(_dict0)
if _dict0 != []:
    print('1')
if _dict0 == []:
    print('2')
    
