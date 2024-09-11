# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-b6K85Y_VMI-hbRT_uXKq9NKI6F_a8U5
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/national+health+and+nutrition+health+survey+2013-2014+(nhanes)+age+prediction+subset.zip')

df.head()

df.tail()

#columns and rows
df.shape

df.info()

#data uniqueness
df.nunique()

df.describe().T

df.isnull().sum()

df.duplicated().sum()

#Gabbage
for i in df.select_dtypes(include='object').columns:
  print(df[i].value_counts())
  print("***"*10)

pd.get_dummies(df,columns=['age_group'], drop_first=True)

for i in df.select_dtypes(include='object').columns:
  print(df[i].value_counts())
  print("***"*10)

pd.get_dummies(df,columns=['age_group'], drop_first=1)

#Visualization
for i in df.select_dtypes(include='number').columns:
  sns.histplot(data=df, x=i)
  plt.show()

#outliers
for i in df.select_dtypes(include='number').columns:
  sns.boxplot(data=df, x=i)
  plt.show()

df.select_dtypes(include='object').columns

df.select_dtypes(include='number').columns

#checking for correlation
df.select_dtypes(include='number').corr()

plt.figure(figsize=(15,15))
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True)

#heatmap-interpretes relationships btn variables
df.select_dtypes(include='number').corr()
plt.figure(figsize=(15,15))
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True)

for i in df.select_dtypes(include='number').columns:
  plt.figure(figsize=(10,10))
  sns.kdeplot(data=df, x=i)
  plt.show()

