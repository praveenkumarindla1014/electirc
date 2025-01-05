import pandas as pd
import random

class SmartTV:
    def __init__(self, power_rate=0.15):
        """
        Initialize the SmartTV object.
        :param power_rate: Power consumption rate in kWh per hour.
        """
        self.power_rate = power_rate
        self.history = pd.DataFrame(columns=["Date", "Usage Hours", "Power Consumed (kWh)", "Cost (₹)"])

    def simulate_daily_usage(self, usage_hours=None):
        """
        Simulate TV usage for a day based on input usage hours.
        :param usage_hours: Number of hours the TV was used.
        :return: Dictionary containing daily data (usage hours, power consumed, and cost).
        """
        if usage_hours is None:
            usage_hours = random.uniform(2, 5)  # Default random usage hours between 2 and 5 hours

        power_consumed = usage_hours * self.power_rate  # kWh
        cost = power_consumed * 10  # Assuming 10 ₹ per kWh for simplicity

        # Store the data in a DataFrame
        new_data = pd.DataFrame({
            "Date": [pd.to_datetime("today").strftime("%Y-%m-%d")],
            "Usage Hours": [round(usage_hours, 2)],
            "Power Consumed (kWh)": [round(power_consumed, 2)],
            "Cost (₹)": [round(cost, 2)]
        })

        # Concatenate the new data with the historical data
        self.history = pd.concat([self.history, new_data], ignore_index=True)

        return new_data.iloc[0].to_dict()  # Return the new data as a dictionary

    def get_history(self):
        """
        Return the historical energy consumption data.
        :return: DataFrame containing all historical data.
        """
        return self.history
