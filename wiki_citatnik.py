'''
Цитата дня. WEB-ресурс: https://ru.wikiquote.org/
Парсинг и сохранение вывода в формате json.

'''


import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup
from pprint import pprint
import json



session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36'}
base_url = 'https://ru.wikiquote.org/'
response = session.get(base_url, headers = headers)
random_dom = BeautifulSoup(response.text, 'html.parser')
text = str(random_dom.find_all('cite'))
author = str(random_dom.find_all('div', {'style':'float:right'}))
text = text.replace('[<cite>', '"').replace('</cite>]','"')
author = author.replace('[<div style="float:right">','').partition(',')[0]
listik = ['text: ', 'author: ']
listochek = [text, author]
dictim = dict(zip(listik, listochek))
pprint(dictim)

with open('main_wikiquote.json', 'w') as f:
    json.dump(dictim, f, ensure_ascii=False)

