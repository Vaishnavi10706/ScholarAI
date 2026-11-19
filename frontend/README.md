# ScholarAI - AI Research Assistant

An AI-powered research assistant that helps students and researchers explore academic papers, retrieve relevant information, and get answers grounded in research documents.

## Overview

Reading and understanding lengthy research papers can be time-consuming. ScholarAI aims to simplify this process by using Generative AI and Retrieval-Augmented Generation (RAG) to make academic research more accessible.

Users can upload research papers in PDF format, extract their content, and search for relevant information using natural-language queries. The long-term goal is to provide reliable, context-aware answers with page-level citations so users can verify information directly from the original papers.

## Key Features

### Implemented / In Progress
- **PDF Upload:** Upload academic research papers in PDF format.
- **Text Extraction:** Extract text from PDF documents while preserving page numbers.
- **Text Chunking:** Divide extracted content into smaller, overlapping chunks.
- **Vector Storage:** Store document chunks and their embeddings using ChromaDB.
- **Semantic Search:** Retrieve relevant research passages based on natural-language questions.
- **Page Metadata:** Associate retrieved passages with their original document and page number.

### Planned Features
- **AI-Powered Q&A:** Ask questions about uploaded research papers.
- **RAG Pipeline:** Generate answers using retrieved research content as context.
- **Verifiable Citations:** Display source paper names and page numbers alongside answers.
- **Research Paper Summarization:** Generate concise summaries of academic papers.
- **Multi-Paper Comparison:** Compare findings, methodologies, and conclusions across multiple papers.
- **Research Gap Exploration:** Help identify potential research gaps and future research directions.
- **Chat History:** Maintain previous research conversations.

## Tech Stack

| Layer | Technologies |
|---|---|
| Frontend | React, Vite, Tailwind CSS |
| Backend | Python, FastAPI |
| PDF Processing | PyMuPDF |
| Vector Database | ChromaDB |
| Embeddings | ChromaDB Default Embedding Function |
| API Communication | Axios |
| Data Validation | Pydantic |
| Metadata Database | MongoDB (planned) |
| Generative AI | LLM API (planned) |

## Architecture

```text
                 USER
                   |
                   v
           React Frontend
                   |
                   v
             FastAPI Backend
                   |
          +--------+--------+
          |                 |
          v                 v
      PDF Upload       Search Query
          |                 |
          v                 v
    PyMuPDF Parser     Query Embedding
          |                 |
          v                 v
     Text Extraction    ChromaDB
          |                 |
          v                 v
      Text Chunking    Similarity Search
          |                 |
          v                 v
       Embeddings     
