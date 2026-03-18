# 🚀 Quick Start Guide (5 Minutes)

Follow these steps exactly to get the app running in 5 minutes.

---

## ⏱️ Step-by-Step (Copy & Paste)

### Step 1: Navigate to Project Folder
```bash
cd C:\Users\YourName\Documents\pdf_chatbot
```

### Step 2: Activate Virtual Environment
```bash
.\venv\Scripts\Activate.ps1
```

You should see `(venv)` at the start of your terminal line.

**If you get an error about execution policy, run:**
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try again.

### Step 3: Verify Packages are Installed
```bash
pip list
```

You should see:
- streamlit
- langchain
- faiss-cpu
- pypdf
- sentence-transformers
- transformers
- huggingface-hub
- torch

If any are missing:
```bash
pip install -r requirements.txt
```

### Step 4: Start the App
```bash
streamlit run app.py
```

The app should open in your browser automatically.

**If it doesn't open:**
- Manually go to: `http://localhost:8501`
- Check terminal for error messages

---

## 📤 How to Use the App

1. **In the left sidebar:**
   - Click "📤 Upload a PDF file"
   - Select your PDF (start with < 10 pages)
   - Wait for "✅ Successfully loaded PDF!" message

2. **Main area:**
   - Type your question in the text box
   - Click "🔍 Search & Answer"
   - Wait for the answer (15-30 seconds)

3. **View results:**
   - Read the answer
   - Click "View source documents" to see chunks used

---

## 🛑 Troubleshooting (Quick Fixes)

| Problem | Solution |
|---------|----------|
| `(venv)` doesn't appear | Run: `.\venv\Scripts\Activate.ps1` |
| Module not found | Run: `pip install -r requirements.txt` |
| Port 8501 already in use | Run: `streamlit run app.py --server.port 8502` |
| App hangs on first run | Let it finish (downloading models ~2GB) |
| PDF upload fails | Try a different, smaller PDF |
| Poor answer quality | Try a clearer PDF or different question |

See `ERRORS.md` for detailed troubleshooting.

---

## 📚 Example Questions to Try

After uploading a PDF, try asking:

✅ **Work Well:**
- "What is the main topic?"
- "Summarize this document"
- "What are the key points?"
- "List the findings"
- "Who is the author?"

❌ **Might Not Work:**
- "What do you think about this?" (opinion)
- "How does this compare to [other document]?" (needs both)
- "Predict the future based on this" (requires inference)

---

## 🎯 Next Steps

1. ✅ Download a test PDF from internet
2. ✅ Upload it to the app
3. ✅ Ask 3-4 questions
4. ✅ Check answers and source chunks
5. ✅ Read `README.md` for deep understanding
6. ✅ Modify `app.py` to customize (change models, etc.)
7. ✅ Push to GitHub when satisfied

---

## 📚 Useful Files

- **README.md**: Full documentation and explanations
- **ERRORS.md**: Troubleshooting guide for common errors
- **app.py**: Main application (well-commented code)
- **requirements.txt**: List of all dependencies
- **GIT_COMMANDS.md**: How to push to GitHub

---

## ⚙️ Simple Customizations (No coding needed)

### Change the Chunk Size (simpler = faster)
In `app.py`, find line ~120:
```python
chunk_size=1000,  # Change to 500 for faster, 2000 for better context
```

### Change the Temperature (randomness)
In `app.py`, find line ~148:
```python
"temperature": 0.7,  # Lower (0.3) = consistent, Higher (0.9) = random
```

### Use Different LLM Model
In `app.py`, find line ~145:
```python
model_id="google/flan-t5-base",  # Can change to "flan-t5-large"
```

---

## ❓ FAQ

**Q: Why is it slow on first run?**
A: Downloading 2GB of models. Next runs are fast!

**Q: Do I need GPU?**
A: No, it works on CPU. GPU makes it faster but not required.

**Q: Can I use my own LLM?**
A: Yes! Change the model_id in app.py (see above).

**Q: Is my data private?**
A: Yes! Everything runs locally on your computer.

**Q: Can I upload multiple PDFs?**
A: One at a time currently. Can be modified for multiple (advanced).

---

**Ready? Run `streamlit run app.py` and upload your first PDF! 🎉**
