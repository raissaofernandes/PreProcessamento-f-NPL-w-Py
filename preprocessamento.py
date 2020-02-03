import nltk
import unicodedata
import codecs
#import emoji IMPLEMENTAR ISSO DEPOIS!!!
from nltk.stem import RSLPStemmer

def normalize(sentence):
    sentence = sentence.lower()
    sentence = strip_accents(sentence)
    sentence = nltk.word_tokenize(sentence)
    return sentence

def tokenize(sentence):
    sentence = sentence.lower()
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

  #Remover caracteteres irrelevantes como os não alfanuméricos;
  #Remover palavras que não são relevantes, como as menções indicadas com "@";
  #Converter termos para minúsculos, homogeneizando os dados (OLÁ - olá);
  #Combinar palavras escritas incorretamente para uma única representação (legaaalll - legal);
  #Considerar lematização (reduzir palavras como "sou", "é" para uma forma desflexionada como "ser")
  #Quebrar o seu texto em termos.
def limpeza_dos_dados(df, text_field):
    df[text_field] = df[text_field].str.replace(r"http\S+", "")
    df[text_field] = df[text_field].str.replace(r"http", "")
    df[text_field] = df[text_field].str.replace(r"@\S+", "")
    df[text_field] = df[text_field].str.replace(r"[^A-Za-z0-9(),!?@\'\`\"\_\n]", " ")
    df[text_field] = df[text_field].str.replace(r"@", "at")
    df[text_field] = df[text_field].str.lower()
    return df
