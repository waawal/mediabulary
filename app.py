# -*- coding: utf-8 -*-
import os
import json
from gevent import monkey
monkey.patch_all()
import bottle

import ipool
import langprocessing
from dicttoxml import dicttoxml


app = bottle.Bottle()


def process_query(q):
    articles = ipool.query(q)
    return langprocessing.process_documents(articles, 20)


@app.get('/flashcards/<query>')
def index(query):
    print json.dumps(process_query(query))
    some_dict = {}
    some_dict['flashcards'] = []
    for key, value in process_query(query).items():
        some_dict['flashcards'].append({'word': unicode(key), 'translation': unicode(value)})

    return dicttoxml(some_dict)

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))