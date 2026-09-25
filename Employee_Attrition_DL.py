# Design Deep Learning application which follows below steps as:
# 1. Get Data
# 2. Display shape, columns and first five records
# 3. Check missing values
# 4. Identify numerical and categorical features
# 5. Convert categorical features into numerical representation
# 6. Convert target Attrition into 0 and 1
# 7. Separate independent and dependent variables
# 8. Divide dataset into training and testing data
# 9. Apply feature scaling
# 10. Design MLP with at least two hidden layers
# 11. Train the network
# 12. Display number of iterations required for training
# 13. Calculate training accuracy
# 14. Calculate testing accuracy
# 15. Generate confusion matrix
# 16. Plot loss curve
# 17. Create PredictAttrition function
# 18. Test system using five new employee records
# 19. Explain overfitting or underfitting


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt


border = "-" * 60


############################################################
# Step 1: Get the Data
############################################################

print(border)
print("Step 1: Get the Data")
print(border)

DataPath = "Employee_Attrition.csv"

df = pd.read_csv(DataPath)

print("Dataset loaded successfully")
print(df.head())


############################################################
# Step 2: Display shape, columns and first five records
############################################################

print(border)
print("Step 2: Display dataset information")
print(border)

print("Shape of dataset:", df.shape)

print("Columns:")
print(df.columns)

print("First five records:")
print(df.head())


############################################################
# Step 3: Check for missing values
############################################################

print(border)
print("Step 3: Check for missing values")
print(border)

print("Missing values:")
print(df.isnull().sum())


############################################################
# Step 4: Identify numerical and categorical features
############################################################

print(border)
print("Step 4: Identify numerical and categorical features")
print(border)

numerical_features = [
    "Age",
    "MonthlyIncome",
    "YearsAtCompany",
    "TotalWorkingYears",
    "DistanceFromHome",
    "JobSatisfaction",
    "WorkLifeBalance",
    "NumCompaniesWorked",
    "TrainingTimesLastYear"
]

categorical_features = [
    "OverTime"
]

print("Numerical features:")
print(numerical_features)

print("Categorical features:")
print(categorical_features)


############################################################
# Step 5: Convert categorical features into numerical
############################################################

print(border)
print("Step 5: Convert categorical features into numerical")
print(border)

df["OverTime"] = df["OverTime"].map({
    "Yes": 1,
    "No": 0
})

print("Categorical conversion activity done")


############################################################
# Step 6: Convert target Attrition into 0 and 1
############################################################

print(border)
print("Step 6: Convert Attrition into 0 and 1")
print(border)

df["Attrition"] = df["Attrition"].map({
    "Yes": 1,
    "No": 0
})

print("Target conversion activity done")


############################################################
# Step 7: Separate independent and dependent variables
############################################################

print(border)
print("Step 7: Separate independent and dependent variables")
print(border)

feature_cols = [
    "Age",
    "MonthlyIncome",
    "YearsAtCompany",
    "TotalWorkingYears",
    "DistanceFromHome",
    "JobSatisfaction",
    "WorkLifeBalance",
    "OverTime",
    "NumCompaniesWorked",
    "TrainingTimesLastYear"
]

X = df[feature_cols]

Y = df["Attrition"]

print("X shape:", X.shape)
print("Y shape:", Y.shape)


############################################################
# Step 8: Divide dataset into training and testing data
############################################################

print(border)
print("Step 8: Divide dataset into training and testing data")
print(border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.20,
    random_state=42
)

print("Dataset splitting activity done")

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("Y_train shape:", Y_train.shape)
print("Y_test shape:", Y_test.shape)


############################################################
# Step 9: Apply feature scaling
############################################################

print(border)
print("Step 9: Apply feature scaling")
print(border)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

print("Feature scaling activity done")


############################################################
# Step 10: Design the MLP with two hidden layers
############################################################

print(border)
print("Step 10: Design the MLP model")
print(border)

