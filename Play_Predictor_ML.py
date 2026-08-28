# Design machine Learning application which uses classification technique.
# 1.Get Data  2. Clean, Prepare, and Manipulate data  3.Train Data  4.Test Data  5.Calculate accuracy

import pandas as pd
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

border = "-" * 30

#--------------------------------------------------------------------------------------------
# Step 1: Get Data
#--------------------------------------------------------------------------------------------
print(border)
print("Step 1: Get Data")
print(border)

df = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")
print("Dataset loaded successfully")
print(df.head())

#---------------------------------------------------------------------------------------------
# Step 2: Clean, Prepare and Manipulate Data
#---------------------------------------------------------------------------------------------
print(border)
print("Step 2: Clean, Prepare and Manipulate Data")
print(border)

le = preprocessing.LabelEncoder()

df["Wether"] = le.fit_transform(df["Wether"])
df["Temperature"] = le.fit_transform(df["Temperature"])
df["Play"] = le.fit_transform(df["Play"])

feature_cols = ["Wether", "Temperature"]
X = df[feature_cols]
Y = df["Play"]

print("X shape :", X.shape)
print("Y shape :", Y.shape)

#----------------------------------------------------------------------------------------------
# Step 3: Train Data
#-----------------------------------------------------------------------------------------------
print(border)
print("Step 3: Train Data")
print(border)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, Y)
print("Model training activity done")

#---------------------------------------------------------------------------------------------
# Step 4: Test Data
#---------------------------------------------------------------------------------------------
print(border)
print("Step 4: Test Data")
print(border)

test_data = pd.DataFrame([[0, 2]], columns=feature_cols)
predicted = model.predict(test_data)

if predicted[0] == 1:
    print("Play : Yes")
else:
    print("Play : No")

#----------------------------------------------------------------------------------------------
# Step 5: Calculate Accuracy
#------------------------------------------------------------------------------------------------
print(border)
print("Step 5: Calculate Accuracy")
print(border)


def CheckAccuracy():
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)

    for k in range(1, 6):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, Y_train)
        y_pred = knn.predict(X_test)
        acc = accuracy_score(Y_test, y_pred)
        print("K =", k, "| Accuracy :", acc * 100, "%")


CheckAccuracy()