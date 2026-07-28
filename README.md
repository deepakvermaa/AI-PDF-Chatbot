# 🤖 AI PDF Chatbot

An AI-powered PDF Question Answering application built with **Streamlit**, **Google Gemini**, **FAISS**, and **Sentence Transformers**.

Upload a PDF, ask questions in natural language, and receive context-aware answers generated using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- 📄 Upload PDF documents
- 🤖 Ask questions in natural language
- 🧠 Retrieval-Augmented Generation (RAG)
- 🔍 Semantic search using FAISS
- 📚 Sentence Transformer embeddings
- 💬 Chat history support
- 🗑️ Clear chat option
- ⚡ Fast and interactive Streamlit interface
- 🔐 Secure API key management using `.env`

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Frontend | Streamlit |
| LLM | Google Gemini |
| Vector Database | FAISS |
| Embeddings | Sentence Transformers |
| PDF Processing | PyPDF |
| Text Splitting | LangChain |
| Environment Variables | Python Dotenv |

---

## 📂 Project Structure

```
AI-PDF-Chatbot/
│
├── app.py
├── config.py
├── loader.py
├── retrieval.py
├── generator.py
├── create_index.py
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/deepakvermaa/AI-PDF-Chatbot.git
```

### Go to project folder

```bash
cd AI-PDF-Chatbot
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Get your Gemini API key from Google AI Studio.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📸 Application Preview

> Add screenshots here after deployment.

Example:

```
images/
    home.png
    chat.png
```

Then use:

```markdown
![Home](images/home.png)

![Chat](images/chat.png)
```

---

## 🔮 Future Improvements

- Support multiple PDFs
- Source citation with page numbers
- Conversation export
- Streaming responses
- Docker support
- Cloud deployment

---

## 👨‍💻 Author

**Deepak Kumar Verma**

GitHub: https://github.com/deepakvermaa

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub.