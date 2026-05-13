# System Architecture

# Overview

The Groq Agentic AI RAG System is designed as a modular Retrieval-Augmented Generation pipeline that combines document ingestion, embedding generation, vector search, semantic retrieval, and Groq-powered summarization.

The system enables contextual querying over repositories and documents using local vector storage and LLM reasoning.

---

# High-Level Architecture

```text
                 ┌────────────────────┐
                 │   User Query       │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │   Streamlit UI     │
                 └─────────┬──────────┘
                           │ HTTP Request
                           ▼
                 ┌────────────────────┐
                 │   FastAPI Backend  │
                 └─────────┬──────────┘
                           │
          ┌────────────────┴────────────────┐
          │                                 │
          ▼                                 ▼
┌────────────────────┐          ┌────────────────────┐
│ Retrieval Pipeline │          │ Groq LLM Pipeline  │
└─────────┬──────────┘          └─────────┬──────────┘
          │                               │
          ▼                               ▼
┌────────────────────┐          ┌────────────────────┐
│ ChromaDB Vector DB │          │ Summarization      │
└─────────┬──────────┘          │ Response Generation│
          │                     └────────────────────┘
          ▼
┌────────────────────┐
│ SentenceTransformer│
│ Embeddings         │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Repository/Data    │
│ Documents          │
└────────────────────┘
```

---

# Pipeline Flow

## 1. Document Ingestion

`ingest.py`
- Reads repositories/documents
- Cleans unnecessary files
- Stores structured document data

---

## 2. Embedding Generation

`embed.py`
- Loads Sentence Transformer model
- Converts document chunks into embeddings
- Stores embeddings in ChromaDB

---

## 3. Semantic Retrieval

`retrieval.py`
- Encodes user query
- Performs vector similarity search
- Retrieves relevant contextual chunks

---

## 4. LLM Summarization

`summarizer_agent.py`
- Sends retrieved context to Groq LLM
- Generates contextual response
- Returns summarized output

---

## 5. API Layer

`api.py`
- Exposes REST API endpoints
- Handles query requests
- Connects retrieval and summarization pipeline

---

## 6. Frontend Layer

`app.py`
- Streamlit-based user interface
- Accepts natural language queries
- Displays retrieved context and generated response

---

# Core Technologies

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI |
| Embeddings | Sentence Transformers |
| Vector DB | ChromaDB |
| LLM | Groq |
| AI Framework | LangChain |
| Tracking | MLflow |

---

# Key Engineering Challenges Solved

## Chroma Cache Recovery
Resolved interrupted ONNX model downloads and corrupted embedding cache issues.

## Groq Model Migration
Migrated deprecated Groq model identifiers to supported models.

## Token Optimization
Reduced oversized retrieval contexts to stay within Groq TPM limits.

## Retrieval Cleanup
Filtered `.git`, metadata, and unnecessary repository files to improve semantic relevance.

## LangChain Compatibility
Resolved dependency fragmentation caused by newer LangChain modular package architecture.

---

# Future Enhancements

- Hybrid Search (BM25 + Vector)
- GraphRAG
- Memory Agents
- Tool Calling
- Redis Cache Layer
- LangSmith Monitoring
- Multi-Hop Retrieval
- MCP Server Integration
- Autonomous Agent Workflows
