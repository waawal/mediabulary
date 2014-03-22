# -*- coding: utf-8 -*-
from pattern.de import parse, split

def parse_text(text):
    """ takes german text, 1 or more sentences and applies part of speech information
    """
    # STTS works better than standard tagset. The target words are NN and NE
    return parse(text, tagset="STTS")

def noun_list(sentence):
    """sentence format: 
       [[u'Die', u'ARTDEF', u'O', u'O'], item2as_list, ...]
    """
    nouns = []
    for i in sentence:
        the_word = i[0]
        if i[1] in ['NN', 'NE'] and the_word[0].isupper():
            nouns.append(the_word)
    return nouns

if __name__ == "__main__":
    # text = 'Auf der Krim haben russische Kräfte zwei weitere Militärbasen erobert.'
    # text = 'Die Bayern hätten bereits an diesem Spieltag Meister werden können, darauf müssen sie jedoch noch ein bisschen warten.'
    text = "Auf der Suche nach seinen verschwundenen Eltern folgt der junge Peter Parker (Andrew Garfield) einer Spur, die ihn zu Wissenschaftler Curt Connors führt. In dessen Labor wird Peter von einer Spinne gebissen. Fortan verfügt er über Superkräfte, die er als Spider-Man im Kampf gegen das Verbrechen einsetzt. Doch als er es mit Connors' bösem Alter Ego \"The Lizard\" zu tun bekommt, steht Peter vor einer schweren Entscheidung. - Spider-Man ist zurück: Neustart der Marvel-Comicverfilmung, voll grandioser Effekte, Tempo und Action."
    parsed_text = parse_text(text)
    nouns = []
    for sentence in parsed_text.split():
        nouns = nouns + noun_list(sentence)
    print nouns
