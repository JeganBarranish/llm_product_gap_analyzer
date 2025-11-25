# embeddings.py
# Utilities for creating embeddings and storing/retrieving them from a vector DB (Chroma / FAISS).
# This is a template. You can swap in OpenAI embeddings or sentence-transformers.

from sentence_transformers import SentenceTransformer
import numpy as np

class Embedder:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def embed_texts(self, texts):
        return self.model.encode(texts, show_progress_bar=False)

if __name__ == '__main__':
    e = Embedder()
    samples = ['6.4-inch OLED display', '48MP camera', '4000mAh battery']
    vecs = e.embed_texts(samples)
    print('Example embedding shape:', vecs.shape)
