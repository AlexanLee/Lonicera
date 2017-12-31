# _*_coding:utf-8_*_

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation

model = Sequential()
model.add(Dense(20, 64))
model.add(Activation('tanh'))
model.add(Dropout(0.5))
model.add(Dense(64, 64))
