from test_obj import Paper
from neomodel import db
from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
    UniqueIdProperty, RelationshipTo, RelationshipFrom)


class Country(StructuredNode):
    code = StringProperty(unique_index=True, required=True)

    # traverse incoming IS_FROM relation, inflate to Person objects
    inhabitant = RelationshipFrom('Person', 'IS_FROM')


class Person(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)

    # traverse outgoing IS_FROM relations, inflate to Country objects
    country = RelationshipTo(Country, 'IS_FROM')

db.set_connection('bolt://neo4j:root@127.0.0.1:7687')

jim = Person(name='Jim', age=3).save()
#newpaper = Paper("https://www.lemonde.fr/asie-pacifique/article/2018/11/16/cambodge-pourquoi-le-terme-de-genocide-a-mis-quarante-ans-a-s-imposer_5384642_3216.html")

#newpaper