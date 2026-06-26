# Medical Document Intelligence Assistant: RAG-Based AI System
## Project Objective

The objective of this project is to build an AI-powered Medical Document Intelligence Assistant that enables users to upload medical reports in PDF format and ask natural language questions about their reports. The system leverages Retrieval-Augmented Generation (RAG), semantic search, and Large Language Models (LLMs) to provide accurate, context-aware answers directly from the uploaded medical document.

## Project Description

This project is an interactive medical report analysis application built using Streamlit and LangChain. It allows users to upload laboratory reports, blood test reports, or other medical documents in PDF format and receive AI-generated answers to their queries.

Instead of manually reading lengthy reports, users can ask questions such as:

- What is the patient's hemoglobin level?
- What is the WBC count?
- What are the major health concerns?
- What are the abnormal test values?

The system extracts text from the uploaded PDF, converts it into semantic embeddings, stores them in a FAISS vector database, retrieves the most relevant context, and generates accurate responses using Gemma 3 running locally via Ollama.

The application provides an intuitive dashboard with document upload, AI-powered question answering, retrieved source context, and a clean user interface for an enhanced user experience.

## Key Performance Indicators (KPIs)
- Retrieval Accuracy of Relevant Medical Information
- Response Time for AI Question Answering
- PDF Processing Speed
- Embedding & Vector Search Performance
- Retrieval Precision using FAISS
- LLM Response Quality
- Semantic Search Accuracy
- Number of Medical Queries Successfully Answered

## Additional metrics include:

- Context retrieval relevance
- Source chunk accuracy
- Vector search latency
- AI response consistency
- Medical report processing success rate

## Technologies Used
## Frontend
- Streamlit
## AI Framework
- LangChain
## Embedding Model
- BAAI/bge-small-en-v1.5
- Vector Database
- FAISS
## Large Language Model
- Gemma 3 (via Ollama)
- PDF Processing
- PyPDF2
## Programming Language
Python
## Project Process
1. PDF Upload

Users upload medical reports such as:
- CBC Reports
- Blood Test Reports
- HbA1c Reports
- Diagnostic Reports
2. Text Extraction

The uploaded PDF is processed using PyPDF2, extracting all readable medical information while preserving the document content.

3. Text Chunking

The extracted text is divided into smaller chunks to improve semantic retrieval.

Benefits include:

- Faster retrieval
- Better context matching
- Reduced LLM workload
- Improved response accuracy
4. Embedding Generation

Each text chunk is converted into high-dimensional vector embeddings using:

BAAI/bge-small-en-v1.5

This enables semantic understanding rather than relying on exact keyword matching.

5. Vector Database Creation

The generated embeddings are stored in a FAISS Vector Database, allowing efficient similarity search across the medical document.

6. Semantic Retrieval

When a user asks a question, the retriever searches the FAISS index and identifies the most relevant text chunks related to the query.

7. Prompt Engineering

The retrieved context and the user's question are combined into a structured prompt before being sent to the LLM.

This ensures that answers remain grounded in the uploaded medical report instead of relying solely on the model's pre-trained knowledge.

8. AI-Powered Question Answering

The structured prompt is processed by Gemma 3 running locally through Ollama, generating accurate, context-aware medical responses.

9. Source Context Display

Along with the generated answer, the application displays the retrieved document chunks used to generate the response, improving transparency and explainability.


## Workflow:

User Question → Retrieve Relevant Context → Provide Context to LLM → Generate Grounded Answer

## Benefits:

- Higher answer accuracy
- Reduced hallucinations
- Context-aware responses
- Reliable document-based question answering
- Embeddings

Medical report text is transformed into vector representations using:

BAAI/bge-small-en-v1.5

Purpose:

- Semantic search
- Similarity matching
- Context understanding
- Vector Search

FAISS performs efficient nearest-neighbor search to retrieve the most relevant document chunks for each query.

## Project Insights
- Retrieval-Augmented Generation significantly improves answer accuracy over standalone LLMs.
- BGE embeddings provide better semantic retrieval than MiniLM for medical documents.
- FAISS enables fast and scalable similarity search.
- Prompt engineering ensures responses remain grounded in uploaded reports.
- Chunking improves retrieval quality while reducing computational overhead.
- Source retrieval enhances explainability and user trust.

## Conclusion

This project demonstrates how Retrieval-Augmented Generation (RAG), semantic search, vector databases, and Large Language Models can be integrated to build an intelligent medical document assistant. By combining LangChain, FAISS, BGE embeddings, and Gemma 3, the system enables users to quickly extract meaningful insights from complex medical reports through natural language interaction, delivering accurate, explainable, and context-aware AI responses.

