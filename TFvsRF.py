import pandas as pd
import numpy as np
import tensorflow as tf

data = pd.read_csv('cardio_train1.csv')
# print(data.head())


# # EDA and preproccesing 
# print(data.isna().sum())
X = data.iloc[:, 1:-1]
Y = data.iloc[:, -1]
from sklearn.preprocessing import MinMaxScaler
mms = MinMaxScaler()
X = mms.fit_transform(X)
Y = pd.get_dummies(Y) # for neural network models

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=1)

# first model

model1 = tf.keras.models.Sequential([
    tf.keras.layers.Dense(11, activation='relu', input_shape=(11,)),
    tf.keras.layers.Dense(30, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')
])

model1.compile(optimizer=tf.keras.optimizers.Adam(0.001), loss=tf.keras.losses.CategoricalCrossentropy(), metrics=[tf.keras.metrics.CategoricalAccuracy()])
model1.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test), batch_size=1000)

print(model1.summary())