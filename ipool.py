import json
import requests

from htmllaundry import strip_markup
from textblob import TextBlob
from collections import Counter

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

def tokenize(data):
    content = TextBlob(data[0])
    return content.words

def frequency(wordlist):
    """ Takes a list of words/token and returns a dict
        with the counts of the words/token.
    """
    return Counter(wordlist)

if __name__ == "__main__":
    data = query('katzen', 3)
    wordlist = tokenize(data)
    freq = frequency(wordlist)
    print freq
