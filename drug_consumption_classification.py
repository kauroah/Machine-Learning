# -*- coding: utf-8 -*-
"""Machine Learning project(Drug Consumption Classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tEuPCZgNEKDP9vvSO03Fj8xLm6-kJD_n
"""

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from plotly.subplots import make_subplots
import plotly.graph_objects as go

import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('/content/drug_consumption.csv')

df.info()

df.shape

df.describe()

df.isnull().sum()

df.duplicated().sum()

df.head()

age = {
          -0.95197: '18-24',
          -0.07854: '25 - 34',
          0.49788: '35 - 44',
          1.09449: '45 - 54',
          1.82213: '55 - 64',
          2.59171: '65+'
          }

gender = {
            0.48246: 'Female',
            -0.48246: 'Male'
            }

education = {
            -2.43591: 'Left School Before 16 years',
            -1.73790: 'Left School at 16 years',
            -1.43719: 'Left School at 17 years',
            -1.22751: 'Left School at 18 years',
            -0.61113: 'Some College,No Certificate Or Degree',
            -0.05921: 'Professional Certificate/ Diploma',
            0.45468: 'University Degree',
            1.16365: 'Masters Degree',
            1.98437: 'Doctorate Degree',
            }

country = {
            -0.09765: 'Australia',
            0.24923: 'Canada',
            -0.46841: 'New Zealand',
            -0.28519: 'Other',
            0.21128: 'Republic of Ireland',
            0.96082: 'UK',
            -0.57009: 'USA'
            }

ethnicity = {
            -0.50212: 'Asian',
            -1.10702: 'Black',
            1.90725: 'Mixed-Black/Asian',
            0.12600: 'Mixed-White/Asian',
            -0.22166: 'Mixed-White/Black',
            0.11440: 'Other',
            -0.31685: 'White'
            }

usage = {
    'CL0': 'Never Used',
    'CL1': 'Used over a Decade Ago',
    'CL2': 'Used in Last Decade',
    'CL3': 'Used in Last Year',
    'CL4': 'Used in Last Month',
    'CL5': 'Used in Last Week',
    'CL6': 'Used in Last Day',
    }

df['Age'] = df['Age'].replace(age)
df['Gender'] = df['Gender'].replace(gender)
df['Education'] = df['Education'].replace(education)
df['Country'] = df['Country'].replace(country)
df['Ethnicity'] = df['Ethnicity'].replace(ethnicity)
df['Alcohol'] = df['Alcohol'].replace(usage)
df['Amphet'] = df['Amphet'].replace(usage)
df['Amyl'] = df['Amyl'].replace(usage)
df['Benzos'] = df['Benzos'].replace(usage)
df['Caff'] = df['Caff'].replace(usage)
df['Cannabis'] = df['Cannabis'].replace(usage)
df['Choc'] = df['Choc'].replace(usage)
df['Coke'] = df['Coke'].replace(usage)
df['Crack'] = df['Crack'].replace(usage)
df['Ecstasy'] = df['Ecstasy'].replace(usage)
df['Heroin'] = df['Heroin'].replace(usage)
df['Ketamine'] = df['Ketamine'].replace(usage)
df['Legalh'] = df['Legalh'].replace(usage)
df['LSD'] = df['LSD'].replace(usage)
df['Meth'] = df['Meth'].replace(usage)
df['Mushrooms'] = df['Mushrooms'].replace(usage)
df['Nicotine'] = df['Nicotine'].replace(usage)
df['Semer'] = df['Semer'].replace(usage)
df['VSA'] = df['VSA'].replace(usage)

df.head(3)

num_cols = df.select_dtypes(include=['float64']).columns
cat_cols = df.select_dtypes(include=['object']).columns

f, ax = plt.subplots(2,4 , figsize=(15,10))
ax = ax.flatten()

for index, cols in enumerate(num_cols):
    sns.histplot(data = df, x = cols , ax= ax[index], kde=True)
    ax[index].set_title(cols)

plt.tight_layout()
plt.show()

f, ax= plt.subplots(2,4 , figsize=(15,10))
ax = ax.flatten()

for index, cols in enumerate(num_cols):
    sns.boxplot(data = df, y = cols , ax = ax[index])
    ax[index].set_title(cols)

plt.tight_layout()
plt.show()

age_alcohol = df.groupby(['Age','Alcohol']).size().reset_index(name='count')

age_alcohol

# @title Age vs Alcohol

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
plt.subplots(figsize=(8, 8))
df_2dhist = pd.DataFrame({
    x_label: grp['Alcohol'].value_counts()
    for x_label, grp in age_alcohol.groupby('Age')
})
sns.heatmap(df_2dhist, cmap='viridis')
plt.xlabel('Age')
_ = plt.ylabel('Alcohol')

# @title Alcohol

from matplotlib import pyplot as plt
import seaborn as sns
age_alcohol.groupby('Alcohol').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

# @title Age

from matplotlib import pyplot as plt
import seaborn as sns
age_alcohol.groupby('Age').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

# @title count

from matplotlib import pyplot as plt
age_alcohol['count'].plot(kind='line', figsize=(8, 4), title='count')
plt.gca().spines[['top', 'right']].set_visible(False)

# @title count

from matplotlib import pyplot as plt
age_alcohol['count'].plot(kind='hist', bins=20, title='count')
plt.gca().spines[['top', 'right',]].set_visible(False)

px.bar(age_alcohol, y= 'count', x = 'Age' , color = 'Alcohol', barmode = 'group', title = 'Alcohol use by age', text_auto = True)

gender_alcohol = df.groupby(['Gender','Alcohol']).size().reset_index(name='count')

