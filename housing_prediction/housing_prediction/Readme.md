# Housing Price Prediction

## Setup
1. Install dependencies:
pip install -r requirements.txt

## Usage
1. Train the model:
python src/train.py
2. Evaluate the model:
python src/evaluate.py
3. Start the Flask API:

## API
- **POST /predict**: Predict housing prices.
- **Request Body**: `{ "features": [value1, value2, ...] }`
- **Response**: `{ "prediction": [price] }`
