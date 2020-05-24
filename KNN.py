from sklearn.datasets import *
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier

import numpy as np

from random import randrange

digit = load_digits()
dig = pd.DataFrame(digit['data'][0:1700])
dig.head()

digit.keys()


def displayImage(i):
    plt.imshow(digit['images'][i], cmap='Greys_r')
    plt.show()

train_x = digit.data # les input variables
train_y = digit.target # les étiquettes (output variable)
#découpage du jeu de données
x_train,x_test,y_train,y_test=train_test_split(train_x,train_y,test_size=0.25) #0.25 pour indiquer 25%

KNN = KNeighborsClassifier(7) # on veut entrainer un 7-NN Classifier (on utilise 7 voisins)
KNN.fit(x_train, y_train)

print(KNN.score(x_test,y_test)*100,"%")
'''
image = randrange(1700)
test = np.array(digit['data'][image])
test1 = test.reshape(1,-1)

print(KNN.predict(test1))

displayImage(image)
'''
