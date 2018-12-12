#!/usr/bin/env python

from py2neo import Authenticate, Graph, Node, Relationship

authenticate("127.0.0.1:7474", "neo4j", "root")
graph = Graph("http://127.0.0.1:7474/db/data")
graph.delete_all()

article = Node("Articles", name="Title of the article")
nation = Node("Nation", name="Syria")
Relation_between = Relationship(article, "Related", nation)
graph.create(Relation_between)

article = Node("Articles", name="Title of the article 2 ")
nation = Node("Nation", name="Iran")
Relation_between = Relationship(article, "Related", nation)


graph.create(Relation_between)

