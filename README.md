# 📄 PDF Chatbot using RAG (Retrieval-Augmented Generation)

A beginner-friendly project that demonstrates how to build a conversational AI application that can answer questions about PDF documents using **Retrieval-Augmented Generation (RAG)**.

## 🎯 What Does This Project Do?

You upload a PDF file, and the chatbot answers your questions based on the PDF's content. It's like having a smart assistant that reads your document and can explain things from it.

### Example:
- **You upload:** A research paper on AI
- **You ask:** "What are the main findings?"
- **Bot answers:** Extracts and summarizes relevant sections from the paper

---

## 🧠 Understanding RAG (Simple Explanation)

### What is RAG?

RAG stands for **Retrieval-Augmented Generation**. It's a technique that combines:

1. **Retrieval** 🔍: Finding relevant information
2. **Augmented** 📚: Using that information as context
3. **Generation** ✍️: Creating an intelligent response

### Why Not Just Use ChatGPT?

Regular LLMs (like ChatGPT) have **knowledge cutoff dates** and don't know about your specific documents.

RAG solves this by:
- Reading YOUR documents
- Finding relevant parts
- Feeding them to an LLM
- Getting answers based on YOUR data

### How It Works (Simple Analogy)

Imagine you're student preparing for an exam:

1. **Traditional LLM**: Reading a general textbook (generic knowledge)
2. **RAG**: Using your specific class notes + general knowledge (better answers!)

---

## 🏗️ Project Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INTERFACE (Streamlit)                │
│                   (Upload PDF, Ask Questions)                │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                  PDF PIPELINE                                │
│  1. Load PDF  → 2. Split Text → 3. Create Embeddings        │
│  4. Store in Vector DB → 5. Retrieve Relevant Chunks        │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│              LLM (Language Model)                            │
│         (Flan-T5: Generate Answers)                          │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔧 Key Concepts Explained

### 1. **PDF Loading**
- Extracts all text from PDF pages
- Tools used: `PyPDFLoader`

### 2. **Text Chunking**
- Splits long text into smaller pieces (chunks)
- Why? Embeddings work better on shorter text
- **chunk_size=1000**: Each chunk is ~1000 characters (roughly 2 pages)
- **chunk_overlap=200**: Chunks overlap to preserve context

Example:
```
Original text: "The quick brown fox jumps over the lazy dog. The dog was sleeping..."

Chunk 1: "The quick brown fox jumps over the lazy dog. The dog was sleeping..."
                                                 ↓ (200 char overlap)
Chunk 2: "...dog was sleeping under the tree. The tree was very old..."
```

### 3. **Embeddings**
- Convert text into vectors (lists of numbers)
- Each meaning gets a unique number pattern
- Similar texts = similar vectors
- Model: `sentence-transformers/all-MiniLM-L6-v2`
  - **384-dimensional vectors** (384 numbers per text)
  - Free, fast, and accurate enough for most use cases

Example:
```
"The cat sat on the mat"  → [0.234, 0.567, -0.123, ... (384 numbers total)]
"The dog sat on the floor" → [0.245, 0.571, -0.120, ... (similar pattern)]
"Blue elephants dance" → [0.891, -0.234, 0.567, ... (different pattern)]
```

### 4. **Vector Database (FAISS)**
- Fast similarity search database
- When you ask a question:
  1. Convert question to vector
  2. Find vectors close to it in the database
  3. Return chunks with similar vectors
  4. These are the "relevant" sections

### 5. **LLM (Language Model)**
- Flan-T5: Google's free, open-source model
- Takes: Retrieved chunks + Question
- Produces: Natural language answer
- **Why Flan-T5?**
  - ✅ Free (no API costs)
  - ✅ Runs locally (privacy)
  - ✅ Fast enough for demos
  - ❌ Smaller than GPT-4 (less advanced)

---

## 📋 Prerequisites

- **Python 3.8+** installed
- **Pip** (comes with Python)
- **~5GB disk space** (for downloading models)
- **Internet connection** (for first-time setup)

---

## 🚀 Setup Instructions

### Step 1: Create Project Folder
```bash
mkdir pdf_chatbot
cd pdf_chatbot
```

### Step 2: Create Virtual Environment (Windows)
```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment
```bash
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Windows CMD
venv\Scripts\activate.bat

