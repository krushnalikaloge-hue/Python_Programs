# Using the regression model created in the previous question, write a python program to predict marks for 6 study &
# display the predicted value.

from sklearn.linear_model import LinearRegression

X = [[1],[2],[3],[4],[5]]
Y = [50,55,60,65,70]

model = LinearRegression()

# Train the model
model.fit(X,Y)

# Predict marks for 6 study hours
marks = model.predict([[6]])

# Display predicted marks
print("Predicted marks for 6 study hours: ",marks[0])