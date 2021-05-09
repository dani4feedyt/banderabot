import lxml
import requests
from urllib.request import urlopen
from lxml import etree
from lxml import html
import random
from collections import Counter
a1 = 1
b1 = 1
c1 = 1
page = requests.get('https://porokhivnytsya.com.ua/2018/12/30/stepan-bandera_quotes/')
tree = html.fromstring(page.content)
_dict = (tree.xpath('//p[not(contains(text(),"Свої для своїх про своє"))]/text()'))
c = Counter(_dict)
while a1 <= c["\xa0"]:
    if '\xa0' in _dict:
        _dict.remove('\xa0')
    a1 += 1
while b1 <= c["\n"]:
    if '\n' in _dict:
        _dict.remove('\n')
    b1 += 1
while c1 <= c[" "]:
    if ' ' in _dict:
        _dict.remove(' ')
    c1 += 1
_dict.remove('Коментарі закриті.')
quotes = _dict