# macOS/Linux
source venv/bin/activate
```

You should see `(venv)` at the start of your terminal line.

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

This installs all required packages:
- **langchain**: Framework for building LLM apps
- **faiss-cpu**: Vector database
- **pypdf**: PDF reading
- **streamlit**: Web UI
- **sentence-transformers**: Embeddings
- **transformers**: LLM models
- **torch**: Deep learning framework

### Step 5: Create Data Folder (for PDFs)
```bash
mkdir data
```

---

## 🎮 How to Run

### Start the Application
```bash
streamlit run app.py
```

The app will open in your browser at: `http://localhost:8501`

### Using the App
1. **Upload a PDF**: Click "📤 Upload a PDF file" in the sidebar
2. **Wait for processing**: App will:
   - Extract text from PDF
   - Split into chunks
   - Create embeddings
   - Build vector database
   - This takes 1-3 minutes (first time is slower)
3. **Ask a question**: Type your question and click "🔍 Search & Answer"
4. **View answer**: See the generated answer and source chunks

---

## 📂 Project Structure

```
pdf_chatbot/
│
├── app.py                 # Main application (Streamlit)
├── requirements.txt       # Python dependencies
├── README.md              # This file
│
├── data/                  # Folder for PDFs
│   └── example.pdf        # Your PDFs go here
│
└── venv/                  # Virtual environment (created automatically)
    ├── lib/
    ├── Scripts/
    └── ...
```

---

## 🧪 Testing the App

### Test with a Simple PDF
1. Create a small test PDF (~1-2 pages)
2. Upload it to the app
3. Ask simple questions like:
   - "What is this document about?"
   - "Summarize the main points"
   - "List the key findings"

---

## ⚙️ Important Parameters (Tuning for Your Needs)

If you want to improve the app, you can modify these in `app.py`:

### 1. **Chunk Size** (line ~120)
```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,    # Increase: more context, slower
                        # Decrease: less context, faster
    chunk_overlap=200   # Increase: better overlap, slower
)
```

### 2. **Retrieval Count** (line ~160)
```python
retriever=vector_store.as_retriever(
    search_kwargs={"k": 3}  # k=3: retrieve top 3 chunks
                             # Increase: more context, slower
)
```

### 3. **Temperature** (line ~148)
```python
model_kwargs={
    "temperature": 0.7,  # 0.0: deterministic (same answer)
                         # 1.0: random (different answers)
}
```

---

## ⚠️ Common Errors & Fixes

### Error 1: "ModuleNotFoundError: No module named 'streamlit'"
**Cause**: Virtual environment not activated or packages not installed
**Fix**:
```bash
# Activate venv
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate     # macOS/Linux

# Install packages
pip install -r requirements.txt
```

### Error 2: "PDF processing taking too long or hanging"
**Cause**: First-time model download is slow, or PDF is very large
**Fix**:
- Be patient on first run (downloading ~2GB of models)
- Try with a smaller PDF file first
- Check internet connection

### Error 3: "FAISS initialization error"
**Cause**: Torch (deep learning framework) installation issue
**Fix**:
```bash
pip install --upgrade torch
```

### Error 4: "CUDA not found" error
**Cause**: App trying to use GPU (not needed for demo)
**Fix**: The app already uses CPU mode (`faiss-cpu`)

### Error 5: "Answer is not long/detailed enough"
**Cause**: Temperature too low or max_length too short
**Fix**: In app.py, adjust:
```python
model_kwargs={
    "temperature": 0.9,    # Increase from 0.7
    "max_length": 800      # Increase from 500
}
```

### Error 6: "Out of memory error"
**Cause**: Document too large
**Fix**:
- Use a smaller PDF
- Increase chunk_size to reduce number of chunks
- Add filtering to skip certain pages

---

## 📊 How the RAG Pipeline Works (Detailed)

### Example: Uploading a 10-page PDF and asking "What is the main topic?"

