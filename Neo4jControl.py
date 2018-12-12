#!/usr/bin/env python3.6

from py2neo import authenticate, Graph, Node, Relationship, NodeSelector
from urllib.request import urlopen
from bs4 import BeautifulSoup


def DBAuth():
    HOST = "127.0.0.1"
    PORT = "7474"
    USER = "neo4j"
    PASS = "root"
    URL = "http://" + HOST + ":" + PORT + "/db/data"
    authenticate( HOST + ":" + PORT, USER, PASS)
    graph = Graph(URL)
    print("Conected to " + URL)
    #graph.delete_all()
    return graph


def NewArticle(URL, TAG):
    soup = BeautifulSoup(urlopen(URL), "html.parser")
    TITLE=soup.title.string
    graph = DBAuth()
    article = Node("Article", name=TITLE, url=URL)
    tag = Node("Tag", name=TAG)
    relation = Relationship(article, "Tagged" ,tag)
    graph.merge(relation)


def Req():
    graph = DBAuth()
    results = graph.run("MATCH (n) RETURN n").data()
    print(results)
