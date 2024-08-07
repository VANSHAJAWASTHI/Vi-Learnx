import tensorflow as tf
from sklearn.metrics import classification_report, accuracy_score
import numpy as np

def evaluate_model(mdl_path, te):
    mdl = tf.keras.models.load_model(mdl_path)

    y_true = []
    y_pred = []

    for batch in te:
        X, y = batch
        preds = mdl.predict(X)
        y_true.extend(y.numpy())
        y_pred.extend((preds > 0.5).astype(int))

    acc = accuracy_score(y_true, y_pred)
    rpt = classification_report(y_true, y_pred, target_names=['Neg', 'Pos'])
    return acc, rpt
