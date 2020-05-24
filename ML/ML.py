'''
Import the data
Clean the data
Split the Data into Training/Test Sets
Create a Model
Train a Model
Make predictions
Evaluate and Improve
'''

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

music_data = pd.read_csv('music.csv')
music_data

X = music_data.drop(columns = ['genre'])  #input dataset

y = music_data['genre'] #output dataset

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
prediction = model.predict(X_test)

score = accuracy_score(y_test, prediction)
score
