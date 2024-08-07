import pickle
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score
from src.preprocess import load, preprocess
import logging

logging.basicConfig(level=logging.INFO)

def evaluate():
    try:
        logging.info("Evaluating...")
        with open('model.pkl', 'rb') as f:
            model, preprocessor = pickle.load(f)
        X, y = load()
        X_prep, _ = preprocess(X)
        scores = cross_val_score(model, X_prep, y, cv=5, scoring='neg_mean_squared_error')
        logging.info(f'Cross-Validated MSE: {-scores.mean()}')
        y_pred = model.predict(X_prep)
        mse = mean_squared_error(y, y_pred)
        r2 = r2_score(y, y_pred)
        logging.info(f'MSE: {mse}')
        logging.info(f'R2: {r2}')
    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    evaluate()
