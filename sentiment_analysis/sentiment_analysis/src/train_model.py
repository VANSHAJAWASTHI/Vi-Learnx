import tensorflow as tf
from transformers import TFBertForSequenceClassification

def create_and_train_model(tr, tok):
    mdl = TFBertForSequenceClassification.from_pretrained('bert-base-uncased')
    mdl.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=2e-5), loss='binary_crossentropy', metrics=['accuracy'])
    mdl.fit(tr, epochs=3)
    mdl.save('sentiment_model.h5')
    return mdl
