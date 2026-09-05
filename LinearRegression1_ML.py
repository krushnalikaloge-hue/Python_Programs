# Write a python program using LinearRegression to train a regression model using the dataset below:
#        Study Hours         Marks
#            1                 50
#            2                 55
#            3                 60 
#            4                 65
#            5                 70

# Task-> 1. Train the model   2.Print the Coefficient    3.Print the intercept

from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]
Y = [50, 55, 60, 65, 70]

model = LinearRegression()

# Train the regression model
model.fit(X, Y)

# Print the coefficient
print("Coefficient:", model.coef_[0])

# Print the intercept
print("Intercept:", model.intercept_)

