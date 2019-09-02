import requests
import json
# import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import requests
import json# Importing the dataset

df=pd.read_csv("train.csv")
sex=pd.get_dummies(df["Sex"])
a=df["Age"].fillna(df["Age"].mean()).astype(int)
x_min,x_max= a.min(),a.max()
z= df[["Age"]].fillna(df[["Age"]].mean())
age=((z-x_min)/(x_max-x_min))
df["age"]=age
d=pd.concat([df,sex],axis=1)
x=d[["age","female","male","Pclass"]]
y= d[['Survived']]

model=LinearRegression()
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
model.fit(x_train,y_train)

model_predited=model.predict(x_test)
model_predited

data = {'features': [[31, 0, 1, 2 ]]}

filename = 'Titanic_prediction.pkl'
pickle.dump(model, open(filename, 'wb'))

le_model=pickle.load(open('filename','rb'))
print(model.predict([[0,5]]))




# url = 'http://0.0.0.0:5000/api/'

# data = data = {
#     'features': [31, 0, 2 ]
# }
# j_data = json.dumps(data)
# headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
# r = requests.post(url, data=j_data, headers=headers)
# print(r, r.text)


# def load_model():
#     pass
    


# def predict(data):
#     pass
