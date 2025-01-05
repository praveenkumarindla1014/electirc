from tv_data import SmartTV
from optimizer import TVOptimizer
import matplotlib.pyplot as plt

def main():
    print("Smart Home Energy Management System - TV Module")
    print("=" * 50)

    # Initialize TV and Optimizer
    tv = SmartTV()
    optimizer = TVOptimizer()

    # Simulate 30 days of TV usage data
    for _ in range(30):
        daily_data = tv.simulate_daily_usage()

    # Train the ML model with historical data
    optimizer.train_model(tv.get_history())

    # Get user input to predict future cost
    usage_hours = float(input("Enter the number of hours the TV will be used in the next day: "))
    predicted_cost = optimizer.predict_cost(usage_hours)

    print(f"Predicted Cost (₹) for {usage_hours} hours of TV usage: ₹{predicted_cost}")

    # Plot the energy usage over the 30 days
    history = tv.get_history()
    plot_energy_usage(history)

def plot_energy_usage(history):
    """
    Plot the energy usage history with Matplotlib.
    :param history: DataFrame containing historical energy usage data.
    """
    plt.figure(figsize=(10, 6))

    plt.plot(history["Date"], history["Cost (₹)"], label="Energy Cost (₹)", color='blue', marker='o')
    plt.xlabel('Date')
    plt.ylabel('Cost (₹)')
    plt.title('Energy Cost Over Time')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    main()