model = MLPClassifier(
    hidden_layer_sizes=(10, 10),
    max_iter=2000,
    random_state=42
)

print("MLP model created successfully")


############################################################
# Step 11: Train the network
############################################################

print(border)
print("Step 11: Train the model")
print(border)

model.fit(X_train, Y_train)

print("Model training activity done")


############################################################
# Step 12: Display number of iterations required
############################################################

print(border)
print("Step 12: Number of iterations required for training")
print(border)

print("Number of iterations:", model.n_iter_)


############################################################
# Step 13: Calculate training accuracy
############################################################

print(border)
print("Step 13: Calculate training accuracy")
print(border)

Y_train_pred = model.predict(X_train)

training_accuracy = accuracy_score(Y_train, Y_train_pred)

print("Training Accuracy:", training_accuracy)

print("Training Accuracy in percentage:",
      training_accuracy * 100, "%")


############################################################
# Step 14: Calculate testing accuracy
############################################################

print(border)
print("Step 14: Calculate testing accuracy")
print(border)

Y_test_pred = model.predict(X_test)

testing_accuracy = accuracy_score(Y_test, Y_test_pred)

print("Testing Accuracy:", testing_accuracy)

print("Testing Accuracy in percentage:",
      testing_accuracy * 100, "%")


############################################################
# Step 15: Generate confusion matrix
############################################################

print(border)
print("Step 15: Generate confusion matrix")
print(border)

cm = confusion_matrix(Y_test, Y_test_pred)

print("Confusion Matrix:")
print(cm)


############################################################
# Step 16: Plot the loss curve
############################################################

print(border)
print("Step 16: Display loss curve")
print(border)

plt.plot(model.loss_curve_)

plt.title("MLP Training Loss Curve")
plt.xlabel("Iterations")
plt.ylabel("Loss")

plt.show()


############################################################
# Step 17: Create PredictAttrition function
############################################################

print(border)
print("Step 17: Create PredictAttrition function")
print(border)


def PredictAttrition(employee_data):

    employee_data = pd.DataFrame(
        [employee_data],
        columns=feature_cols
    )

    employee_data = scaler.transform(employee_data)

    prediction = model.predict(employee_data)

    if prediction[0] == 0:
        print("Prediction: Employee is likely to stay")
    else:
        print("Prediction: Employee is likely to leave")

    return prediction


############################################################
# Step 18: Test system using five new employee records
############################################################

print(border)
print("Step 18: Test system using five new employee records")
print(border)

employee1 = [
    25, 3000, 2, 5, 10, 3, 3, 1, 2, 3
]

employee2 = [
    35, 7000, 10, 15, 5, 4, 4, 0, 1, 2
]

employee3 = [
    28, 4000, 4, 7, 8, 2, 3, 1, 3, 3
]

employee4 = [
    42, 9000, 15, 20, 4, 4, 4, 0, 2, 2
]

employee5 = [
    30, 5000, 5, 8, 15, 3, 2, 1, 4, 4
]


print("Employee 1:")
PredictAttrition(employee1)

print()

print("Employee 2:")
PredictAttrition(employee2)

print()

print("Employee 3:")
PredictAttrition(employee3)

print()

print("Employee 4:")
PredictAttrition(employee4)

print()

print("Employee 5:")
PredictAttrition(employee5)


############################################################
# Step 19: Check Overfitting or Underfitting
############################################################

print(border)
print("Step 19: Check Overfitting or Underfitting")
print(border)

difference = training_accuracy - testing_accuracy

print("Training Accuracy:", training_accuracy * 100, "%")
print("Testing Accuracy:", testing_accuracy * 100, "%")

if difference > 0.10:
    print("Model may be suffering from overfitting")
elif training_accuracy < 0.70 and testing_accuracy < 0.70:
    print("Model may be suffering from underfitting")
else:
    print("Model is performing reasonably well")