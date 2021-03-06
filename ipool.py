# -*- coding: utf-8 -*-
import json
import requests

from htmllaundry import strip_markup

BASE = 'http://ipool-extern.s.asideas.de:9090/api/v2/search'

def query(q, limit=100, **kwargs):
    """Get a list of result from a query
        query('katzen', 50)
    """

    payload = {'q': q, 'limit': limit}
    if kwargs:
        payload.extend(kwargs)
    docs = requests.get(BASE, params=payload).json()['documents']
    result = [strip_markup(doc['content']) for doc in docs]
    return result
