# Design machine Learning application which follows below steps as:
# 1.Get Data  2. Clean, Prepare, and Manipulate data  3.Train Data  4.Test Data  5.Calculate accuracy

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

border = "-"*30
#######################################################################
# Step 1: Get the data
#######################################################################

print(border)
print("Step 1: Get the Data")
print(border)

DataPath = "WinePredictor.csv"
df = pd.read_csv(DataPath)

print("Dataset loaded successfully")
print(df.head())

#########################################################################
# Step 2: Clean, Prepare and manipulate the data
#########################################################################

print(border)
print("Step 2: Clean, Prepare and manipulate the data")
print(border)

df.dropna(inplace=True)

print("Shape of dataset: ",df.shape)

print("Total records: ",df.shape[0])
print("Total column: ",df.shape[1])

print(border)

# Decide the dependent and independent variables
# X = Independent Variable / Features
# Y = Dependent Variable / Labels

feature_cols = [
    "Alcohol",
    "Malic acid",
    "Ash",
    "Alcalinity of ash",
    "Magnesium",
    "Total phenols",
    "Flavanoids",
    "Nonflavanoid phenols",
    "Proanthocyanins",
    "Color intensity",
    "Hue",
    "OD280/OD315 of diluted wines",
    "Proline"
]

X = df[feature_cols]
Y = df["Class"]

print("X shape :", X.shape)
print("Y shape :", Y.shape)

############################################################################
# Step 3: Split the dataset for training and testing
############################################################################

print(border)
print("Step 3: Split the dataset for training and testing")
print(border)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print("Dataset splitting activity done")

print("X_train shape :", X_train.shape)
print("X_test shape  :", X_test.shape)
print("Y_train shape :", Y_train.shape)
print("Y_test shape  :", Y_test.shape)

############################################################################
# Step 4: Train the model
############################################################################

print(border)
print("Step 4: Train the model")
print(border)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)

print("Model training activity done")

############################################################################
# Step 5: Test the model
############################################################################

print(border)
print("Step 5: Test the model")
print(border)

Y_pred = model.predict(X_test)

print("Model testing activity done")

print("Predicted values:")
print(Y_pred)

############################################################################
# Step 6: Calculate accuracy
############################################################################

print(border)
print("Step 6: Calculate Accuracy")
print(border)

accuracy = accuracy_score(Y_test, Y_pred)

print("Accuracy :", accuracy)
print("Accuracy in percentage :", accuracy * 100, "%")