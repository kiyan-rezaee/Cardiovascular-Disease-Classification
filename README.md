# Cardiovascular-Disease
Cardiovascular disease (CVD) is a class of diseases that involve the heart or blood vessels. CVD includes coronary artery diseases (CAD) such as angina and myocardial infarction (commonly known as a heart attack). Other CVDs include stroke, heart failure, hypertensive heart disease, rheumatic heart disease, cardiomyopathy, abnormal heart rhythms, congenital heart disease, valvular heart disease, Carditis, aortic aneurysms, peripheral artery disease, thromboembolic disease, and venous thrombosis.

## Understanding Dataset

### Head of data 

```
   id    age  gender  height  weight  ap_hi  ap_lo  cholesterol  gluc  smoke  alco  active  cardio
0   0  18393       2     168    62.0    110     80            1     1      0     0       1       0
1   1  20228       1     156    85.0    140     90            3     1      0     0       1       1
2   2  18857       1     165    64.0    130     70            3     1      0     0       0       1
3   3  17623       2     169    82.0    150    100            1     1      0     0       1       1
4   4  17474       1     156    56.0    100     60            1     1      0     0       0       0
```

## Models 

### First model (10 epochs)

### information :
```
 Layer (type)                Output Shape              Param #
=================================================================
 dense (Dense)               (None, 11)                132

 dense_1 (Dense)             (None, 30)                360

 dense_2 (Dense)             (None, 2)                 62

=================================================================
Total params: 554
Trainable params: 554
Non-trainable params: 0
```

### Result : 

```
Epoch 1/10
53/53 [==============================] - 1s 6ms/step - loss: 0.6907 - categorical_accuracy: 0.5340 - val_loss: 0.6793 - val_categorical_accuracy: 0.5879
Epoch 2/10
53/53 [==============================] - 0s 3ms/step - loss: 0.6701 - categorical_accuracy: 0.5926 - val_loss: 0.6600 - val_categorical_accuracy: 0.6014
Epoch 3/10
53/53 [==============================] - 0s 2ms/step - loss: 0.6541 - categorical_accuracy: 0.6099 - val_loss: 0.6484 - val_categorical_accuracy: 0.6175
Epoch 4/10
53/53 [==============================] - 0s 2ms/step - loss: 0.6451 - categorical_accuracy: 0.6277 - val_loss: 0.6418 - val_categorical_accuracy: 0.6321
Epoch 5/10
53/53 [==============================] - 0s 2ms/step - loss: 0.6405 - categorical_accuracy: 0.6328 - val_loss: 0.6384 - val_categorical_accuracy: 0.6355
Epoch 6/10
53/53 [==============================] - 0s 3ms/step - loss: 0.6380 - categorical_accuracy: 0.6350 - val_loss: 0.6373 - val_categorical_accuracy: 0.6341
Epoch 7/10
53/53 [==============================] - 0s 3ms/step - loss: 0.6357 - categorical_accuracy: 0.6376 - val_loss: 0.6359 - val_categorical_accuracy: 0.6346
Epoch 8/10
53/53 [==============================] - 0s 3ms/step - loss: 0.6343 - categorical_accuracy: 0.6373 - val_loss: 0.6336 - val_categorical_accuracy: 0.6413
Epoch 9/10
53/53 [==============================] - 0s 3ms/step - loss: 0.6330 - categorical_accuracy: 0.6401 - val_loss: 0.6325 - val_categorical_accuracy: 0.6407
Epoch 10/10
53/53 [==============================] - 0s 3ms/step - loss: 0.6320 - categorical_accuracy: 0.6409 - val_loss: 0.6318 - val_categorical_accuracy: 0.6419
```

## Second model (Random forest)

### Result : 

```
              precision    recall  f1-score   support

           0       0.70      0.74      0.72      8609
           1       0.73      0.70      0.72      8891

    accuracy                           0.72     17500
   macro avg       0.72      0.72      0.72     17500
weighted avg       0.72      0.72      0.72     17500
```

## Third model (300 epochs)

### information : 
```
 Layer (type)                Output Shape              Param #
=================================================================
 dense (Dense)               (None, 11)                132

 dense_1 (Dense)             (None, 30)                360

 dense_2 (Dense)             (None, 60)                1860

 dense_3 (Dense)             (None, 25)                1525

 dense_4 (Dense)             (None, 2)                 52

=================================================================
Total params: 3,929
Trainable params: 3,929
Non-trainable params: 0
```
### Result : (last five epochs)
```
175/175 [==============================] - 0s 2ms/step - loss: 0.5424 - categorical_accuracy: 0.7324 - val_loss: 0.5737 - val_categorical_accuracy: 0.7059
Epoch 295/300
175/175 [==============================] - 0s 2ms/step - loss: 0.5440 - categorical_accuracy: 0.7314 - val_loss: 0.5645 - val_categorical_accuracy: 0.7190
Epoch 296/300
175/175 [==============================] - 0s 2ms/step - loss: 0.5448 - categorical_accuracy: 0.7316 - val_loss: 0.5532 - val_categorical_accuracy: 0.7289
Epoch 297/300
175/175 [==============================] - 0s 2ms/step - loss: 0.5449 - categorical_accuracy: 0.7306 - val_loss: 0.5627 - val_categorical_accuracy: 0.7247
Epoch 298/300
175/175 [==============================] - 0s 2ms/step - loss: 0.5419 - categorical_accuracy: 0.7330 - val_loss: 0.5597 - val_categorical_accuracy: 0.7239
Epoch 299/300
175/175 [==============================] - 0s 2ms/step - loss: 0.5431 - categorical_accuracy: 0.7324 - val_loss: 0.5553 - val_categorical_accuracy: 0.7301
Epoch 300/300
175/175 [==============================] - 0s 2ms/step - loss: 0.5438 - categorical_accuracy: 0.7328 - val_loss: 0.5531 - val_categorical_accuracy: 0.7303
```
