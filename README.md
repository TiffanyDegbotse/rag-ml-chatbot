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
```bash
git clone https://github.com/TiffanyDegbotse/rag-ml-chatbot.git
cd rag-ml-chatbot
