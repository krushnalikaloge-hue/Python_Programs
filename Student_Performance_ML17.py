# Use the trained model to predict result for a student with:
#    StudyHours = 6           Attendance = 85    
#    PreviousScore = 66       AssignmentsCompleted  = 7       
#    SleepHours = 7
# Will the student Pass or Fail?  

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
# Step 4: Build the model
##################################################################################

print(Border)
print("Step 4: Build the model")
print(Border)

model = DecisionTreeClassifier()

print("Model gets created Successfully")

##################################################################################
# Step 5: Train the model
##################################################################################

print(Border)
print("Step 5: Train the model")
print(Border)

model.fit(X_train,Y_train)

print("Model Trained Successfully")

student = pd.DataFrame([{
    "StudyHours": 6,
    "Attendance": 85,
    "PreviousScore": 66,
    "AssignmentsCompleted": 7,
    "SleepHours": 7
}])

Result = model.predict(student) [0]

print("Predicted Result:",Result)







 








