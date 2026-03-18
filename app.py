"""
PDF Chatbot using RAG (Retrieval-Augmented Generation)
Author: Beginner AI Developer
Description: A simple yet powerful chatbot that:
    1. Uploads PDF files
    2. Extracts and processes text
    3. Converts text to embeddings (vector representations)
    4. Stores in FAISS vector database
    5. Retrieves relevant context for user questions
    6. Generates answers using HuggingFace LLM
"""

# ============================================================================
# STEP 1: IMPORT REQUIRED LIBRARIES
# ============================================================================
import streamlit as st  # Web UI framework
import os  # For file operations
from pathlib import Path  # For file path handling
import tempfile  # For temporary file storage

# LangChain imports - Framework for building LLM applications
from langchain_community.document_loaders import PyPDFLoader  # Load PDF files
from langchain.text_splitter import RecursiveCharacterTextSplitter  # Split text into chunks
from langchain_community.vectorstores import FAISS  # Vector database for similarity search
from langchain_community.embeddings import HuggingFaceEmbeddings  # Convert text to embeddings
from langchain.chains import RetrievalQA  # Create RAG chain
from langchain_community.llms import HuggingFacePipeline  # Use HuggingFace models

from transformers import pipeline  # For loading pre-trained models

# ============================================================================
# STEP 2: CONFIGURE STREAMLIT PAGE
# ============================================================================
st.set_page_config(
    page_title="PDF Chatbot - RAG Demo",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom title and description
st.title("📄 PDF Chatbot using RAG")
st.markdown("""
### Welcome! 🎉
This app lets you:
1. ✅ Upload a PDF file
2. ✅ Ask questions about the content
3. ✅ Get intelligent answers using RAG (Retrieval-Augmented Generation)

**What is RAG?** It combines the power of:
- **Retrieval**: Finding relevant sections from your PDF
- **Augmented**: Using those sections to provide context
- **Generation**: Creating answers based on that context
""")

# ============================================================================
# STEP 3: INITIALIZE SESSION STATE (UI Memory)
# ============================================================================
# Streamlit doesn't keep variables between reruns, so we use session_state
if "pdf_loaded" not in st.session_state:
    st.session_state.pdf_loaded = False  # Track if PDF is loaded
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None  # Store FAISS vector database
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None  # Store the QA chain
if "pdf_filename" not in st.session_state:
    st.session_state.pdf_filename = ""  # Track loaded PDF name

# ============================================================================
# STEP 4: SIDEBAR - FILE UPLOAD SECTION
# ============================================================================
st.sidebar.header("📁 Configuration")
st.sidebar.markdown("---")

uploaded_file = st.sidebar.file_uploader(
    "📤 Upload a PDF file",
    type="pdf",
    help="Upload any PDF document you want to ask questions about"
)

# ============================================================================
# STEP 5: PROCESS PDF WHEN UPLOADED
# ============================================================================
if uploaded_file is not None and not st.session_state.pdf_loaded:
    with st.spinner("🔄 Processing your PDF... This may take a minute..."):
        try:
            # Step 5A: Save uploaded file to temporary location
            # Why: We need a file path to load the PDF
            temp_pdf_path = Path(tempfile.gettempdir()) / uploaded_file.name
            with open(temp_pdf_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # Step 5B: Load PDF and extract text
            # PyPDFLoader: Reads text from PDF files
            print("[INFO] Loading PDF file...")
            loader = PyPDFLoader(str(temp_pdf_path))
            documents = loader.load()
            print(f"[INFO] Loaded {len(documents)} pages from PDF")
            
            # Step 5C: Split text into chunks
            # Why: Large texts are too big for embeddings. We split into smaller pieces.
            # chunk_size=1000: Each chunk is ~1000 characters
            # chunk_overlap=200: Chunks overlap by 200 chars to keep context
            # Think of it like reading pages of a book - 1000 chars ≈ 2 pages
            print("[INFO] Splitting text into chunks...")
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,  # Size of each text chunk
                chunk_overlap=200,  # Overlap between chunks (keeps context)
                length_function=len,  # Method to measure chunk size
                separators=["\n\n", "\n", " ", ""]  # Try to split on these
            )
            chunks = splitter.split_documents(documents)
            print(f"[INFO] Created {len(chunks)} text chunks")
            
            # Step 5D: Create embeddings
            # Embeddings: Convert text to vectors (lists of numbers)
            # These vectors capture the meaning of text
            # Similar texts have similar vectors
            # Model: 'sentence-transformers/all-MiniLM-L6-v2' is fast and free
            print("[INFO] Creating embeddings...")
            embeddings = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2",
                # This model converts text to 384-dimensional vectors
                # Smaller = faster, Larger = more accurate
            )
            
            # Step 5E: Store embeddings in FAISS vector database
            # FAISS: Fast similarity search on huge datasets
            # Converts our embeddings into a searchable index
            print("[INFO] Creating vector database (FAISS)...")
            vector_store = FAISS.from_documents(
                documents=chunks,
                embedding=embeddings
            )
            
            # Step 5F: Create the LLM (Large Language Model)
            # We use Flan-T5 - a free, open-source model that works locally
            # It's smaller than GPT-4 but still very capable
            print("[INFO] Loading language model...")
            llm = HuggingFacePipeline(
                model_id="google/flan-t5-base",  # Free model from HuggingFace
                task="text2text-generation",  # Task type
                model_kwargs={
                    "temperature": 0.7,  # Controls randomness (0=deterministic, 1=random)
                    "max_length": 500  # Max answer length
                }
            )
            
            # Step 5G: Create RAG chain
            # This combines: Retrieval (from vector DB) + Augmented (with context) + Generation (LLM)
            print("[INFO] Creating QA chain...")
            qa_chain = RetrievalQA.from_chain_type(
                llm=llm,
                chain_type="stuff",  # Simple approach: combine all retrieved docs
                retriever=vector_store.as_retriever(
                    search_kwargs={"k": 3}  # Retrieve top 3 relevant chunks
                ),
                return_source_documents=True  # Also return which chunks were used
            )
            
            # Step 5H: Save to session state
            st.session_state.vector_store = vector_store
            st.session_state.qa_chain = qa_chain
            st.session_state.pdf_loaded = True
            st.session_state.pdf_filename = uploaded_file.name
            
            # Clean up temp file
            os.remove(temp_pdf_path)
            
            st.success(f"✅ Successfully loaded PDF! ({uploaded_file.name})")
            print("[INFO] PDF processing completed successfully!")
            
        except Exception as e:
            st.error(f"❌ Error processing PDF: {str(e)}")
            print(f"[ERROR] {str(e)}")

