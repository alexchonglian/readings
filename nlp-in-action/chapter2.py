# 2.1
sentence = """Thomas Jefferson began building Monticello at the age of 26."""
#print(sentence.split())
#print(str.split(sentence))


import numpy as np
token_sequence = str.split(sentence)
vocab = sorted(set(token_sequence))
#print(', '.join(vocab))
num_tokens = len(token_sequence) 
vocab_size = len(vocab) 
onehot_vectors = np.zeros((num_tokens, vocab_size), int)
for i, word in enumerate(token_sequence):
    onehot_vectors[i, vocab.index(word)] = 1
#print(' '.join(vocab))
#print(onehot_vectors)

#2.2
import pandas as pd
#print(pd.DataFrame(onehot_vectors, columns=vocab))

#2.3
df = pd.DataFrame(onehot_vectors, columns=vocab)
df[df == 0] = ''
#print(df)

num_rows = 3000 * 3500 * 15
#print(num_rows) #157500000
num_bytes = num_rows * 1000000
#print(num_bytes) #157500000000000
#print(num_bytes / 1e9) #157500 # jigabytes
#print(num_bytes / 1e9 / 1000) #157.5 # terabytes

sentence_bow = {}
for token in sentence.split():
    sentence_bow[token] = 1
#print(sorted(sentence_bow.items()))

d = dict([(token, 1) for token in sentence.split()])
#print(d)
d = {token: 1 for token in sentence.split()}
#print(d)
series = pd.Series(d)
#print(type(series).__mro__)
#print(series.index)
#print(series)
df = pd.DataFrame(series, columns=['sent']).T
#print(type(df).__mro__)
#print(df)

#2.4
sentences = "Thomas Jefferson began building Monticello at the age of 26.\n"
sentences += "Construction was done mostly by local masons and carpenters.\n"
sentences += "He moved into the South Pavilion in 1770.\n"
sentences += "Turning Monticello into a neoclassical masterpiece was Jefferson's obsession."
corpus = {}
for i, sent in enumerate(sentences.split('\n')):
    #print(i, sent)
    corpus['sent{}'.format(i)] = {tok:1 for tok in sent.split()}
#print(corpus)
#df = pd.DataFrame.from_records(corpus)
df = pd.DataFrame.from_records(corpus).fillna(0).astype(int).T
#print(df)
#print(df[df.columns[:10]])
#print(df.columns)
#print(df.columns.values)
#print(type(df.columns.values))
#print(df.T.columns.values)
#print(df.keys())
#print(df.keys() == df.columns)
#idx = df.columns
#print(type(idx).__mro__)
#print(dir(idx))
#print(dir(df))
#print(np.array(df))
#print(list(df))

#2.5
v1 = pd.np.array([1, 2, 3])
v2 = pd.np.array([2, 3, 4])
#print(v1.shape, v2.shape)
p1 = v1.dot(v2)
p2 = (v1 * v2).sum()
p3 = v1.T @ v2
#print((v1*v2).shape)
p4 = sum([x1 * x2 for x1, x2 in zip(v1, v2)])
#print(p1, p2, p3, p4)
#print(v1)
#print(v2)
#print(v1.reshape(-1, 1).T)
#print(v2.reshape(-1, 1).T)

#2.6
df = df.T
#print(df.sent0.dot(df.sent1))
#print(df.sent0.dot(df.sent2))
#print(df.sent0.dot(df.sent3))
#print(df['sent0'])
#print(df.sent0)

common_words = [(k, v) for (k, v) in (df.sent0 & df.sent3).items() if v]
#print(common_words)

#2.7
import re
sentence = """Thomas Jefferson began building Monticello at the age of 26."""
tokens = re.split(r'[-\s.,;!?]+', sentence)
#print(tokens)

pattern = re.compile(r"([-\s.,;!?])+")
tokens = pattern.split(sentence)
#print(tokens[-10:])

sentence = """Thomas Jefferson began building Monticello at the age of 26."""
tokens = pattern.split(sentence)
filtered = [x for x in tokens if x and x not in '- \t\n.,;!?']
#print(filtered)

import regex

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+|$[0-9.]+|\S+')
#print(tokenizer.tokenize(sentence))

from nltk.tokenize import TreebankWordTokenizer 
sentence = """Monticello wasn't designated as UNESCO World Heritage Site until 1987.""" 
tokenizer = TreebankWordTokenizer() 
#print(tokenizer.tokenize(sentence))

from nltk.tokenize.casual import casual_tokenize
message = """RT @TJMonticello Best day everrrrrrr at Monticello. Awesommmmmmeeeeeeee day :*)"""
#print(casual_tokenize(message))
#print(casual_tokenize(message, reduce_len=True, strip_handles=True))

