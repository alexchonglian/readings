from nltk.tokenize import TreebankWordTokenizer
sentence = """The faster Harry got to the store, the faster Harry, the faster, would get home."""
tokenizer = TreebankWordTokenizer()
tokens = tokenizer.tokenize(sentence.lower())
#print(tokens)

from collections import Counter
bag_of_words = Counter(tokens)
#print(bag_of_words)
#print(bag_of_words.most_common(4))

times_harry_appears = bag_of_words['harry']
num_unique_words = len(bag_of_words)
tf = times_harry_appears / num_unique_words
#print(round(tf, 2))

from collections import Counter
from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
from nlpia.data.loaders import kite_text
tokens = tokenizer.tokenize(kite_text.lower())
token_counts = Counter(tokens)
#print(token_counts)

import nltk
nltk.download('stopwords', quiet=True)
stopwords = nltk.corpus.stopwords.words('english')
tokens = [x for x in tokens if x not in stopwords]
kite_counts = Counter(tokens)
#print(kite_counts)

document_vector = []
doc_length = len(tokens)
for key, value in kite_counts.most_common():
    document_vector.append(value / doc_length)
#print(document_vector)

#from nlpia.data.loaders import harry_docs as docs
docs = ["The faster Harry got to the store, the faster and faster Harry would get home.", "Harry is hairy and faster than Jill.", "Jill is not as hairy as Harry."]
#print(docs)


doc_tokens = []
for doc in docs:
    doc_tokens += [sorted(tokenizer.tokenize(doc.lower()))]
#print(len(doc_tokens[0]))
all_doc_tokens = sum(doc_tokens, [])
#print(len(all_doc_tokens))
lexicon = sorted(set(all_doc_tokens))
#print(len(lexicon))
#print(lexicon)

from collections import OrderedDict
zero_vector = OrderedDict((token, 0) for token in lexicon)
#print(zero_vector)


import copy
doc_vectors = []
for doc in docs: 
    vec = copy.copy(zero_vector)
    tokens = tokenizer.tokenize(doc.lower()) 
    token_counts = Counter(tokens) 
    for key, value in token_counts.items(): 
        vec[key] = value / len(lexicon) 
    doc_vectors.append(vec)

#for v in doc_vectors:print(v)

#3.1
import math
def cosine_sim(vec1, vec2): 
    """ Let's convert our dictionaries to lists for easier matching.""" 
    vec1 = [val for val in vec1.values()] 
    vec2 = [val for val in vec2.values()] 
    dot_prod = 0 
    for i, v in enumerate(vec1): 
        dot_prod += v * vec2[i] 
    mag_1 = math.sqrt(sum([x**2 for x in vec1])) 
    mag_2 = math.sqrt(sum([x**2 for x in vec2])) 
    return dot_prod / (mag_1 * mag_2)


nltk.download('brown')
from nltk.corpus import brown
#print(brown.words()[:10])
#print(brown.tagged_words()[:5])
#print(len(brown.words()))

from collections import Counter
puncs = {',', '.', '--', '-', '!', '?', ':', ';', '``', "''", '(', ')', '[', ']'}
word_list = (x.lower() for x in brown.words() if x not in puncs)
token_counts = Counter(word_list)
#print(token_counts.most_common(20))


from nlpia.data.loaders import kite_text, kite_history
kite_intro = kite_text.lower()
intro_tokens = tokenizer.tokenize(kite_intro)
kite_history = kite_history.lower()
history_tokens = tokenizer.tokenize(kite_history)
intro_total = len(intro_tokens)
#print(intro_total)
history_total = len(history_tokens)
#print(history_total)


intro_tf = {}
history_tf = {}
intro_counts = Counter(intro_tokens)
history_counts = Counter(history_tokens)
intro_tf['kite'] = intro_counts['kite'] / intro_total
history_tf['kite'] = history_counts['kite'] / history_total
#print('Term Frequency of "kite" in intro is: {:.4f}'.format(intro_tf['kite']))
#print('Term Frequency of "kite" in history is: {:.4f}'.format(history_tf['kite']))

intro_tf['and'] = intro_counts['and'] / intro_total
history_tf['and'] = history_counts['and'] / history_total
#print('Term Frequency of "and" in intro is: {:.4f}'.format(intro_tf['and']))
#print('Term Frequency of "and" in history is: {:.4f}'.format(history_tf['and']))

num_docs_containing_and = 0
num_docs_containing_kite = 0
num_docs_containing_china = 0
for doc in [intro_tokens, history_tokens]:
    if 'and' in doc:
        num_docs_containing_and += 1
    if 'kite' in doc:
        num_docs_containing_kite += 1
    if 'china' in doc:
        num_docs_containing_china += 1

intro_tf['china'] = intro_counts['china'] / intro_total
history_tf['china'] = history_counts['china'] / history_total


num_docs = 2
intro_idf = {}
history_idf = {}
intro_idf['and'] = num_docs / num_docs_containing_and
history_idf['and'] = num_docs / num_docs_containing_and
intro_idf['kite'] = num_docs / num_docs_containing_kite
history_idf['kite'] = num_docs / num_docs_containing_kite
intro_idf['china'] = num_docs / num_docs_containing_china
history_idf['china'] = num_docs / num_docs_containing_china

intro_tfidf = {}
intro_tfidf['and'] = intro_tf['and'] * intro_idf['and']
intro_tfidf['kite'] = intro_tf['kite'] * intro_idf['kite']
intro_tfidf['china'] = intro_tf['china'] * intro_idf['china']

history_tfidf = {}
history_tfidf['and'] = history_tf['and'] * history_idf['and']
history_tfidf['kite'] = history_tf['kite'] * history_idf['kite']
history_tfidf['china'] = history_tf['china'] * history_idf['china']


#log_tf = log(term_occurences_in_doc) - log(num_terms_in_doc)
#log_log_idf = log(log(total_num_docs) - log(num_docs_containing_term))
#log_tf_idf = log_tf + log_idf

document_tfidf_vectors = []
for doc in docs: 
    vec = copy.copy(zero_vector)
    tokens = tokenizer.tokenize(doc.lower()) 
    token_counts = Counter(tokens) 
    for key, value in token_counts.items(): 
        docs_containing_key = 0 
        for _doc in docs: 
            if key in _doc: 
                docs_containing_key += 1 
        tf = value / len(lexicon) 
        if docs_containing_key: 
            idf = len(docs) / docs_containing_key 
        else: 
            idf = 0 
        vec[key] = tf * idf 
    document_tfidf_vectors.append(vec)
#print(document_tfidf_vectors)

query = "How long does it take to get to the store?"
query_vec = copy.copy(zero_vector)
query_vec = copy.copy(zero_vector)
tokens = tokenizer.tokenize(query.lower())
token_counts = Counter(tokens)
for key, value in token_counts.items():
    docs_containing_key = 0
    for _doc in docs:
        if key in _doc.lower():
            docs_containing_key += 1
    if docs_containing_key == 0:
        continue
    tf = value / len(tokens)
    idf = len(docs) / docs_containing_key
    query_vec[key] = tf * idf

#print(cosine_sim(query_vec, document_tfidf_vectors[0])) #0.5235048549676834
#print(cosine_sim(query_vec, document_tfidf_vectors[1])) #0.0
#print(cosine_sim(query_vec, document_tfidf_vectors[2])) #0.0


from sklearn.feature_extraction.text import TfidfVectorizer
corpus = docs
vectorizer = TfidfVectorizer(min_df=1)
model = vectorizer.fit_transform(corpus)
print(model.todense().round(2))