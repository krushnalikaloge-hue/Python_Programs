#Identify student where: y_test ! = y_pred
#    Display those rows.
#    How many students were misclassified?
#    what common pattern doyou observe?

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

print("X_train: ",X_train.shape)
print("X_test: ",X_test.shape)

print("Y_train: ",Y_train.shape)
print("Y_test: ",Y_test.shape)

##################################################################################
# Step 4: Build the model
##################################################################################

print(Border)
print("Step 4: Build the model")
print(Border)

model = DecisionTreeClassifier()

print("Model gets created Successfully")

##################################################################################
# Step 5: Train and Test the model
##################################################################################

print(Border)
print("Step 5: Train and Test the model")
print(Border)

model.fit(X_train,Y_train)

print("Model Trained Successfully")

Y_pred = model.predict(X_test)
print("Predicted answers are: ",Y_pred.tolist())

print("Expected answer are: ",Y_test.tolist())

##################################################################################
# Step 6: Find Misclassified students
##################################################################################

print(Border)
print("Step 6: Find Misclassified students")
print(Border)

Y_pred = model.predict(X_test)

misclassified = Y_test != Y_pred

print("Misclassified students: ")
print(X_test[misclassified])

print("Number of misclassified students: ",misclassified.sum())

# No clear common pattern can be oberserved beacause only one student was misclassified. 





