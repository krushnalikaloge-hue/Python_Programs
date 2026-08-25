#Train three Decision Tree models with:
#    max_depth = 1
#    max_depth = 3
#    max_depth = None
# Compare their testing accuracies and write your observations.

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
# Step 3: Split the dataset for training and testing
##################################################################################

print(Border)
print("Step 3: Split the dataset for training and testing")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

print("Dataset splitting Activity done")

print("X: ",X.shape)
print("Y: ",Y.shape)

print("X_train: ",X_train.shape)
print("X_test: ",X_test.shape)

print("Y_train: ",Y_train.shape)
print("Y_test: ",Y_test.shape)

##################################################################################
# Step 4: First model
##################################################################################

print(Border)
print("Step 4: first model")
print(Border)

model1 = DecisionTreeClassifier(max_depth=1)

print("First Model gets created Successfully")

model1.fit(X_train,Y_train)

print("First Model Trained Successfully")

Y_pred1 = model1.predict(X_test)
testing_Accuracy1 = accuracy_score(Y_test,Y_pred1)

print("Predicted answer are: ",Y_pred1)

print("Testing Accuracy: ",testing_Accuracy1 * 100,"%")

##################################################################################
# Step 5: Second model
##################################################################################

print(Border)
print("Step 5: Second model")
print(Border)

model2 = DecisionTreeClassifier(max_depth=3)

print("second Model gets created Successfully")

model2.fit(X_train,Y_train)

print("Second Model Trained Successfully")

Y_pred2 = model2.predict(X_test)

print("Predicted answer are: ",Y_pred2)
testing_Accuracy2 = accuracy_score(Y_test,Y_pred2)

print("Testing Accuracy: ",testing_Accuracy2 * 100,"%")

##################################################################################
# Step 6: Third the model
##################################################################################

print(Border)
print("Step 6: Third the model")
print(Border)

model3 = DecisionTreeClassifier(max_depth=None)

print("Third Model gets created Successfully")

model3.fit(X_train,Y_train)

print("Third Model Trained Successfully")

Y_pred3 = model3.predict(X_test)

print("Predicted answer are: ",Y_pred3)
testing_Accuracy3 = accuracy_score(Y_test,Y_pred3)

print("Testing Accuracy: ",testing_Accuracy3 * 100,"%")








 








