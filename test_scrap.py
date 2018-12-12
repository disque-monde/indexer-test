#!/usr/bin/env python

import bs4
import requests
import configparser

url = 'https://www.lemonde.fr/pollution/article/2018/10/24/les-eurodeputes-pour-l-interdiction-des-produits-en-plastique-a-usage-unique_5374014_1652666.html'

config = configparser.ConfigParser()
config.read('scrapping-config.ini')
#print(config.sections())
#for key in config.get('lemonde.fr', ): print(key)

page = requests.get(url)
soup = bs4.BeautifulSoup(page.text, features="lxml" )
#print(soup)

title = soup.title.string
print(title)

timepublish = soup.find( {'time' : 'nth-child(2)'}).get_text(' ', strip=True)
print(timepublish)

#timemaj = soup.find({'time' : 'nth-child(3)'}).get_text('', strip=True) < ULTRABUG
#print(timemaj)

author = soup.find(id="publisher").get_text(' ', strip=True)
print(author)

article = soup.find(class_='article')
exclude1 = soup.find(class_='bandeau_matinale')
exclude1.clear(article)
exclude2 = soup.find(class_='bloc_signature')
exclude2.clear(article)
articleclean = article.get_text(' ', strip=True)
print(articleclean)