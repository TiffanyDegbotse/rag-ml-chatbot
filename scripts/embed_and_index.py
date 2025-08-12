
import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle

def embed_and_index(processed_dir='data/processed', index_path='faiss_index.index', meta_path='meta.pkl'):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    texts = []
    metadata = []
    for filename in os.listdir(processed_dir):
        if filename.endswith('.txt'):
            filepath = os.path.join(processed_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                chunks = f.read().split('\n\n')
                for i, chunk in enumerate(chunks):
                    if chunk.strip():
                        texts.append(chunk.strip())
                        metadata.append({'source_file': filename, 'chunk_id': i})
    print(f"Embedding {len(texts)} text chunks...")
    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    print(f"FAISS index has {index.ntotal} vectors.")
    faiss.write_index(index, index_path)
    with open(meta_path, 'wb') as f:
        pickle.dump({'texts': texts, 'metadata': metadata}, f)
    print(f"Saved FAISS index to {index_path} and metadata to {meta_path}")

if __name__ == "__main__":
    embed_and_index()
