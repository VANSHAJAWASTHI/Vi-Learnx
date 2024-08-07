import tensorflow as tf
from transformers import BertTokenizer
import numpy as np

def preprocess_data():
    (tr, te), _ = tfds.load('imdb_reviews', split=['train', 'test'], with_info=True, as_supervised=True)

    tok = BertTokenizer.from_pretrained('bert-base-uncased')

    def preprocess_text(txt, lbl):
        txt = tf.strings.lower(txt)
        txt = tf.strings.regex_replace(txt, '[^a-zA-Z\s]', '')
        toks = tok(txt.numpy().decode('utf-8'), padding='max_length', truncation=True, return_tensors='np')
        return toks['input_ids'][0], lbl

    tr = tr.map(lambda txt, lbl: tf.py_function(func=preprocess_text, inp=[txt, lbl], Tout=(tf.int32, tf.int64)))
    te = te.map(lambda txt, lbl: tf.py_function(func=preprocess_text, inp=[txt, lbl], Tout=(tf.int32, tf.int64)))

    tr = tr.batch(32).prefetch(tf.data.AUTOTUNE)
    te = te.batch(32).prefetch(tf.data.AUTOTUNE)
    
    return tr, te, tok
