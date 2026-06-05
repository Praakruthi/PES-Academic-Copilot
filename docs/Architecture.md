# Architecture


## High Level Flow

Student
↓
PES Copilot Extension
↓
Backend API
↓
Knowledge Base
↓
LLM (AI Model)
↓
Response to Student

---

## File Indexing Flow

PES Academy Files
+
User Uploaded Files
↓
Text Extraction
↓
Chunking
↓
Embeddings
↓
Vector Database

---

## Question Answering Flow

Student Question
↓
Semantic Search
↓
Retrieve Relevant Chunks
↓
Send Context + Question to LLM
↓
Generate Answer
↓
Display Answer + Sources

---

## Core Components

### Browser Extension

Responsibilities:

* Add PES Copilot button
* Collect file links
* Upload user files
* Display AI responses

### Backend

Responsibilities:

* Process files
* Generate embeddings
* Handle AI requests
* Manage knowledge base

### Vector Database

Responsibilities:

* Store embeddings
* Perform semantic search
* Retrieve relevant content

### LLM

Responsibilities:

* Answer questions
* Generate summaries
* Generate MCQs
* Conduct quizzes

---

## Future Components

* Multi-college support
* Previous year paper analysis
* Personalized study recommendations
* Advanced quiz analytics

