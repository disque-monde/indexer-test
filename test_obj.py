#!/usr/bin/env python

from newspaper import Article
from neomodel import db
from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
    UniqueIdProperty, RelationshipTo, RelationshipFrom)


class Paper(StructuredNode):
    def __init__(self, url):
        article = Article(url)
        article.download()
        article.parse()
        self.title = article.title
        self.date = article.publish_date
        self.img = article.top_image
        self.content = article.text


#  def newaper(self):
# p1 = Paper("https://www.lemonde.fr/asie-pacifique/article/2018/11/16/cambodge-pourquoi-le-terme-de-genocide-a-mis-quarante-ans-a-s-imposer_5384642_3216.html")
#
# print(p1.img)
# print(p1.title)
# print(p1.date)
# print(p1.content)
