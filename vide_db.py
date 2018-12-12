#!/usr/bin/env python

from py2neo import authenticate, Graph, Node, Relationship

authenticate("127.0.0.1:7474", "neo4j", "root")
graph = Graph("http://127.0.0.1:7474/db/data")
graph.delete_all()