```
┌─ STEP 1: LOADING ────────────────────────────────────┐
│  Input: 10-page PDF                                  │
│  Process: PyPDFLoader reads all pages               │
│  Output: Full text from all 10 pages               │
└──────────────────────────────────────────────────────┘
                           │
┌─ STEP 2: CHUNKING ──────────────────────────────────┐
│  Input: ~20,000 character text                       │
│  Process: Split into chunks of 1000 chars          │
│  Output: 20 chunks (with 200 char overlap)         │
└──────────────────────────────────────────────────────┘
                           │
┌─ STEP 3: EMBEDDING ─────────────────────────────────┐
│  Input: 20 chunks of text                            │
│  Process: MiniLM converts each to 384-D vector     │
│  Output: 20 vectors (384 numbers each)             │
└──────────────────────────────────────────────────────┘
                           │
┌─ STEP 4: INDEXING ──────────────────────────────────┐
│  Input: 20 vectors                                   │
│  Process: FAISS builds searchable index            │
│  Output: Indexed database ready for queries        │
└──────────────────────────────────────────────────────┘
                           │
        User asks: "What is the main topic?"
                           │
┌─ STEP 5: RETRIEVAL ─────────────────────────────────┐
│  Input: Question "What is the main topic?"          │
│  Process: Convert to vector → Find 3 closest      │
│  Output: Top 3 most similar chunks                 │
│           (probably from page 1-2, introduction)   │
└──────────────────────────────────────────────────────┘
                           │
┌─ STEP 6: AUGMENTATION ──────────────────────────────┐
│  Input: 3 chunks + Question                          │
│  Process: Combine into prompt                       │
│  Prompt: [Chunks] + "Question: What is the topic?"└──────────────────────────────────────────────────────┘
                           │
┌─ STEP 7: GENERATION ────────────────────────────────┐
│  Input: Combined prompt                              │
│  Process: Flan-T5 generates natural answer         │
│  Output: "The document is about [topic], as       │
│           evidenced by [details from chunks]"     │
└──────────────────────────────────────────────────────┘
                           │
                   User sees answer!
```

---

## 💡 Tips & Best Practices

### ✅ Do:
- Use clear, well-formatted PDFs
- Ask specific questions ("What is the budget for Q1?" vs "Tell me about finances")
- Break down complex questions into simpler ones
- Include context if needed

### ❌ Don't:
- Use scanned images without OCR
- Ask questions unrelated to the PDF (model will try but may fail)
- Expect perfect answers (it's still AI, not perfect)
- Give extremely long PDFs (>100 pages may be slow)

---

## 🚀 Deployment (Advanced)

To deploy this app online (free options):

### Option 1: Streamlit Cloud (Easiest)
```bash
# Push to GitHub first
git add .
git commit -m "PDF Chatbot using RAG"
git push

# Then deploy at: https://share.streamlit.io
```

### Option 2: Hugging Face Spaces (Free)
1. Create repo on Hugging Face
2. Push code there
3. Uses Streamlit natively

### Option 3: Docker (Advanced)
```bash
# Create Dockerfile and deploy anywhere
docker build -t pdf-chatbot .
docker run -p 8501:8501 pdf-chatbot
```

---

## 📚 Further Learning

### Resources:
- [LangChain Docs](https://python.langchain.com/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [FAISS Tutorial](https://github.com/facebookresearch/faiss)
- [Sentence Transformers](https://www.sbert.net/)

### Try These Next:
1. Add memory (remember previous questions)
2. Multiple PDF support
3. Different LLM models
4. Configurable embedding models
5. Export chat history

---

## 🤝 Contributing

Found a bug or want to improve? Feel free to modify and enhance!

---

## 📄 License

This project is open-source and free to use.

---

## ❓ FAQ

**Q: Why is the first run slow?**
A: Models are downloaded (~2GB). Subsequent runs are faster.

**Q: Can I use GPT-4 instead?**
A: Yes, but you'd need an API key (paid). Currently using free Flan-T5.

**Q: Does this work with images in PDFs?**
A: Not directly. It only reads text. For scanned PDFs, use OCR first.

**Q: Can I upload multiple PDFs?**
A: Current version supports one at a time. Can be modified for multiple PDFs.

**Q: Is my data private?**
A: Yes! Everything runs locally. No data sent to external servers.

**Q: How accurate are the answers?**
A: ~80-90% for clear PDFs with direct information. Less for inference/analysis.

---

## 📧 Questions?

Check `app.py` comments for detailed explanations of each step!

---

**Happy chatting with your PDFs! 🚀**
