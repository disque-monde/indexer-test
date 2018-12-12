from neomodel import (db, config, StructuredNode, StringProperty, IntegerProperty,
    UniqueIdProperty, RelationshipTo, RelationshipFrom)
from newspaper import Article


class Paper(StructuredNode):
    #uid = UniqueIdProperty()
    title = StringProperty(unique_index=True)
    date = StringProperty(unique_index=True)
    img = StringProperty(unique_index=True)
    content = StringProperty(unique_index=True)


db.set_connection('bolt://neo4j:root@127.0.0.1:7687')
article = Article("https://www.liberation.fr/france/2018/11/17/manifestante-morte-en-savoie-c-etait-sa-premiere-manif_1692724")
article.download()
article.parse()

p1 = Paper(title=article.title, date=article.publish_date, img=article.top_image, content=article.text)
p1.save()
print(p1)

