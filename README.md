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

### First model

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


