# -*- coding: utf-8 -*-
"""
Python 2 notebook for the kaggle contest "Toxic Comment Classification Challenge"
data;
https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data

regression analysis for classifying comments into classes based on toxicity

800 out of 1322 on the leaderboard in the kaggle competition
"""

#standard imports
import pandas as pd
import numpy as np

import os
import warnings
warnings.filterwarnings('ignore')

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')
subm = pd.read_csv('data/sample_submission.csv')

df = pd.concat([train['comment_text'], test['comment_text']], axis=0)
df = df.fillna("unkown")
nrow_train = train.shape[0]

vectorizer = TfidfVectorizer(stop_words='english', max_features=50000)
X = vectorizer.fit_transform(df)

classes = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

    
preds = np.zeros((test.shape[0], len(classes)))

loss = []

for i, j in enumerate(classes):
    print('===Fit '+j)
    model = LogisticRegression()
    model.fit(X[:nrow_train], train[j])
    preds[:,i] = model.predict_proba(X[nrow_train:])[:,1]
    pred_train = model.predict_proba(X[:nrow_train])[:,1]
    print('ROC AUC:', roc_auc_score(train[j], pred_train))
    loss.append(roc_auc_score(train[j], pred_train))
    
print('mean column-wise ROC AUC:', np.mean(loss))

submid = pd.DataFrame({'id': subm["id"]})
submission = pd.concat([submid, pd.DataFrame(preds, columns = classes)], axis = 1)
submission.to_csv('submission.csv', index=False)