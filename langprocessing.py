# -*- coding: utf-8 -*-
from collections import Counter
#from pattern.de import parse, split
from textblob import TextBlob
from stopwords import STOPWORDS

# def parse_text(text):
#     """ takes german text, 1 or more sentences and applies part of speech information
#     """
#     # STTS works better than standard tagset. The target words are NN and NE
#     return parse(text, tagset="STTS")
# 
# def noun_list(sentence):
#     """sentence format: 
#        [[u'Die', u'ARTDEF', u'O', u'O'], item2as_list, ...]
#     """
#     nouns = []
#     for i in sentence:
#         the_word = i[0]
#         if i[1] in ['NN', 'NE'] and the_word[0].isupper():
#             nouns.append(the_word)
#     return nouns

def tokenize(data):
    content = TextBlob(data)
    return content.words

def remove_stopwords(doc):
    words = doc.split()
    processed_words = [word for word in words if not word in STOPWORDS]
    return ' '.join(processed_words)

def find_most_frequent_words(docs, amount=20):
    counter = Counter()
    for doc in docs:
        doc = remove_stopwords(doc)
        wordlist = tokenize(doc)
        counter.update(wordlist)
    return counter.most_common(amount)

def process_documents(docs, amount=20):
    top_20 = find_most_frequent_words(docs, amount)
    print 'top 20 words:', top_20
    result = {}
    for word in top_20:
        result[word] = TextBlob(word).translate(from_lang="De", to="en")
    return result


if __name__ == "__main__":
    text = "Auf der Suche nach seinen verschwundenen Eltern folgt der junge Peter Parker (Andrew Garfield) einer Spur, die ihn zu Wissenschaftler Curt Connors führt. In dessen Labor wird Peter von einer Spinne gebissen. Fortan verfügt er über Superkräfte, die er als Spider-Man im Kampf gegen das Verbrechen einsetzt. Doch als er es mit Connors' bösem Alter Ego \"The Lizard\" zu tun bekommt, steht Peter vor einer schweren Entscheidung. - Spider-Man ist zurück: Neustart der Marvel-Comicverfilmung, voll grandioser Effekte, Tempo und Action."
    parsed_text = parse_text(text)
    nouns = []
    for sentence in parsed_text.split():
        nouns = nouns + noun_list(sentence)
    print nouns
