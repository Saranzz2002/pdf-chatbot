# 🐛 Common Errors & Troubleshooting Guide

A comprehensive guide for beginners to fix common issues.

---

## 🔴 Error 1: "ModuleNotFoundError: No module named 'streamlit'"

### What Does This Mean?
Your Python can't find the `streamlit` module. It's either not installed or your virtual environment isn't activated.

### How to Fix:

**Step 1: Verify Virtual Environment is Activated**
```bash
# On Windows, you should see (venv) at the start:
# (venv) PS C:\Users\YourName\Documents\pdf_chatbot>

# If you don't see (venv), activate it:
.\venv\Scripts\Activate.ps1  # Windows PowerShell
# OR
venv\Scripts\activate.bat    # Windows Command Prompt
```

**Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 3: Verify Installation**
```bash
pip show streamlit
```

If you see package info, it's installed correctly!

---

## 🔴 Error 2: "No such file or directory: 'data'"

### What Does This Mean?
The `data/` folder wasn't created.

### How to Fix:
```bash
# Create the data folder
mkdir data

# Verify it was created
dir  # Windows
ls   # macOS/Linux
```

---

## 🔴 Error 3: "ValueError: PDF loader is not initialized"

### What Does This Mean?
The PDF file is either corrupted, empty, or not a valid PDF.

### How to Fix:

1. **Check if PDF is valid**
   - Try opening the PDF in Adobe Reader
   - If it won't open, it's corrupted

2. **Check file size**
   - PDF should be > 10KB
   - Very small PDFs might cause issues

3. **Try a different PDF**
   - Test with a known good PDF
   - Official documents work best

4. **Convert the PDF**
   ```bash
   # If you suspect encoding issues, convert using online tools
   # https://cloudconvert.com/pdf-to-pdf
   ```

---

## 🔴 Error 4: "CUDA out of memory" or "OutOfMemoryError"

### What Does This Mean?
The app ran out of RAM (computer memory).

### How to Fix:

**Option 1: Use a Smaller PDF**
```bash
# Test with a small file first (< 5 pages)
# Then try larger files
```

**Option 2: Reduce Chunk Size**
In `app.py`, find this line and decrease the number:
```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,      # Changed from 1000 to 500
    chunk_overlap=100,   # Changed from 200 to 100
)
```

**Option 3: Close Other Programs**
- Close Chrome, Spotify, Discord, etc.
- Free up RAM and try again

**Option 4: Restart Computer**
- Sometimes clearing memory helps

---

## 🔴 Error 5: "Connection refused" or "OSError: [Errno 10061]"

### What Does This Mean?
Streamlit can't start the web server.

### How to Fix:

**Solution 1: Port Already in Use**
```bash
# Kill the process using port 8501
# Windows: Use Task Manager and look for Python

# Or run on different port:
streamlit run app.py --server.port 8502
```

**Solution 2: Firewall Blocking**
- Open Windows Defender Firewall
- Allow Python through firewall
- Try again

**Solution 3: Reinstall Streamlit**
```bash
pip uninstall streamlit
pip install streamlit==1.28.1
```

---

## 🔴 Error 6: "ImportError: transformers not installed"

### What Does This Mean?
The `transformers` library isn't installed.

### How to Fix:
```bash
# Make sure virtual environment is activated
.\venv\Scripts\Activate.ps1

# Install transformers
pip install transformers==4.36.2

# Install huggingface-hub as well
pip install huggingface-hub==0.20.3

# Test installation
python -c "import transformers; print(transformers.__version__)"
```

---

## 🔴 Error 7: "App processing is slow / hanging"

### What Does This Mean?
The app is processing but taking a long time.

### How to Fix:

**First Time?** (Normal, takes 3-5 minutes)
- Don't cancel! Let it finish downloading models
- Subsequent runs are much faster