# ============================================================================
# STEP 6: MAIN CHAT INTERFACE
# ============================================================================
# Show content only if PDF is loaded
if st.session_state.pdf_loaded:
    st.markdown(f"**✅ PDF Loaded:** {st.session_state.pdf_filename}")
    st.markdown("---")
    
    # Display loaded file info in sidebar
    st.sidebar.success(f"✅ PDF loaded: {st.session_state.pdf_filename}")
    st.sidebar.info(f"📊 Vector Store prepared with embeddings")
    
    # Create two columns for better layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Input section
        st.subheader("❓ Ask a Question")
        user_question = st.text_input(
            "Enter your question about the PDF:",
            placeholder="e.g., What is the main topic of this document?",
            help="Ask anything about the content of your PDF"
        )
        
        # Button to submit question
        if st.button("🔍 Search & Answer", use_container_width=True):
            if user_question.strip():
                with st.spinner("🤔 Thinking..."):
                    try:
                        # Query the QA chain
                        # This retrieves relevant chunks and generates an answer
                        print(f"[INFO] User question: {user_question}")
                        result = st.session_state.qa_chain.invoke(
                            {"query": user_question}
                        )
                        
                        # Display the answer
                        st.markdown("### 🎯 Answer")
                        st.write(result["result"])
                        
                        # Display source chunks used
                        st.markdown("### 📚 Source Chunks Used")
                        with st.expander("View source documents (click to expand)"):
                            for i, doc in enumerate(result["source_documents"], 1):
                                st.markdown(f"**Chunk {i}:**")
                                st.write(doc.page_content)
                                st.markdown("---")
                        
                        print("[INFO] Query completed successfully")
                        
                    except Exception as e:
                        st.error(f"❌ Error generating answer: {str(e)}")
                        print(f"[ERROR] {str(e)}")
            else:
                st.warning("⚠️ Please enter a question!")
    
    with col2:
        st.subheader("ℹ️ How It Works")
        st.info("""
        **RAG Pipeline Steps:**
        
        1️⃣ **Load**: PDF text extracted
        2️⃣ **Chunk**: Text split (1000 chars)
        3️⃣ **Embed**: Text → Vectors
        4️⃣ **Store**: FAISS indexes vectors
        5️⃣ **Retrieve**: Find top 3 matching chunks
        6️⃣ **Generate**: LLM creates answer
        
        **Models Used:**
        - Embeddings: MiniLM-L6-v2
        - LLM: Flan-T5-Base
        - DB: FAISS
        """)

else:
    st.info("👆 Upload a PDF file to get started!")
    
    # Show example questions
    st.markdown("""
    ### Example Questions You Can Ask:
    - What is this document about?
    - Summarize the main points
    - What are the key findings?
    - Explain [specific topic] from the document
    """)

# ============================================================================
# STEP 7: FOOTER
# ============================================================================
st.markdown("---")
st.markdown("""
### 💡 Tips for Best Results:
1. Use PDFs with clear text (not scanned images)
2. Ask specific questions for better answers
3. Short questions often work better than long ones
4. The model uses the document content, not general knowledge

### ⚠️ Limitations:
- Works best with English text
- Scanned PDFs may not work (need OCR)
- Answer quality depends on PDF clarity
- This is a free, local model (trade-off: speed vs accuracy)

**Built with:** Streamlit, LangChain, FAISS, HuggingFace Transform Transformers
""")
