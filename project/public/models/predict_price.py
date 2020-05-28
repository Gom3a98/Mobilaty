import numpy as np
import pandas as pd

data = pd.read_csv('train.csv')
x = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
m, n = len(x), len(x[0])+1
x = np.append(arr = np.ones((m, 1)).astype(int), values = x, axis = 1)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

pipe = make_pipeline(StandardScaler(), LogisticRegression())
pipe.fit(x_train, y_train)
y_pred = pipe.predict(x_train)

print(pipe.score(x_train, y_train))#0.975625
print(pipe.score(x_test, y_test)) #0.965

joblib.dump(pipe, 'predictPrice.pkl')