**Not First Time?** (Something's wrong)
1. **Check disk space**: Need 5GB+ free
   ```bash
   # Windows: Open "This PC" and check C: drive
   ```

2. **Check RAM**: Need 8GB+ RAM
   ```bash
   # Open Task Manager > Performance tab
   ```

3. **Close background apps**: Free up resources

4. **Reduce PDF size**: Use a smaller test PDF

---

## 🔴 Error 8: "Unexpected token )"  or Syntax Error

### What Does This Mean?
There's a Python syntax error (typo in code).

### How to Fix:

**Check the error message carefully:**
```
File "app.py", line 145, unexpected token )
```

**This points to line 145. Check that line for typos.**

Common issues:
- Missing `(` or `)`
- Missing `:`
- Wrong indentation (use spaces, not tabs)

If you can't find it:
```bash
# Re-download the app.py from the repo
```

---

## 🔴 Error 9: "The model name provided is not valid"

### What Does This Mean?
The embedding model or LLM model name is wrong.

### How to Fix:

The models used are correct, but if you changed them:

**Check Embedding Model:**
```python
# Should be exactly:
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"  # ✓ Correct
)
```

**Check LLM Model:**
```python
# Should be exactly:
llm = HuggingFacePipeline(
    model_id="google/flan-t5-base"  # ✓ Correct
)
```

**Valid alternatives:**
```python
# Embedding models (free):
"sentence-transformers/all-MiniLM-L6-v2"  # Fast (default)
"sentence-transformers/all-mpnet-base-v2"  # More accurate

# LLM models (free):
"google/flan-t5-base"           # Balanced (default)
"google/flan-t5-large"          # Better but slower
"google/flan-t5-small"          # Faster but less accurate
```

---

## 🔴 Error 10: "Answer quality is poor / nonsensical"

### What Does This Mean?
The answers make no sense or are incomplete.

### Why This Happens:
1. PDF quality poor / blurry text
2. Chunk size too small
3. Temperature too high
4. LLM model too small

### How to Fix:

**Option 1: Improve PDF Quality**
```bash
# Use a high-quality PDF
# Avoid scanned documents without OCR
# Test with official documents first
```

**Option 2: Adjust Temperature (randomness)**
```python
# Lower temperature = more consistent
model_kwargs={
    "temperature": 0.3,  # Lower = more deterministic
    "max_length": 500
}
```

**Option 3: Increase Chunk Size**
```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000,     # Larger chunks = more context
    chunk_overlap=400
)
```

**Option 4: Use Larger Model**
```python
llm = HuggingFacePipeline(
    model_id="google/flan-t5-large"  # More powerful
)
```

---

## 🔴 Error 11: "No space left on device"

### What Does This Mean?
Your hard drive is full.

### How to Fix:

1. **Check disk space:**
   ```bash
   # Windows: C: drive in File Explorer
   # Need at least 5-10GB free
   ```

2. **Delete unnecessary files:**
   - Downloads folder
   - Temp files
   - Old projects

3. **Clear cache:**
   ```bash
   rm -rf ~/.cache/huggingface  # Linux/macOS
   # Windows: Delete C:\Users\YourName\.cache\huggingface
   ```

---

## 🔴 Error 12: "SSL: CERTIFICATE_VERIFY_FAILED"

### What Does This Mean?
Certificate verification error when downloading models.

### How to Fix:

**Solution 1: Update Certificates (macOS)**
```bash
/Applications/Python\ 3.x/Install\ Certificates.command
```

**Solution 2: Disable Verification (Temporary)**
```bash
pip install --trusted-host files.pythonhosted.org --trusted-host pypi.python.org transformers
```

**Solution 3: Update Pip**
```bash
pip install --upgrade pip certifi
```

---

## 🟠 Warning: "The `embedding_function` argument is not a valid..."

### What Does This Mean?
Minor version compatibility issue (not a blocking error).

### How to Fix:
```python
# Just ignore this warning - the app still works
# To suppress it, add this to app.py (line 1):
import warnings
warnings.filterwarnings("ignore")
```

---

## 🔧 Debugging Tips

### How to Get More Information

**Step 1: Enable Debug Mode**
Add this to the start of app.py:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

**Step 2: Print Diagnostic Info**
```bash
# Check Python version
python --version

# Check Pip version
pip --version

# List all installed packages
pip list

# Check specific package
pip show streamlit
```

**Step 3: Test Components Separately**
```python
# Test PDF loading only
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("path/to/pdf.pdf")
docs = loader.load()
print(f"Loaded {len(docs)} pages")

# Test embeddings only
from langchain_community.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings()
result = embeddings.embed_documents(["Hello world"])
print(f"Embedding successful: {len(result[0])} dimensions")
```

---

## 🔄 Complete Fresh Install

If nothing works, do a complete fresh install:

```bash
# Deactivate current environment
deactivate

# Remove venv folder
rm -r venv  # Linux/macOS
rmdir /s venv  # Windows

# Create new venv
python -m venv venv

# Activate
.\venv\Scripts\Activate.ps1  # Windows

# Install again
pip install -r requirements.txt

# Run app
streamlit run app.py
```

---

## 📞 Still Stuck?

1. **Check the error message carefully** - it usually tells you the problem
2. **Google the error** - likely someone had it before
3. **Review app.py comments** - detailed explanations are there
4. **Try a minimal example** - test with smallest possible PDF
5. **Ask for help** - include:
   - Exact error message
   - What you were doing
   - Your Python version
   - Your OS

---

## ✅ How to Know Everything is Working

```bash
# Test 1: Python is installed
python --version
# Expected: Python 3.8 or higher

# Test 2: Virtual environment works
.\venv\Scripts\Activate.ps1
# Expected: (venv) appears in prompt

# Test 3: All packages installed
pip list | findstr streamlit  # Windows
pip list | grep streamlit    # Linux/macOS
# Expected: streamlit 1.28.1

# Test 4: App starts
streamlit run app.py
# Expected: Opens browser at localhost:8501

# Test 5: Can upload PDF
# Upload a small test PDF
# Expected: "✅ Successfully loaded PDF!" message

# Test 6: Can ask questions
# Type "What is this document about?"
# Expected: Gets an answer (maybe not perfect, but gets something)
```

---

**Good luck! Most errors are easy to fix - just follow the steps above! 🚀**
