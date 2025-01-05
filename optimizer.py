import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

class TVOptimizer:
    def __init__(self, power_rate=0.15, cost_per_kwh=10):
        self.power_rate = power_rate
        self.cost_per_kwh = cost_per_kwh
        self.model = LinearRegression()

    def train_model(self, historical_data):
        """
        Train a Linear Regression model to predict energy usage.
        :param historical_data: DataFrame containing historical usage data.
        """
        # Check if the input DataFrame is empty
        if historical_data.empty:
            raise ValueError("Historical data is empty. Please provide valid data.")
        
        # Use 'Usage Hours' to predict 'Cost'
        X = historical_data[["Usage Hours"]]  # Features: Usage Hours
        y = historical_data["Cost (₹)"]  # Target: Cost (₹)

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the model
        self.model.fit(X_train, y_train)

        # Predict on the test set
        y_pred = self.model.predict(X_test)

        # Print the performance of the model
        mse = mean_squared_error(y_test, y_pred)
        print(f"Model Mean Squared Error: {mse}")

    def predict_cost(self, usage_hours):
        """
        Predict the cost based on usage hours using the trained model.
        :param usage_hours: Number of hours the TV will be used.
        :return: Predicted cost (₹).
        """
        # Predict the cost based on the usage hours input
        predicted_cost = self.model.predict([[usage_hours]])[0]
        return predicted_cost
