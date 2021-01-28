#!/usr/bin/env python
# coding: utf-8

# In[2]:


#standard imports
import pandas as pd
import numpy as np
from tqdm import tqdm
tqdm.pandas(desc='progress-bar')
from gensim.models import Doc2Vec
from sklearn import utils
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score, f1_score
from sklearn.feature_extraction.text import CountVectorizer

import gensim
from sklearn.linear_model import LogisticRegression
from gensim.models.doc2vec import TaggedDocument
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords


import multiprocessing
cores=multiprocessing.cpu_count()

import re
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[3]:


#read csv file into a dataframe(df)
df = pd.read_csv('loans.csv', nrows=100000)


# In[10]:


df['ORIGINAL_LANGUAGE'].value_counts()


# In[3]:


#extract relevant columns
df = df[['ORIGINAL_LANGUAGE','DESCRIPTION', 'STATUS']]


# In[9]:


#check dataframe values
df.info()


# In[6]:


#create variable to drop rows that do not have english descriptions for easier analysis
index_names = df[(df['ORIGINAL_LANGUAGE']=='Spanish') | (df['ORIGINAL_LANGUAGE']=='French')|(df['ORIGINAL_LANGUAGE']=='Russian')|(df['ORIGINAL_LANGUAGE']=='Portuguese')|(df['ORIGINAL_LANGUAGE']=='Indonesian')|(df['ORIGINAL_LANGUAGE']=='Vietnamese')].index


# In[7]:


df.drop(index_names, inplace=True)


# In[7]:


#drop all rows with null values
df=df.dropna()


# In[17]:


#reset index
df=df.reset_index()


# In[21]:


#keep only the two relevant columns
df = df[['DESCRIPTION','STATUS']]


# In[19]:


#clean up the descriptions column
def cleanText(text):
    text = BeautifulSoup(text, "lxml").text#remove break tags and other html markup
    text = re.sub(r'\|\|\|', r' ', text) 
    text = re.sub(r'http\S+', r'<URL>', text)
    text = text.lower()
    text = text.replace('\\r', '')
    text = text.replace('\\n', '')   
    text = text.replace('\r', '')
    text = text.replace('\n', '')    
    return text
df['DESCRIPTION']=df['DESCRIPTION'].apply(cleanText)


# In[26]:


#split dataframe into test, train samples and tokenize 
train, test = train_test_split(df, test_size=0.3, random_state=42)

#nltk.download('punkt')
def tokenize_text(text):
    tokens = []
    for sent in nltk.sent_tokenize(text):
        for word in nltk.word_tokenize(sent):
            if len(word) < 2:
                continue
            tokens.append(word.lower())
    return tokens

train_tagged = train.apply(
    lambda r: TaggedDocument(words=tokenize_text(r['DESCRIPTION']), tags=[r.STATUS]), axis=1)
test_tagged = test.apply(
    lambda r: TaggedDocument(words=tokenize_text(r['DESCRIPTION']), tags=[r.STATUS]), axis=1)


# In[28]:


#intiliaze doc2vec's dbow
model_dbow = Doc2Vec(
            dm=0, #use distributed bag of words 
            vector_size=300, #dimensions of feature vectors
            negative=5, #how many 'noise words' to be drawn
            hs=0,
            min_count=2, #analyze words used more than twice
            sample=0,
            workers=cores-1
)
#build the vocabulary
#model_dbow.build_vocab([x for x in tqdm(train_tagged.values)])


# In[31]:


#train the Doc2Vec model
#%%time
for epoch in range(30):
    model_dbow.train(utils.shuffle([x for x in tqdm(train_tagged.values)]), 
                    total_examples=len(train_tagged.values), epochs=1)
    model_dbow.alpha -= 0.002
    model_dbow.min_alpha = model_dbow.alpha


# In[35]:


#function for the final vector feature for the classifier
def vec_for_learning(model, tagged_docs):
    sents = tagged_docs.values
    targets, regressors = zip(*[(doc.tags[0], model.infer_vector(doc.words, steps=20)) for doc in sents])
    return targets, regressors 


# In[39]:


y_train, X_train = vec_for_learning(model_dbow, train_tagged)
y_test, X_test = vec_for_learning(model_dbow, test_tagged)

logreg = LogisticRegression(n_jobs=1, C=1e5)
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)


print('Testing accuracy %s' % accuracy_score(y_test, y_pred))
print('Testing F1 score: {}'.format(f1_score(y_test, y_pred, average='weighted')))


# In[65]:


model_dbow.most_similar([model_dbow.docvecs['funded']])


# In[66]:


model_dbow.most_similar(positive='business')


# In[67]:


model_dbow.most_similar(positive='funded')


# In[68]:


model_dbow.most_similar(positive='kiva')


# In[ ]:




