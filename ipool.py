import json
import requests

from htmllaundry import strip_markup

BASE = 'http://ipool-extern.s.asideas.de:9090/api/v2/search'

def query(self, q, limit=100, **kwargs):
    """Get a list of result from a query
        query('katzen', 50)
    """

    payload = {'q': q, 'limit': limit}
    if kwargs:
        payload.extend(kwargs)
    docs = requests.get(BASE, params=payload).json()['documents']
    return [strip_markup(doc['content']) for doc in docs]
