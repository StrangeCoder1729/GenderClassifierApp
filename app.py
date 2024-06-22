from flask import Flask, request, render_template
import numpy as np
import pickle
from DataPreProcessing import sc

app = Flask(__name__, static_folder='static')

# Load the model
model = pickle.load(open('RandomForest.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract form inputs
    long_hair = int(request.form['long_hair'])
    forehead_width_cm = float(request.form['forehead_width_cm'])
    forehead_height_cm = float(request.form['forehead_height_cm'])
    nose_wide = int(request.form['nose_wide'])
    nose_long = int(request.form['nose_long'])
    lips_thin = int(request.form['lips_thin'])
    distance_nose_to_lip_long = int(request.form['distance_nose_to_lip_long'])

    # Prepare input features for prediction
    input_features = np.array([[long_hair, forehead_width_cm, forehead_height_cm, nose_wide, nose_long, lips_thin, distance_nose_to_lip_long]])

    # Scale the input features
    input_features_scaled = sc.transform(input_features)

    # Perform prediction using the Random Forest model
    prediction = model.predict(input_features_scaled)[0]

    # Determine the result based on prediction
    result = 'Random Forest Model: Woman' if prediction == 1 else 'Random Forest Model: Man'

    return result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
