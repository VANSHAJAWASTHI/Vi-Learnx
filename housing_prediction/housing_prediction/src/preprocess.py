import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

def load():
    from sklearn.datasets import fetch_california_housing
    data = fetch_california_housing()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = data.target
    return X, y

def feature_eng(X):
    X['rph'] = X['total_rooms'] / X['households']
    X['bpr'] = X['total_bedrooms'] / X['total_rooms']
    return X

def preprocess(X):
    X = feature_eng(X)
    num_feats = X.columns.tolist()
    num_transformer = Pipeline(steps=[
        ('imp', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', num_transformer, num_feats)
        ])
    X_prep = preprocessor.fit_transform(X)
    return X_prep, preprocessor

if __name__ == "__main__":
    X, y = load()
    X_prep, preprocessor = preprocess(X)
    print("Preprocessing complete. Sample data:")
    print(X_prep[:5])
