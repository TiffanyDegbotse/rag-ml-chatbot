# AI/ML Document Chatbot (RAG + VectorDB)

A domain-specific **Question & Answer chatbot** for AI and Machine Learning documents, powered by **Retrieval-Augmented Generation (RAG)** using a vector database and the Together API for language generation.

---

## Project Overview

This project builds a Q&A chatbot that can answer questions based on a specialized AI/ML knowledge base. It uses:

- Wikipedia AI/ML articles as the knowledge source  
- Text preprocessing and chunking to prepare data  
- Sentence Transformer embeddings stored in a FAISS vector index  
- A retrieval module to find relevant text chunks  
- The Together API (with Llama-based models) to generate natural language answers using retrieved context  

---

## Features

- Downloads and preprocesses domain-specific Wikipedia data  
- Embeds documents and builds a vector index with FAISS  
- Retrieves relevant text chunks for user queries  
- Generates human-like answers with retrieval context via Together API  
- Command line chatbot interface  

---

## Getting Started

### Prerequisites

- Python 3.8+  
- Git  
- Google Colab or local environment  
- Together API key (get one from [Together.xyz](https://together.xyz))  

### Installation

1. Clone the repository  
   `git clone https://github.com/TiffanyDegbotse/rag-ml-chatbot.git`  
   `cd rag-ml-chatbot`

2. Install dependencies  
   `pip install -r requirements.txt`

3. Set your Together API key (recommended)  
   `export TOGETHER_API_KEY="your_api_key_here"`

---

## Usage

### 1. Data extraction and preprocessing  
Run the notebook `notebooks/data_extraction.ipynb` or corresponding scripts to download and preprocess AI/ML Wikipedia articles.

### 2. Generate embeddings and index  
`python scripts/embed_and_index.py`

### 3. Run the chatbot  
`python scripts/rag_chatbot.py`

Type your AI/ML questions and get context-aware answers!

---

## Project Structure

ai-ml-document-chatbot/
│
├── data/
│ ├── raw/ # Raw downloaded Wikipedia articles
│ └── processed/ # Cleaned and chunked documents
│
├── notebooks/
│ └── data_extraction.ipynb # Data extraction and preprocessing notebook
│
├── scripts/
│ ├── download_wiki.py # Script to download Wikipedia AI/ML articles
│ ├── preprocess.py # Text cleaning and chunking functions
│ ├── embed_and_index.py # Embedding and FAISS index creation
│ └── rag_chatbot.py # RAG chatbot code integrating Together API
│
├── requirements.txt # Python dependencies
├── README.md # This file
└── .gitignore



---

## Notes

- The chatbot uses the **Together API** for natural language generation, which requires an API key and may incur costs depending on usage.  - This project is a great starting point for building domain-specific chatbots on niche datasets.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
