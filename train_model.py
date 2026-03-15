import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Sample training dataset
data = {
    "genre":[1,2,1,3,2,1,3,2],
    "budget":[100,200,150,300,250,120,350,270],
    "runtime":[90,120,110,150,130,95,160,140],
    "rating":[6.5,7.8,7.0,8.5,7.9,6.8,8.8,8.0]
}

df = pd.DataFrame(data)

X = df[['genre','budget','runtime']]
y = df['rating']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train,y_train)

joblib.dump(model,'movie_model.pkl')

print("Model trained successfully")