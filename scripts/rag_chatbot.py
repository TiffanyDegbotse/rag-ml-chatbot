
import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from together import Together  # import the Together client

TOGETHER_API_KEY = "0966418881d440d3a1bfc8b32f078e73e16439c8d260c917b9ae3f8b6d05d282"
GPT_MODEL = "meta-llama/Llama-3-70b-chat-hf"  # example model from Together

class RAGChatbot:
    def __init__(self, index_path='faiss_index.index', meta_path='meta.pkl'):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = faiss.read_index(index_path)
        with open(meta_path, 'rb') as f:
            data = pickle.load(f)
            self.texts = data['texts']
            self.metadata = data['metadata']
        self.client = Together(api_key=TOGETHER_API_KEY)  # instantiate Together client

    def retrieve(self, query, top_k=5):
        query_vec = self.model.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(query_vec, top_k)
        results = []
        for i in indices[0]:
            results.append(self.texts[i])
        return results

    def generate_answer(self, query, retrieved_chunks):
        context = "\n\n".join(retrieved_chunks)
        prompt = f"Use the following context to answer the question:\n{context}\n\nQuestion: {query}\nAnswer:"

        try:
            response = self.client.chat.completions.create(
                model=GPT_MODEL,
                messages=[
                    {"role": "system", "content": "You are an AI assistant knowledgeable about AI and Machine Learning."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error generating answer: {e}"

    def chat(self, query):
        chunks = self.retrieve(query)
        answer = self.generate_answer(query, chunks)
        return answer

if __name__ == "__main__":
    chatbot = RAGChatbot()
    print("Ask me anything about AI/ML:")
    while True:
        user_input = input(">> ")
        if user_input.lower() in ['exit', 'quit']:
            break
        response = chatbot.chat(user_input)
        print(f"\n{response}\n")
