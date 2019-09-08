import operator
import os
import re
import string
import nltk
from collections import defaultdict
from pprint import pprint

nltk.download('punkt')

documents = {}

dir_name = 'example-documents'

stopwords_f = open('stopwords.txt')
stopwords = stopwords_f.read().split('\n')

for filename in os.listdir(dir_name):
    f = open(dir_name + os.sep + filename)
    documents[filename] = f.read()
    f.close()

## 각 문서별 워드 리스트를 생성
for name, text in documents.items():
    text = text.lower()
    text = re.sub(r"[{}]".format(string.punctuation), " ", text)
    all_words = nltk.word_tokenize(text)
    # all_words = text.split()
    documents[name] = list(filter(lambda x: x not in stopwords, all_words))

dfs = defaultdict(lambda: 0)
# {word[string]: df[number]}
documents_tfs = defaultdict(lambda: {})

# { document_name[string]: { word[string]: tf[number] } }

# df를 계산
for name, words in documents.items():
    word_set = set(words)
    total_word_count = len(words)
    for word in word_set:
        dfs[word] += 1
        word_count = words.count(word)
        if word_count > 4 and len(word) > 2:
            documents_tfs[name][word] = (word_count / total_word_count) * 100000

for word, df in dfs.items():
    dfs[word] = df / len(documents)

documents_tf_idf = defaultdict(lambda: {})

# tf-idf 계산
for name, tfs in documents_tfs.items():
    for word, tf in tfs.items():
        documents_tf_idf[name][word] = tf / dfs[word]

documents_top_five_keywords = defaultdict(lambda: {})

for name, tf_idfs in documents_tf_idf.items():
    documents_top_five_keywords[name] = dict(sorted(tf_idfs.items(), key=operator.itemgetter(1), reverse=True)[:20])


pprint(documents_top_five_keywords)
