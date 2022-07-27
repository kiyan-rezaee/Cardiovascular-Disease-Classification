from random import random
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

# # first model

# model1 = tf.keras.models.Sequential([
#     tf.keras.layers.Dense(11, activation='relu', input_shape=(11,)),
#     tf.keras.layers.Dense(30, activation='relu'),
#     tf.keras.layers.Dense(2, activation='softmax')
# ])

# model1.compile(optimizer=tf.keras.optimizers.Adam(0.001), loss=tf.keras.losses.CategoricalCrossentropy(), metrics=[tf.keras.metrics.CategoricalAccuracy()])
# model1.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test), batch_size=1000)

# print(model1.summary())

# # second model

# from sklearn.ensemble import RandomForestClassifier

# model2 = RandomForestClassifier(n_estimators=300)

# x_train, x_test, y_train, y_test = train_test_split(X, data.iloc[:, -1], random_state=1)

# model2.fit(x_train, y_train)

# # evaluate 

# from sklearn import metrics

# print(metrics.classification_report(y_true=y_test, y_pred=model2.predict(x_test)))

# third model

model3 = tf.keras.models.Sequential([
    tf.keras.layers.Dense(11, activation='relu', input_shape=(11,)),
    tf.keras.layers.Dense(30, activation='relu'),
    tf.keras.layers.Dense(60, activation='relu'),
    tf.keras.layers.Dense(25, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')
])
model3.compile(optimizer=tf.keras.optimizers.Adam(0.001), loss=tf.keras.losses.CategoricalCrossentropy(), metrics=[tf.keras.metrics.CategoricalAccuracy()])
model3.fit(X_train, y_train, epochs=300, validation_data=(X_test, y_test), batch_size=300)
print(model3.summary())