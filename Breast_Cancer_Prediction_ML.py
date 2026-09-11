# Design machine learning application which follows below steps as:
# 1. Get Data  2. Clean, Prepare and Manipulate Data
# 3. Split Data  4. Train Model  5. Test Model  6. Calculate Accuracy

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

border = "*" * 70

##############################################################################
# Step 1: Get the data
##############################################################################

print(border)
print("Step 1: Get the Data")
print(border)

data = load_breast_cancer()

df = pd.DataFrame(data.data, columns=data.feature_names)

df["target"] = data.target

print("Dataset loaded successfully")
print(df.head())

##############################################################################
# Step 2: Clean, Prepare and Manipulate the data
##############################################################################

print(border)
print("Step 2: Clean, Prepare and Manipulate the data")
print(border)

# Check shape of dataset
print("Shape of dataset :", df.shape)

# Display total records and columns
print("Total records :", df.shape[0])
print("Total columns :", df.shape[1])

# Check missing values
print("Missing values :")
print(df.isnull().sum().sum())

# Handle missing values if any
df.fillna(df.median(numeric_only=True), inplace=True)

# Display summary statistics
print("Summary statistics :")
print(df.describe())


##############################################################################
# Decide the dependent and independent variables
##############################################################################

# X = Independent Variables / Features
# Y = Dependent Variable / Label

feature_cols = data.feature_names

X = df[feature_cols]
Y = df["target"]

print("X shape :", X.shape)
print("Y shape :", Y.shape)


##############################################################################
# Feature Scaling
##############################################################################

print(border)
print("Feature Scaling")
print(border)

scaler = StandardScaler()

X = scaler.fit_transform(X)

print("Feature scaling activity done")


##############################################################################
# Feature Correlation Visualization
##############################################################################

print(border)
print("Feature Correlation Visualization")
print(border)

correlation = df[feature_cols].corr()

plt.figure(figsize=(10, 8))
plt.imshow(correlation, cmap="coolwarm")
plt.colorbar()
plt.title("Feature Correlation")
plt.xlabel("Features")
plt.ylabel("Features")
plt.show()


##############################################################################
# Step 3: Split the dataset for training and testing
##############################################################################

print(border)
print("Step 3: Split the dataset for training and testing")
print(border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

print("Dataset splitting activity done")

print("X_train shape :", X_train.shape)
print("X_test shape :", X_test.shape)
print("Y_train shape :", Y_train.shape)
print("Y_test shape :", Y_test.shape)


##############################################################################
# Step 4: Train the model
##############################################################################

print(border)
print("Step 4: Train the model")
print(border)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)

print("Model training activity done")


##############################################################################
# Step 5: Test the model
##############################################################################

print(border)
print("Step 5: Test the model")
print(border)

Y_pred = model.predict(X_test)

print("Model testing activity done")

print("Predicted values :")
print(Y_pred)

print("Expected values :")
print(Y_test.values)


##############################################################################
# Step 6: Calculate Accuracy
##############################################################################

print(border)
print("Step 6: Calculate Accuracy")
print(border)

accuracy = accuracy_score(Y_test, Y_pred)

print("Accuracy :", accuracy)
print("Accuracy in percentage :", accuracy * 100, "%")


##############################################################################
# Confusion Matrix
##############################################################################

print(border)
print("Confusion Matrix")
print(border)

cm = confusion_matrix(Y_test, Y_pred)

print(cm)


##############################################################################
# Precision, Recall and F1-Score
##############################################################################

print(border)
print("Precision, Recall and F1-Score")
print(border)

print(classification_report(Y_test, Y_pred))