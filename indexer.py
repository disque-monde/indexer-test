#!/usr/bin/env python3.6

import getopt
import sys
from Neo4jControl import NewArticle, Req

try:
    opts, _ = getopt.getopt(sys.argv[1:], 'u:t:l', ['url=', 'tag=', 'liste'])
except getopt.GetoptError:
    sys.exit(2)

for opt, arg in opts:
    if opt in ('-u', '--url'):
        URL=arg
    if opt in ('-t', '--tag'):
        TAG=arg
    if opt in ('-l', '--liste'):
        Req()

NewArticle(URL, TAG)
#Req()
