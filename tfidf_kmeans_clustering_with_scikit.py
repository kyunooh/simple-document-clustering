import os
import re
import string
from pprint import pprint

documents = []

dir_name = 'example-documents'

for filename in os.listdir(dir_name):
    f = open(dir_name + os.sep + filename)
    documents.append(f.read())
    f.close()


### sklearn

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


def preprocessing(text):
    text = text.lower()
    text = re.sub(r"[{}]".format(string.punctuation), " ", text)
    return text


tfidf_v = TfidfVectorizer(preprocessor=preprocessing, stop_words="english", use_idf=True)


tfidf = tfidf_v.fit_transform(documents)


kmeans = KMeans(n_clusters=5).fit(tfidf)

predicted = kmeans.predict(tfidf)


final = {}
count = 0
for filename in os.listdir(dir_name):
    final[filename] = predicted[count]
    count += 1

defined_cluster = {}

for k, v in final.items():
    if defined_cluster.get(v) is None:
        defined_cluster[v] = []
    defined_cluster.get(v).append(k)


pprint(defined_cluster)














