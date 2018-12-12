#!/usr/bin/env python

from newspaper import Article

url = "https://www.liberation.fr/debats/2018/11/08/les-abeilles-victimes-de-leur-intelligence_1690852"

article = Article(url)
article.download()
article.parse()
print(article.title)
print(article.top_image)
#print(article.authors)
print(article.publish_date)
print(article.text)
