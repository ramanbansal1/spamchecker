#!/usr/bin/env python
# coding: utf-8

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression


dataset = pd.read_csv("spam.csv")


target = dataset["Category"]
X = dataset['Message']
target = target.replace({"ham": 0, "spam": 1})

n_samples = len(dataset)


vectorizer = TfidfVectorizer()
vectorizer.fit(X)


X = vectorizer.transform(X)


model = LogisticRegression()

model.fit(X[:n_samples//2], target[:n_samples//2])


def predict(x):
	x = vectorizer.transform([x])
	return model.predict(x)[0]
  
 
joblib.dump(model, open("model.sav", "wb"))

joblib.dump(vectorizer, open("vectorizer.sav", "wb"))
