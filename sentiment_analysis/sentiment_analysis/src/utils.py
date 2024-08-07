import tensorflow as tfds

def load_dataset():
    return tfds.load('imdb_reviews', split=['train', 'test'], with_info=True, as_supervised=True)
