# app/app.py
from flask import Flask, request, jsonify
import pickle
import numpy as np
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

try:
    with open('../model.pkl', 'rb') as f:
        model, preprocessor = pickle.load(f)
except Exception as e:
    raise RuntimeError(f"Error loading model: {e}")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        feats = np.array(data['features']).reshape(1, -1)
        X_prep = preprocessor.transform(feats)
        pred = model.predict(X_prep)
        return jsonify(prediction=pred.tolist())
    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify(error=f"Invalid input: {e}"), 400

if __name__ == '__main__':
    app.run(debug=True)
