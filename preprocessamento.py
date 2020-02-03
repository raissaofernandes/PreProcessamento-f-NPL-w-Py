import nltk
import unicodedata
import codecs
#import emoji #implementar isso depois 
from nltk.stem import RSLPStemmer

def normalize(sentence):
    sentence = sentence.lower()
    sentence = strip_accents(sentence)
    sentence = nltk.word_tokenize(sentence)
    return sentence

def strip_accents(sentence):
    try:
        sentence = unicode(sentence, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass

    sentence = unicodedata.normalize('NFD', sentence)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")
    return str(sentence)

def remove_stopWords(sentence):
    stopwords = nltk.corpus.stopwords.words('portuguese')
    phrase = []
    for word in sentence:
        if word not in stopwords:
            phrase.append(word)
    return phrase

def stemming(sentence):
    stemmer = RSLPStemmer()
    phrase = []
    for word in sentence:
        phrase.append(stemmer.stem(word.lower()))
    return phrase

def tokenize(sentence):
    sentence = sentence.lower()
    sentence = nltk.word_tokenize(sentence)
    return sentence
