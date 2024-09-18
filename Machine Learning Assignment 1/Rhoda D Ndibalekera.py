# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1g5cswjjeXmfw0mDHx3izobryO2_RyDRz
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm

df = pd.read_csv('/content/national+health+and+nutrition+health+survey+2013-2014+(nhanes)+age+prediction+subset.zip')

df.head()

"""## **Data Wrangling**"""

#Check for missing Values
df.isnull().sum()
#there was no need of dropping any columns since none had missing data

#convert categorical data into numerical data
df['age_group'] = df['age_group'].map({'senior': 1, 'non-senior': 0})

# Display the data types
df.dtypes

# Display the first fields
df.head()

pd.get_dummies(df,columns=['age_group'], drop_first=True)

"""## **3. Exploratory Data Analysis (EDA):**

## Question 1: Can age be predicted using health and nutrition data from the dataset? **bold text**
"""

# Visualize the distribution of age
sns.histplot(df['RIDAGEYR'], kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Correlation matrix
correlation_matrix = df.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

"""## **Question 2: What is the relationship between lifestyle choices and age?**"""

# Visualize the relationship between age and lifestyle choices (PAQ605)
sns.boxplot(x='PAQ605', y='RIDAGEYR', data=df)
plt.title('Relationship between Lifestyle Choices and Age')
plt.xlabel('Lifestyle Choices (PAQ605)')
plt.ylabel('Age')
plt.show()

"""## **Question 3: How does respondents’ gender and body mass index correlate with age_group?**"""

# Correlation between gender, BMI, and age_group
print(df[['age_group', 'RIAGENDR', 'BMXBMI']].corr())

"""## **Question 4: Can LBXIN, body mass index, and PAQ605 be strong predictors of age?**"""

# Prepare the data for modeling
X = df[['LBXIN', 'BMXBMI', 'PAQ605']]
y = df['RIDAGEYR']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Display the coefficients
coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print(coefficients)

# Visualize the actual vs predicted values
plt.scatter(y_test, y_pred)
plt.title('Actual vs Predicted Age')
plt.xlabel('Actual Age')
plt.ylabel('Predicted Age')
plt.show()