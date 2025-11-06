
# Import required libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Step 1: Create sample data
data = {
    'Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Scores': [10, 20, 30, 35, 45, 50, 65, 70, 85, 95]
}

# Step 2: Convert to DataFrame
df = pd.DataFrame(data)
print("Sample Data:\n", df)

# Step 3: Split into features (X) and labels (y)
X = df[['Hours']]
y = df['Scores']

# Step 4: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Predict scores for test data
y_pred = model.predict(X_test)

# Step 7: Display actual vs predicted
result = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("\nActual vs Predicted:\n", result)

# Step 8: Plot the regression line
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel("Study Hours")
plt.ylabel("Scores")
plt.title("Study Hours vs Student Scores")
plt.legend()
plt.show()

# Step 9: Test with new data
new_hours = [[7.5]]
predicted_score = model.predict(new_hours)
print(f"\nPredicted Score for 7.5 study hours: {predicted_score[0]:.2f}")
