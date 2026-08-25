# Train model using:
#     random_state =0
#     random_state = 10
#     random_state = 42
# compare testin accuracy.Does the result change ?

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

Border = "-"*30

##################################################################################
# Step 1: Load the dataset
##################################################################################

print(Border)
print("Step 1 : Load the Dataset")
print(Border)

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

##################################################################################
# Step 2: Decide the dependant and Independant variable
##################################################################################

print(Border)
print("Step 2: Decide the dependant and Independant Varibles")
print(Border)

# X : Independant Variable / Features
# Y : Dependant Variable / Labels

feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_cols]
Y = df["FinalResult"]

print("X Shape: ",X.shape)
print("Y Shape: ",Y.shape)

##################################################################################
# Step 3: Split the dataset for training and testing-model1
##################################################################################

print(Border)
print("Step 3: Split the dataset for training and testing-model1")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

print("Dataset splitting Activity done")

print("X_train: ",X_train.shape)
print("X_test: ",X_test.shape)

print("Y_train: ",Y_train.shape)
print("Y_test: ",Y_test.shape)

model1 = DecisionTreeClassifier()

print("Model gets created Successfully")

##################################################################################
# Step 4: Train and Test the model1
##################################################################################

print(Border)
print("Step 4: Train and Test the model1")
print(Border)

model1.fit(X_train,Y_train)

print("Model Trained Successfully")

Y_pred = model1.predict(X_test)

Model_accuracy_0 = accuracy_score(Y_test,Y_pred)
print("Model Accuracy_0: ",Model_accuracy_0*100,"%")

##################################################################################
# Step 5: Split the dataset for training and testing-model2
##################################################################################

print(Border)
print("Step 5: Split the dataset for training and testing-model2")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

print("Dataset splitting Activity done")

print("X_train: ",X_train.shape)
print("X_test: ",X_test.shape)

print("Y_train: ",Y_train.shape)
print("Y_test: ",Y_test.shape)

model2 = DecisionTreeClassifier()

print("Model gets created Successfully")

##################################################################################
# Step 6: Train and Test the model2
##################################################################################

print(Border)
print("Step 6: Train and Test the model2")
print(Border)

model2.fit(X_train,Y_train)

print("Model Trained Successfully")

Y_pred = model2.predict(X_test)

Model_accuracy_10 = accuracy_score(Y_test,Y_pred)
print("Model Accuracy_10: ",Model_accuracy_10*100,"%")

##################################################################################
# Step 7: Split the dataset for training and testing-model3
##################################################################################

print(Border)
print("Step 7: Split the dataset for training and testing-model3")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

print("Dataset splitting Activity done")

print("X_train: ",X_train.shape)
print("X_test: ",X_test.shape)

print("Y_train: ",Y_train.shape)
print("Y_test: ",Y_test.shape)

model3 = DecisionTreeClassifier()

print("Model gets created Successfully")

##################################################################################
# Step 8: Train and Test the model3
##################################################################################

print(Border)
print("Step 8: Train and Test the model3")
print(Border)

model3.fit(X_train,Y_train)

print("Model Trained Successfully")

Y_pred = model3.predict(X_test)

Model_accuracy_42 = accuracy_score(Y_test,Y_pred)
print("Model Accuracy_42: ",Model_accuracy_42*100,"%")

##################################################################################
# Step 9: Compare 3 Accuracies
##################################################################################

print(Border)
print("Step 9: Compare 3 Accuracies")
print(Border)

print("Model Accuracy_0: ",Model_accuracy_0*100,"%")
print("Model Accuracy_10: ",Model_accuracy_10*100,"%")
print("Model Accuracy_42: ",Model_accuracy_42*100,"%")



