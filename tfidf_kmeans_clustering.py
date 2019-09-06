import os

documents = {}

dir_name = 'example-documents'

for filename in os.listdir(dir_name):
    f = open(dir_name + os.sep + filename)
    documents[filename] = f.read()
    f.close()


word_set = set()


for k, v in documents.items():
    documents[k] = v.lower().split()
    word_set = word_set.union(set(documents[k]))




document_words = {}

for k, v in documents.items():
    document_words[k] = dict.fromkeys(word_set, 0)
    for word in document_words[k]:
        document_words[k][word] += 1


tfs = {}


def compute_tf(word_dict, l):
    tf = {}
    sum_nk = len(l)
    for word, count in word_dict.items():
        tf[word] = count / sum_nk
    return tf


for key in documents.keys():
    tfs[key] = compute_tf(document_words[key], documents[key])



### sklearn

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

tfidf_vectorizer = TfidfVectorizer(preprocessor=prep)











