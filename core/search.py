import fileinput
from core import xml_parser
from core import nlp
from nltk.corpus import wordnet as wn
import nltk


def syn_search(word):
    nltk.download('wordnet')
    nltk.download('omw')

    synonyms = {word}

    for syn in wn.synsets(word, lang='fra'):
        for l in syn.lemmas('fra'):
            synonym = l.name()
            if '_' in synonym:
                continue
            else:
                synonyms.add(synonym)
    return synonyms


def search():
    raw_files = xml_parser.init_data()
    raw_data = xml_parser.parser(raw_files)

    articles = []
    for data in raw_data:
        articles.append(data.description + ' ' + data.title)

    # Lecture des données depuis l'entrée standard
    str_input = fileinput.input()[0].strip()
    # str_input = 'voiture'

    splitted_input = str_input.split()
    str_input = [syn_search(word) for word in splitted_input]
    str_input = set().union(*str_input)
    str_input = ' '.join(str_input)

    result, fiability = nlp.find_best_matching(str_input, articles)
    print(raw_data[result].link)

search()
