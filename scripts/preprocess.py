
import os
import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text

def chunk_text(text, max_chars=1000, overlap=200):
    chunks = []
    start = 0
    text_length = len(text)
    while start < text_length:
        end = min(start + max_chars, text_length)
        chunk = text[start:end]
        chunks.append(chunk)
        start += max_chars - overlap
    return chunks

def preprocess_and_chunk(raw_dir='data/raw', processed_dir='data/processed'):
    os.makedirs(processed_dir, exist_ok=True)
    for filename in os.listdir(raw_dir):
        if filename.endswith('.txt'):
            filepath = os.path.join(raw_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()
            cleaned = clean_text(text)
            chunks = chunk_text(cleaned)
            processed_path = os.path.join(processed_dir, filename)
            with open(processed_path, 'w', encoding='utf-8') as f:
                for chunk in chunks:
                    f.write(chunk + "\n\n")
            print(f"Processed and chunked: {filename}")

if __name__ == "__main__":
    preprocess_and_chunk()