sentence = """Thomas Jefferson began building Monticello at the age of 26."""
pattern = re.compile(r"([-\s.,;!?])+")
tokens = pattern.split(sentence)
tokens = [x for x in tokens if x and x not in '- \t\n.,;!?']
#print(tokens)
from nltk.util import ngrams
#print(list(ngrams(tokens, 2)))
#print(list(ngrams(tokens, 3)))

two_grams = list(ngrams(tokens, 2))
#print([" ".join(x) for x in two_grams])

stop_words = ['a', 'an', 'the', 'on', 'of', 'off', 'this', 'is']
tokens = ['the', 'house', 'is', 'on', 'fire']
tokens_without_stopwords = [x for x in tokens if x not in stop_words]
#print(tokens_without_stopwords)

#2.8
import nltk
#nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')
#print(len(stop_words))
#print(stop_words[:7])
#print([sw for sw in stop_words if len(sw) == 1])
stop_words = set(stop_words)

#2.9
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS as sklearn_stop_words
#print(len(sklearn_stop_words))
#print(len(stop_words))
#print(len(stop_words.union(sklearn_stop_words)))
#print(len(stop_words.intersection(sklearn_stop_words)))


def stem(phrase):
    return ' '.join([re.findall('^(.*ss|.*?)(s)?$', word)[0][0].strip("'") for word in phrase.lower().split()])
#print(stem('houses'))
#print(stem("Doctor House's calls"))


from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
j = ' '.join([stemmer.stem(w).strip("'") for w in "dish washer's washed dishes".split()])
#print(j)

#nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
#print(lemmatizer.lemmatize("better")) #'better'
#print(lemmatizer.lemmatize("better", pos="a")) #'good'
#print(lemmatizer.lemmatize("good", pos="a")) #'good'
#print(lemmatizer.lemmatize("goods", pos="a")) #'goods'
#print(lemmatizer.lemmatize("goods", pos="n")) #'good'
#print(lemmatizer.lemmatize("goodness", pos="n")) #'goodness'
#print(lemmatizer.lemmatize("best", pos="a")) #'best'


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sa = SentimentIntensityAnalyzer()
#print(len(sa.lexicon))
tok_score = [(tok, score) for tok, score in sa.lexicon.items() if " " in tok]
#print(tok_score)
#print(sa.polarity_scores(text="Python is very readable and it's great for NLP."))
#print(sa.polarity_scores(text="Python is not a bad choice for most applications."))

corpus = ["Absolutely perfect! Love it! :-) :-) :-)",
    "Horrible! Completely useless. :(",
    "It was OK. Some good and some bad things."]
for doc in corpus:
    scores = sa.polarity_scores(doc)
    #print('{:+}: {}'.format(scores['compound'], doc))


from nlpia.data.loaders import get_data
movies = get_data('hutto_movies')
#print(dir(movies))
#print(movies.head().round(2))
#print(movies.describe().round(2))


import pandas as pd
pd.set_option('display.width', 75)
from nltk.tokenize import casual_tokenize
bags_of_words = []

from collections import Counter
for text in movies.text:
    bags_of_words.append(Counter(casual_tokenize(text)))
df_bows = pd.DataFrame.from_records(bags_of_words)
df_bows = df_bows.fillna(0).astype(int)
print(df_bows.shape) #(10605, 20756)
print(df_bows.head())
print(df_bows.head()[list(bags_of_words[0].keys())])


from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
print((movies.sentiment > 0))
nb = nb.fit(df_bows, movies.sentiment > 0)
movies['predicted_sentiment'] = nb.predict_proba(df_bows) * 8 - 4
movies['error'] = (movies.predicted_sentiment - movies.sentiment).abs()
print(movies.error.mean().round(1))
movies['sentiment_ispositive'] = (movies.sentiment > 0).astype(int)
movies['predicted_ispositiv'] = (movies.predicted_sentiment > 0).astype(int)
movies['''sentiment predicted_sentiment sentiment_ispositive predicted_ispositive'''.split()].head(8)


products = get_data('hutto_products')
bags_of_words = []
for text in products.text:
    bags_of_words.append(Counter(casual_tokenize(text)))
df_product_bows = pd.DataFrame.from_records(bags_of_words)
df_product_bows = df_product_bows.fillna(0).astype(int)
df_all_bows = df_bows.append(df_product_bows)
print(df_all_bows.columns)
df_product_bows = df_all_bows.iloc[len(movies):][df_bows.columns]
print(df_product_bows.shape)
print(df_bows.shape)
products[ispos] = (products.sentiment > 0).astype(int)
products['predicted_ispositive'] = nb.predict(df_product_bows.values).astype(int)
print(products.head())
print((products.pred == products.ispos).sum() / len(products))

