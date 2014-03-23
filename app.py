# -*- coding: utf-8 -*-
import os
import json
from gevent import monkey
monkey.patch_all()
import bottle

import ipool
import langprocessing

app = bottle.Bottle()

def process_query(q):
    articles = ipool.query(q)
    return langprocessing.process_documents(articles, 10)


@app.get('/flashcards/<query>')
def index(query):
    print json.dumps(process_query(query))
    return json.dumps(process_query(query))

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))