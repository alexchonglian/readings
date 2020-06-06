import pandas as pd
from nlpia.data.loaders import get_data
pd.options.display.width = 120
sms = get_data('sms-spam')
index = ['sms{}{}'.format(i, '!'*j) for (i,j) in zip(range(len(sms)), sms.spam)]
sms = pd.DataFrame(sms.values, columns=sms.columns, index=index)
sms['spam'] = sms.spam.astype(int)
#print(len(sms))
#print(sms.spam.sum())
#print(sms.head(6))

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize.casual import casual_tokenize
tfidf_model = TfidfVectorizer(tokenizer=casual_tokenize)
tfidf_docs = tfidf_model.fit_transform(raw_documents=sms.text).toarray()
#print(tfidf_docs.shape)
#print(sms.spam.sum())


mask = sms.spam.astype(bool).values
spam_centroid = tfidf_docs[mask].mean(axis=0)
ham_centroid = tfidf_docs[~mask].mean(axis=0)
#print(spam_centroid.round(2)) #array([0.06, 0. , 0. , ..., 0. , 0. , 0. ])
#print(ham_centroid.round(2)) #array([0.02, 0.01, 0. , ..., 0. , 0. , 0. ])

spamminess_score = tfidf_docs.dot(spam_centroid - ham_centroid)
#print(spamminess_score.round(2))


from sklearn.preprocessing import MinMaxScaler
sms['lda_score'] = MinMaxScaler().fit_transform(spamminess_score.reshape(-1,1))
sms['lda_predict'] = (sms.lda_score > .5).astype(int)
#print(sms['spam lda_predict lda_score'.split()].round(2).head(6))
#print((1. - (sms.spam - sms.lda_predict).abs().sum() / len(sms)).round(3))

from pugnlp.stats import Confusion
print(sms['spam lda_predict'.split()])
print(Confusion(sms['spam lda_predict'.split()]))











