import os
from gevent import monkey
monkey.patch_all()
import bottle

import ipool
import langprocessing

app = bottle.Bottle()

def process_query(q):
    articles = ipool.query(q)
    return langprocessing.process_documents(articles)


@app.get('/flashcards/<query>')
def index(query):
    return dict(process_query(query))

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))