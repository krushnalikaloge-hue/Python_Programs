# Design machine learning application which follows below steps as:
# 1. Get Data  2. Clean, Prepare and Manipulate data
# 3. Train Data  4. Test Data  5. Display Predicted and Expected Values


import pandas as pd
from sklearn.linear_model import LinearRegression

border = "-" * 80

############################################################
# Step 1: Get the data
############################################################

print(border)
print("Step 1: Get the Data")
print(border)

DataPath = "Advertising.csv"

df = pd.read_csv(DataPath)

print("Dataset loaded successfully")
print(df.head())

############################################################
# Step 2: Clean, Prepare and Manipulate the data
############################################################

print(border)
print("Step 2: Clean, Prepare and Manipulate the data")
print(border)

df.dropna(inplace=True)

print("Shape of dataset :", df.shape)

print("Total records :", df.shape[0])

print("Total column :", df.shape[1])

############################################################
# Decide the dependent and independent variables
############################################################

# X = Independent Variable / Features
# Y = Dependent Variable / Labels

feature_cols = [
    "TV",
    "radio",
    "newspaper"
]

X = df[feature_cols]

Y = df["sales"]

print("X shape :", X.shape)

print("Y shape :", Y.shape)

############################################################
# Step 3: Train the data
############################################################

print(border)
print("Step 3: Train the data")
print(border)

# Use first half of dataset for training

X_train = X.iloc[:len(X)//2]

Y_train = Y.iloc[:len(Y)//2]

model = LinearRegression()

model.fit(X_train, Y_train)

print("Model training activity done")

############################################################
# Step 4: Test the data
############################################################

print(border)
print("Step 4: Test the data")
print(border)

# Use remaining half of dataset for testing

X_test = X.iloc[len(X)//2:]

Y_test = Y.iloc[len(Y)//2:]


Y_pred = model.predict(X_test)


print("Model testing activity done")

############################################################
# Step 5: Display predicted and expected values
############################################################

print(border)
print("Step 5: Display Predicted and Expected Values")
print(border)

print("Predicted values:")

print(Y_pred)

print("Expected values:")

print(Y_test.values)