gender_alcohol

px.bar(gender_alcohol, y= 'count', x = 'Gender' , color = 'Alcohol', barmode = 'group', title = 'Alcohol use by Gender', text_auto = True)

age_nicotine = df.groupby(['Age','Nicotine']).size().reset_index(name='count')

age_nicotine

px.bar(age_nicotine , x='Age', y= 'count' , color = 'Nicotine', barmode = 'group', title = 'Nicotine use by Age', text_auto = True )

gender_nicotine = df.groupby(['Gender','Nicotine']).size().reset_index(name='count')

gender_nicotine

px.bar(gender_nicotine, y= 'count', x = 'Gender' , color = 'Nicotine', barmode = 'group', title = 'Nicotine use by Gender', text_auto = True)

UK = df[df['Country'] == 'UK']
UK_alcohol = UK.groupby(['Alcohol']).size().reset_index(name='count')
UK_alcohol

fig = px.pie(UK_alcohol , values = 'count',names= 'Alcohol',title = 'UK alcohol use status')
fig.update_traces(textposition='outside',textinfo='label + percent + value')

UK_Nicotine = UK.groupby(['Nicotine']).size().reset_index(name='count')
UK_Nicotine

fig = px.pie(UK_Nicotine , values = 'count',names= 'Nicotine',title = 'UK Nicotine use status')
fig.update_traces(textposition='outside',textinfo='label + percent + value')

sns.heatmap(df[num_cols].corr(),annot=True, cmap='Reds')
  plt.show()

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

import tensorflow as tf
import xgboost as xgb


from sklearn.metrics import accuracy_score , classification_report

df = df.drop('ID', axis = 1)

label_encoder = LabelEncoder()

for col in cat_cols:
    df[col] = label_encoder.fit_transform(df[col])

features = ['Age', 'Gender', 'Education', 'Country', 'Ethnicity', 'Nscore',
            'Escore', 'Oscore', 'Ascore', 'Cscore', 'Impulsive', 'SS', 'Nicotine']

X = df[features]
Y = df['Alcohol']

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
RF = RandomForestClassifier(random_state=42)
RF.fit(X_train,Y_train)

pred_RF = RF.predict(X_test)
print(classification_report(Y_test,pred_RF))

print(f'accuracy : {accuracy_score(Y_test,pred_RF)}')

SVM = SVC(C=1 , kernel = 'rbf')

SVM.fit(X_train,Y_train)

pred_SVM = SVM.predict(X_test)

print(classification_report(Y_test,pred_SVM))

print(f'accuracy : {accuracy_score(Y_test,pred_SVM)}')



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV

# Load data
df = pd.read_csv('/content/drug_consumption.csv')

# Preprocess data (assuming your preprocessing steps here)
# Replace encoded values with readable values (you already did this)

# Handle missing values if any (example)
df = df.dropna()

# Split data into features and target
X = df.drop(['Alcohol'], axis=1)  # Drop the 'Alcohol' column from features
y = df['Alcohol']  # Assign the 'Alcohol' column to y as the target


# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing pipeline
numeric_features = num_cols  # List of numeric columns
categorical_features = cat_cols  # List of categorical columns

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Define the model
model = RandomForestClassifier(random_state=42)

# Create a pipeline
clf = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', model)
])

# Train the model
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate the model
print("Classification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Hyperparameter tuning
param_grid = {
    'classifier__n_estimators': [100, 200],
    'classifier__max_depth': [None, 10, 20],
    'classifier__min_samples_split': [2, 5, 10],
}

grid_search = GridSearchCV(clf, param_grid, cv=5)
grid_search.fit(X_train, y_train)

print("Best parameters found: ", grid_search.best_params_)
print("Best cross-validation score: {:.2f}".format(grid_search.best_score_))

# Evaluate the best model on the test set
best_model = grid_search.best_estimator_
y_pred_best = best_model.predict(X_test)

print("Classification Report (Best Model):")
print(classification_report(y_test, y_pred_best))

print("Confusion Matrix (Best Model):")
print(confusion_matrix(y_test, y_pred_best))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV

# Load data
df = pd.read_csv('/content/drug_consumption.csv')

# Preprocess data (assuming your preprocessing steps here)
# Replace encoded values with readable values (you already did this)

# Handle missing values if any (example)
df = df.dropna()

# Assuming you have already replaced encoded values with readable values

# Define target column
target_column = 'Alcohol'  # Replace 'Alcohol' with the actual target column name

# Split data into features and target
X = df.drop([target_column], axis=1)  # Drop the target column from features
y = df[target_column]  # Assign the target column to y

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing pipeline
numeric_features = X.select_dtypes(include=['float64']).columns
categorical_features = X.select_dtypes(include=['object']).columns

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Define the model
model = RandomForestClassifier(random_state=42)

# Create a pipeline
clf = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', model)
])

# Train the model
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate the model
print("Classification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Hyperparameter tuning
param_grid = {
    'classifier__n_estimators': [100, 200],
    'classifier__max_depth': [None, 10, 20],
    'classifier__min_samples_split': [2, 5, 10],
}

grid_search = GridSearchCV(clf, param_grid, cv=5)
grid_search.fit(X_train, y_train)

print("Best parameters found: ", grid_search.best_params_)
print("Best cross-validation score: {:.2f}".format(grid_search.best_score_))

# Evaluate the best model on the test set
best_model = grid_search.best_estimator_
y_pred_best = best_model.predict(X_test)

print("Classification Report (Best Model):")
print(classification_report(y_test, y_pred_best))

print("Confusion Matrix (Best Model):")
print(confusion_matrix(y_test, y_pred_best))