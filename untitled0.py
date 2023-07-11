# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17kPPN1UD152U_oY6qAmZFiRZCimhDdgK
"""

import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
from sklearn import linear_model

import seaborn as sns
import matplotlib.pyplot as plt

day_copy = pd.read_csv("day_copy.csv")
day_copy.head()

df = day_copy.drop(['dteday','yr','casual','registered'], axis = 1)
day_copy.head(10)

"""# Dropped Attributes that i think we don't need

"""

sns.pairplot(df)
plt.show()

"""#using matplotlib.pyplot to plot the attributes."""

df.weathersit.value_counts()

def monthday(x):
    if x == 1:
        return 'Jan'
    elif x == 2:
        return 'Feb'
    elif x == 3:
        return 'Mar'
    elif x == 4:
        return 'Apr'
    elif x == 5:
        return 'May'
    elif x == 6:
        return 'Jun'
    elif x == 7:
        return 'Jul'
    elif x == 8:
        return 'Aug'
    elif x == 9:
        return 'Sep'
    elif x == 10:
        return 'Oct'
    elif x == 11:
        return 'Nov'
    elif x == 12:
        return 'Dec'

df['month'] = df['mnth'].apply(monthday)
df = df.drop('mnth' , axis = 1 )
df.head()

def day_name(x):
    if x == 1:
        return 'Sun'
    elif x == 2:
        return 'Mon'
    elif x == 3:
        return 'Tue'
    elif x == 4:
        return 'Wed'
    elif x == 5:
        return 'Thu'
    elif x == 6:
        return 'Fri'
    elif x == 7:
        return 'Sat'

df['wkd'] = df['weekday'].apply(day_name)
df = df.drop('weekday' , axis = 1 )
df.head()

def h_name(x):
  if x== 1:
    return "Holiday"
  elif x == 0:
    return "No Holiday"

df['Holiday'] = df['holiday'].apply(h_name)
df = df.drop('holiday' , axis = 1 )
df.head()

wkd_dummy = pd.get_dummies(df.wkd, drop_first = True)
wkd_dummy.head()

month_dummy = pd.get_dummies(df.month, drop_first = True)
month_dummy.head()

wkd_dummy = pd.get_dummies(df.wkd, drop_first = True)
wkd_dummy.head()

Holiday_dummy = pd.get_dummies(df.Holiday, drop_first = True)
Holiday_dummy.head()

data = pd.concat([Holiday_dummy,wkd_dummy,month_dummy ], axis =1)
data.head(20)

Data = pd.concat([day_copy,data ], axis =1)
Data.head(20)

df['season'].plot(kind = 'box')

final = Data.drop(['dteday'], axis = 1)
final.head(20)

final.head

import sklearn
from sklearn.model_selection import train_test_split

"""#data division into train and test"""

final_train, final_test = train_test_split(final, train_size = 0.8, random_state = 100)
print(final_train.shape)
print(final_test.shape)

from sklearn.preprocessing import MinMaxScaler

scalar = MinMaxScaler()

numeric = ['temp','hum','windspeed','atemp']

"""#fitting the scalar on dataframe"""

final_train[numeric] = scalar.fit_transform(final_train[numeric])

final_train.head()