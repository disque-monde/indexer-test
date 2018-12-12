import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

response = HtmlResponse(url='https://www.lemonde.fr/planete/article/2018/11/01/un-archipel-independant-du-pacifique-les-palaos-bannit-la-creme-solaire-pour-sauver-son-corail_5377510_3244.html')
print(response)
title = response.css('.tt2').extract_first()
print(title)