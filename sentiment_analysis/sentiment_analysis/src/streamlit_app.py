import streamlit as st
import tensorflow as tf
from transformers import BertTokenizer
import numpy as np

mdl = tf.keras.models.load_model('sentiment_model.h5')
tok = BertTokenizer.from_pretrained('bert-base-uncased')

def preprocess_text(txt):
    toks = tok(txt, padding='max_length', truncation=True, return_tensors='np')
    return toks['input_ids']

def main():
    st.title('Sentiment Analysis Dashboard')
    txt = st.text_area("Enter a movie review:")
    if st.button("Predict"):
        pt = preprocess_text(txt)
        pred = mdl.predict(np.expand_dims(pt, axis=0))
        st.write("Prediction:", "Positive" if pred[0][0] > 0.5 else "Negative")

if __name__ == '__main__':
    main()
