from flask import Flask, render_template, request
from tv_data import SmartTV
from optimizer import TVOptimizer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input from the user
    usage_hours = float(request.form['usage_hours'])
    
    # Create a SmartTV instance
    tv = SmartTV()
    optimizer = TVOptimizer()

    # Simulate and collect data for training
    tv.simulate_daily_usage()

    # Get historical data
    history = tv.get_history()

    # Train the model using the collected data
    optimizer.train_model(history)

    # Predict the energy cost based on the input usage
    predicted_cost = optimizer.predict_cost(usage_hours)

    return render_template('index.html', predicted_cost=predicted_cost)

if __name__ == '__main__':
    app.run(debug=True)
