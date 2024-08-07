import pickle
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
from src.preprocess import load, preprocess
import logging

logging.basicConfig(level=logging.INFO)

def train():
    logging.info("Training...")
    try:
        X, y = load()
        X_prep, preprocessor = preprocess(X)
        model = Ridge()
        params = {'alpha': [0.1, 1.0, 10.0]}
        gs = GridSearchCV(model, params, cv=5)
        gs.fit(X_prep, y)
        best_model = gs.best_estimator_
        with open('model.pkl', 'wb') as f:
            pickle.dump((best_model, preprocessor), f)
        logging.info("Model saved.")
    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    train()
