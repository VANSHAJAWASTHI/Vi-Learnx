from flask import Flask, request, jsonify
import tensorflow as tf
from transformers import BertTokenizer
import numpy as np

app = Flask(__name__)

mdl = tf.keras.models.load_model('sentiment_model.h5')
tok = BertTokenizer.from_pretrained('bert-base-uncased')

def preprocess_text(txt):
    toks = tok(txt, padding='max_length', truncation=True, return_tensors='np')
    return toks['input_ids']

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    txt = data['text']
    pt = preprocess_text(txt)
    pred = mdl.predict(np.expand_dims(pt, axis=0))
    return jsonify({'prediction': int(pred[0][0] > 0.5)})

if __name__ == '__main__':
    app.run(debug=True)
