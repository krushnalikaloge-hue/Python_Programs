# Decision Tree Visulaization
# Use: from sklearn.tree import plot_tree
# Visualize the trained decicsion tree.
#      Which feature appears at the root node?
#      Why do you think that feature was selected first?

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

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

##################################################################################
# Step 6: Plot Tree
##################################################################################

print(Border)
print("Step 6: Plot Tree")
print(Border)

plt.figure(figsize=(6,7))

plot_tree(model,filled=True,feature_names=feature_cols,class_names=True)

plt.title("Student Performance Decision Tree")

plt.show()

#1. PreviousScore is the feature appears at the root node
#2. It was selected first beacause it provide the best split for predicting FinalResult 
