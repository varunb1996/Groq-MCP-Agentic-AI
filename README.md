# Groq Agentic AI RAG System

An end-to-end Agentic AI Retrieval-Augmented Generation (RAG) system built using FastAPI, Streamlit, ChromaDB, LangChain, Sentence Transformers, and Groq LLM APIs.

The project performs document ingestion, embedding generation, semantic retrieval, contextual summarization, and question answering over repository and documentation data using vector search and LLM-powered reasoning workflows.

---

# Features

- FastAPI backend APIs
- Streamlit frontend interface
- ChromaDB vector database integration
- Sentence Transformer embeddings
- Semantic document retrieval
- Context-aware summarization
- Groq LLM integration
- LangChain retrieval workflows
- MLflow experiment tracking
- Repository/document ingestion pipeline
- Local vector persistence

---

# Tech Stack

## Backend
- FastAPI
- Python

## Frontend
- Streamlit

## Vector Database
- ChromaDB

## LLM
- Groq API

## Embeddings
- Sentence Transformers

## AI Frameworks
- LangChain
- LangGraph-style workflows

## Experiment Tracking
- MLflow

---

# Project Structure
# Project Structure

```text
groq-mcp-agentic-ai/
│
├── agents/
│   ├── router_agent.py
│   ├── retrieval_agent.py
│   ├── reasoning_agent.py
│   ├── summarizer_agent.py
│   ├── memory_agent.py
│   ├── dependency_agent.py
│   ├── code_agent.py
│   ├── mcp_agent.py
│   └── .gitkeep
│
├── tools/
│   ├── groq_tool.py
│   ├── retrieval_tool.py
│   ├── memory_tool.py
│   ├── dependency_tool.py
│   ├── filesystem_tool.py
│   ├── github_tool.py
│   ├── logging_tool.py
│   └── .gitkeep
│
├── workflows/
│   ├── state.py
│   ├── langgraph_workflow.py
│   └── .gitkeep
│
├── mcp/
│   ├── mcp_client.py
│   ├── mcp_server_config.py
│   ├── tool_registry.py
│   └── .gitkeep
│
├── utils/
│   ├── config.py
│   ├── helpers.py
│   └── .gitkeep
│
├── data/
│   ├── pdfs/
│   │   └── .gitkeep
│   │
│   ├── repos/
│   │   ├── langgraph/
│   │   └── .gitkeep
│   │
│   ├── documents.json
│   └── .gitkeep
│
├── embeddings/
│   └── .gitkeep
│
├── memory/
│   └── .gitkeep
│
├── mlruns/
│   └── .gitkeep
│
├── app.py
├── api.py
├── ingest.py
├── embed.py
├── retrieval.py
├── requirements.txt
├── README.md
├── Architecture.md
├── .env.example
├── .gitignore
└── venv/ (not uploaded to GitHub)
```

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/groq-mcp-agentic-ai.git
cd groq-mcp-agentic-ai
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
```

---

# Run Pipeline

## Step 1: Ingest Documents

```bash
python ingest.py
```

## Step 2: Generate Embeddings

```bash
python embed.py
```

## Step 3: Start FastAPI Backend

```bash
uvicorn api:app --reload
```

## Step 4: Launch Streamlit Frontend

```bash
streamlit run app.py
```

---

# Example Query

```text
What is LangGraph?
```

---

# Challenges Solved

- Interrupted ONNX embedding downloads
- Chroma cache corruption handling
- Groq model deprecation migration
- Token-per-minute rate limit optimization
- LangChain package modularization fixes
- Context reduction for efficient retrieval
- Repository filtering and retrieval cleanup
- JSON parsing failure debugging

---

# Future Improvements

- Memory agents
- Hybrid BM25 + vector retrieval
- GraphRAG integration
- Redis caching
- LangSmith observability
- MCP server support
- Multi-agent orchestration
- Tool-calling workflows

---

# Author

Varun Bukka
