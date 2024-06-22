import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

genderData = pd.read_csv("gender_classification_v7.csv",low_memory = False)
newData = genderData

newData['gender']=newData['gender'].map({'Male':0, 'Female':1})

X = newData.iloc[:,:-1].values
y = newData.iloc[:,-1].values

X_train, X_test, y_train,y_test = train_test_split(X,y, test_size = 0.25, random_state = 0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)