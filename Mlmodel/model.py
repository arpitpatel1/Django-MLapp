from copyreg import pickle
import pandas as pd
import numpy as np
import pickle

dfi = pd.read_csv(r"C:\Users\Arpit Patel\Angular\Machine learning\My practice\insurance prediction\insurance.csv")
from sklearn.preprocessing import OrdinalEncoder

ordinal_encoder = OrdinalEncoder()
sex = dfi[["sex"]]

smoke = dfi[["smoker"]]
region = dfi[["region"]]
sex_encoded = ordinal_encoder.fit_transform(sex)

smoke_encoded = ordinal_encoder.fit_transform(smoke)
region_encoded = ordinal_encoder.fit_transform(region)

dfi["sex1"] = sex_encoded
dfi["smoke1"] = smoke_encoded
dfi["region1"] = region_encoded

dfi.drop(['sex'],axis=1,inplace=True)
dfi.drop(['region'],axis=1,inplace=True)
dfi.drop(['smoker'],axis=1,inplace=True)
y = dfi['charges']
del dfi['charges']
X = dfi.values
y = y.values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)
from sklearn import linear_model
model = linear_model.LinearRegression()
model.fit(X_train, y_train)

# print("Predict value " + str(model.predict([X_test[3]])))
# print("Real value " + str(y_test[3]))

pickle.dump(model,open('model.pkl','wb'))