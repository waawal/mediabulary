import os
import gevent
gevent.monkey.patch_all()
import bottle

app = bottle.Bottle()

@app.get('/<query>')
def process_query(query):
    return {
        'Katze': 'Cat',
        'Hund': 'Dog',
        'Pferd': 'Horse'
    }

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))