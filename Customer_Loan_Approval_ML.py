# Design machine learning application which follows below steps as:
# 1. Get Data  2. Clean, Prepare and Manipulate Data
# 3. Train Data  4. Test Data  5. Calculate Accuracy
# 6. Hard Voting  7. Soft Voting

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score


border = "-"*30

############################################################
# Step 1: Get the data
############################################################

print(border)
print("Step 1: Get the Data")
print(border)

DataPath = "Loan_Default.csv"

df = pd.read_csv(DataPath)

print("Dataset loaded successfully")
print(df.head())


############################################################
# Step 2: Clean, Prepare and Manipulate the data
############################################################

print(border)
print("Step 2: Clean, Prepare and Manipulate the data")
print(border)

print("Missing values:")
print(df.isnull().sum())

df.dropna(inplace=True)

print("Shape of dataset: ", df.shape)

print("Total records: ", df.shape[0])
print("Total columns: ", df.shape[1])


# Decide the dependent and independent variables
# X = Independent Variables / Features
# Y = Dependent Variable / Label

feature_cols = [
    "Age",
    "Income",
    "LoanAmount",
    "CreditScore",
    "EmploymentYears",
    "ExistingLoans",
    "MonthlyDebt",
    "LoanTerm",
    "PreviousDefault",
    "HomeOwnership"
]

X = df[feature_cols]

Y = df["Default"]

print("X shape: ", X.shape)
print("Y shape: ", Y.shape)


# Convert categorical column into numerical value

X = pd.get_dummies(X, drop_first=True)

print("Categorical data converted successfully")

# Scale the data

scaler = StandardScaler()

X = scaler.fit_transform(X)

print("Data scaling activity done")


############################################################
# Step 3: Split the dataset for training and testing
############################################################

print(border)
print("Step 3: Split the dataset for training and testing")
print(border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

print("Dataset splitting activity done")

print("X_train shape : ", X_train.shape)
print("X_test shape : ", X_test.shape)
print("Y_train shape : ", Y_train.shape)
print("Y_test shape : ", Y_test.shape)


############################################################
# Step 4: Train the models
############################################################

print(border)
print("Step 4: Train the models")
print(border)


# Logistic Regression

model_lr = LogisticRegression()

model_lr.fit(X_train, Y_train)

print("Logistic Regression training activity done")


# Decision Tree

model_dt = DecisionTreeClassifier(random_state=42)

model_dt.fit(X_train, Y_train)

print("Decision Tree training activity done")


# KNN

model_knn = KNeighborsClassifier()

model_knn.fit(X_train, Y_train)

print("KNN training activity done")


############################################################
# Step 5: Test the models
############################################################

print(border)
print("Step 5: Test the models")
print(border)

Y_pred_lr = model_lr.predict(X_test)

Y_pred_dt = model_dt.predict(X_test)

Y_pred_knn = model_knn.predict(X_test)

print("Model testing activity done")


############################################################
# Step 6: Calculate individual accuracy
############################################################

print(border)
print("Step 6: Calculate Individual Accuracy")
print(border)

accuracy_lr = accuracy_score(Y_test, Y_pred_lr)

accuracy_dt = accuracy_score(Y_test, Y_pred_dt)

accuracy_knn = accuracy_score(Y_test, Y_pred_knn)

print("Logistic Regression Accuracy : ", accuracy_lr)

print("Decision Tree Accuracy : ", accuracy_dt)

print("KNN Accuracy : ", accuracy_knn)


############################################################
# Step 7: Create Hard Voting Classifier
############################################################

print(border)
print("Step 7: Create Hard Voting Classifier")
print(border)

hard_voting = VotingClassifier(
    estimators=[
        ("lr", model_lr),
        ("dt", model_dt),
        ("knn", model_knn)
    ],
    voting="hard"
)

hard_voting.fit(X_train, Y_train)

print("Hard Voting training activity done")

Y_pred_hard = hard_voting.predict(X_test)

accuracy_hard = accuracy_score(Y_test, Y_pred_hard)

print("Hard Voting Accuracy : ", accuracy_hard)


############################################################
# Step 8: Create Soft Voting Classifier
############################################################

print(border)
print("Step 8: Create Soft Voting Classifier")
print(border)

soft_voting = VotingClassifier(
    estimators=[
        ("lr", model_lr),
        ("dt", model_dt),
        ("knn", model_knn)
    ],
    voting="soft"
)

soft_voting.fit(X_train, Y_train)

print("Soft Voting training activity done")

Y_pred_soft = soft_voting.predict(X_test)

accuracy_soft = accuracy_score(Y_test, Y_pred_soft)

print("Soft Voting Accuracy : ", accuracy_soft)


############################################################
# Step 9: Compare the accuracy
############################################################

print(border)
print("Step 9: Compare the Accuracy")
print(border)

print("Logistic Regression : ", accuracy_lr * 100, "%")

print("Decision Tree : ", accuracy_dt * 100, "%")

print("KNN : ", accuracy_knn * 100, "%")

print("Hard Voting : ", accuracy_hard * 100, "%")

print("Soft Voting : ", accuracy_soft * 100, "%")