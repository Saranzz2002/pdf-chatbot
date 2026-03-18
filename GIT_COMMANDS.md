# 📤 How to Upload Your Project to GitHub

A beginner-friendly guide to push your PDF Chatbot project to GitHub.

---

## 📋 Prerequisites

1. **GitHub Account**: Sign up at [github.com](https://github.com) (free)
2. **Git Installed**: Download from [git-scm.com](https://git-scm.com/)
3. **Project Ready**: Your pdf_chatbot folder with all files

---

## ✅ Step-by-Step Instructions

### Step 1: Create a GitHub Repository

1. Go to [github.com](https://github.com)
2. Log in with your account
3. Click **"+"** (top right) → Select **"New repository"**
4. Fill in:
   - **Repository name**: `pdf-chatbot` (use hyphens, not underscores)
   - **Description**: "PDF Chatbot using RAG (Retrieval-Augmented Generation) - Beginner Friendly"
   - **Visibility**: Public (so others can learn from it)
5. Click **"Create repository"**
6. **Copy the URL** shown (something like: `https://github.com/YourUsername/pdf-chatbot.git`)

---

### Step 2: Configure Git (First Time Only)

Open terminal/cmd and run:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Replace with your actual name and email (same as GitHub).

---

### Step 3: Navigate to Your Project

```bash
cd C:\Users\YourName\Documents\pdf_chatbot
```

---

### Step 4: Initialize Git Repository

```bash
git init
```

This creates `.git` folder (hidden - don't delete it).

---

### Step 5: Add Files to Git

```bash
git add .
```

This stages all files for commit. Files in `.gitignore` are automatically excluded.

**Verify what's staged:**
```bash
git status
```

You should see:
```
On branch master

Initial commit

Changes to be committed:
  new file:   .gitignore
  new file:   README.md
  new file:   QUICK_START.md
  new file:   ERRORS.md
  new file:   app.py
  new file:   requirements.txt
  ...
```

---

### Step 6: Create First Commit

```bash
git commit -m "Initial commit: PDF Chatbot using RAG"
```

This saves a snapshot with a message describing what you did.

**Tips for commit messages:**
- ✅ Good: "Initial commit: PDF Chatbot using RAG"
- ✅ Good: "Add RAG implementation with Streamlit UI"
- ❌ Bad: "changes"
- ❌ Bad: "asdf"

---

### Step 7: Rename Branch to 'main' (If Needed)

GitHub uses `main` as default (not `master`):

```bash
git branch -M main
```

---

### Step 8: Add Remote Repository

Connect your local folder to GitHub:

```bash
git remote add origin https://github.com/YourUsername/pdf-chatbot.git
```

**⚠️ Replace:**
- `YourUsername` with your GitHub username
- This is the URL you copied in Step 1

---

### Step 9: Push to GitHub

Upload your files to GitHub:

```bash
git push -u origin main
```

The `-u` flag sets `main` as default for future pushes.

**On first push, you may need to:**
1. Enter your GitHub username
2. Enter a "Personal Access Token" instead of password:
   - [Create token here](https://github.com/settings/tokens)
   - Give it `repo` permissions
   - Copy and paste it when prompted

---

### Step 10: Verify Success

Go to `https://github.com/YourUsername/pdf-chatbot`

You should see all your files!

---

## 🔄 Making Changes & Updating GitHub

Once your repo is set up, here's how to update it:

### Every Time You Change Files

```bash
# 1. Check what changed
git status

# 2. Add files
git add .

# 3. Commit with message
git commit -m "Describe what you changed"

# 4. Push to GitHub
git push
```

---

## 📝 Example: Adding a New Feature

```bash
# Add improvements to app.py

# Stage all changes
git add .

# Commit with descriptive message
git commit -m "Add chat history feature"

# Push to GitHub
git push
```

---

## 📚 Good Commit Message Examples

```bash
# Feature additions
git commit -m "Add multi-PDF support"
git commit -m "Implement chat memory"

# Bug fixes
git commit -m "Fix embedding loading error"
git commit -m "Fix PDF parsing for scanned documents"

# Documentation
git commit -m "Update README with new examples"
git commit -m "Add troubleshooting guide"

# Improvements
git commit -m "Optimize chunking strategy"
git commit -m "Reduce model loading time"
```

---

## 🔧 Useful Git Commands

### View Commit History
```bash
git log
```

Shows all commits with timestamps and messages.

### Check Current Status
```bash
git status
```

Shows what files changed and what's staged.

### Undo Last Commit (Be Careful!)
```bash
git reset --soft HEAD~1
```

Keeps changes but undoes the commit.

### View Differences
```bash
git diff
```

Shows what changed in files.

---

## 🐛 Common Git Errors & Fixes

### Error: "fatal: not a git repository"
```bash
# You're not in the project folder
cd C:\Users\YourName\Documents\pdf_chatbot
```

### Error: "Permission denied (publickey)"
```bash
# Set up SSH key
# Go to: https://github.com/settings/keys
# Create new key or use personal access token
```

### Error: "Branch 'main' set up to track remote 'origin/main'"
This is not an error - just means it's working!

### Error: "git: command not found"
```bash
# Git not installed properly
# Download from: https://git-scm.com/
# Restart terminal after installation
```

---

## 📊 Complete Push Workflow (Cheat Sheet)

Copy and paste this entire block:

```bash
# Navigate to project
cd C:\Users\YourName\Documents\pdf_chatbot

# Initialize (only first time)
git init

# Configure (only first time)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Add all files
git add .

# Create commit
git commit -m "Initial commit: PDF Chatbot using RAG"

# Rename to main (only first time)
git branch -M main

# Add remote (only first time, replace YourUsername)
git remote add origin https://github.com/YourUsername/pdf-chatbot.git

# Push to GitHub
git push -u origin main
```

---

## 🎯 What Gets Uploaded?

**Uploaded Files:**
```
✅ app.py
✅ requirements.txt
✅ README.md
✅ QUICK_START.md
✅ ERRORS.md
✅ .gitignore
✅ data/ (folder, but empty because PDFs aren't uploaded)
```

**NOT Uploaded:**
```
❌ venv/ (excluded by .gitignore)
❌ *.pdf (excluded by .gitignore)
❌ __pycache__/ (excluded by .gitignore)
```

This is good! You don't need to upload `venv/` (huge) or PDFs.

---

## 🚀 Next: Share Your Project

After pushing to GitHub:

### 1. Add to Your Portfolio
```
Add to LinkedIn: "Built a RAG-based PDF Chatbot"
Add to Resume: "Created Python Streamlit app with LLM"
```

### 2. Share a Badge in README
```markdown
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28.1-red)](https://streamlit.io)
```

### 3. Deploy for Free
```bash
# Deploy to Streamlit Cloud
# (GitHub integration - one-click deploy)
```

---

## 📖 Learning More

- [GitHub Guides](https://guides.github.com/)
- [Git Basics](https://git-scm.com/book/en/v2)
- [Git Cheat Sheet](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)

---

## ❓ FAQ

**Q: Do I have to use GitHub?**
A: No, but it's great for:
- Backup
- Version control
- Sharing with others
- Portfolio

**Q: Can I keep my repo private?**
A: Yes, but make it public for portfolio value.

**Q: How do I delete a file from GitHub?**
```bash
git rm filename
git commit -m "Remove filename"
git push
```

**Q: How do I undo a push?**
```bash
git revert HEAD~1
git push
```

**Q: Can multiple people work on this?**
A: Yes! Use branches and pull requests (advanced).

---

## 🎉 Congratulations!

Your project is now on GitHub! You can:
- ✅ Share the link with anyone
- ✅ Show it in interviews
- ✅ Collaborate with others
- ✅ Keep a backup
- ✅ Track changes over time

**Your GitHub profile now shows:**
- 1 repository created
- Clean code structure
- Documentation skills
- Use of modern tech stack

This looks great on a resume! 📄✨

---

**Happy coding and sharing! 🚀**
