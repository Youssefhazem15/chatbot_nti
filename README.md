# 🩺 Medical Assistant Chatbot

A multi-functional AI-powered medical chatbot that fuses document retrieval, large language models, OCR, and disease-specific logic to deliver actionable health insights. Developed as an NTI graduation project using industry-standard AI tools.

---

## 🚀 Features

- ✅ Interactive chat-based Q&A on medical topics
- 🧠 Retrieval-Augmented Generation (RAG) from trusted medical PDFs
- 📝 OCR support for extracting text from scanned prescriptions or medical documents
- 📊 Disease risk analysis based on user-entered values (e.g., glucose, blood pressure)
- 🧾 Auto-generated titles for each chat
- 🗂️ Persistent session chat history

---

## 🧪 Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Core programming language |
| 🌐 Streamlit | User-friendly frontend chat interface |
| ⚡ FastAPI | High-performance backend/API |
| 🤖 Together AI (LLaMA 3) | Advanced language model for natural-language answers |
| 🔗 LangChain | Modular RAG and workflow orchestration |
| 📁 FAISS | Fast similarity search for document chunks |
| 🔍 pytesseract | OCR for image and scan text extraction |
| 🧬 Custom medical logic | Disease risk evaluation by thresholding lab/test results |

---

## 🧠 How It Works

1. **User submits a medical question** through the Streamlit chat interface.
2. **Backend fetches related document excerpts** via FAISS and LangChain for accurate, context-aware responses.
3. **Prompt is sent to LLaMA 3** on Together AI for answer generation.
4. If an image is provided, **OCR extracts text** and feeds it to the model as context.
5. If the user includes measurements (e.g., blood sugar), **custom disease logic** analyzes health risk.
6. **Answers and session titles are stored** in chat history for future reference.

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Youssefhazem15/AI-Medical-Chatbot.git
cd AI-Medical-Chatbot
```

### 2. Create a Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys
Create a `.env` file:

### 5. Build the FAISS Index
```bash
python rag.py
```

### 6. Run the Backend
```bash
uvicorn fast:app --port 8000 --reload
```

### 7. Run the Frontend
Open a new terminal:
```bash
streamlit run app.py
```

### 8. Open in Browser
http://localhost:8501

---

## 📂 Project Structure
AI-Medical-Chatbot/
├── app.py              # Streamlit UI
├── fast.py             # FastAPI backend
├── rag.py              # PDF/CSV to FAISS index builder
├── llm.py              # LLM test script
├── faiss_index/        # Generated vector index
├── .env                # API keys (excluded from git)
├── requirements.txt    # Dependencies
└── README.md
