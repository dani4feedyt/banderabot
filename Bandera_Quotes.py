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
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Connection': 'keep-alive'}
pag = Request('https://porokhivnytsya.com.ua/2018/12/30/stepan-bandera_quotes/',  headers=hdr)
webpage = urlopen(pag, timeout =10).read()
page = webpage.decode('utf-8')
print(page)
soup = BeautifulSoup(page, 'html.parser')

_dict0 = soup.find_all('p', text=True)[5:n_1]
print(_dict0)
if _dict0 != []:
    print('1')
if _dict0 == []:
    print('2')
    
