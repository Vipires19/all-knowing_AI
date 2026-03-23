# 🧠 Gideon AI - Multi-Source Document Chat Assistant

Gideon is an AI-powered assistant built with **Streamlit + LangChain + OpenAI**, capable of answering questions based on multiple data sources such as websites, YouTube videos, PDFs, CSVs, Excel files, and plain text.

This project demonstrates how to build a **context-aware conversational AI system** that dynamically adapts to user-provided content.

---

## 🚀 Features

- 🌐 Load and analyze **websites**
- 🎥 Extract and understand **YouTube transcripts**
- 📄 Chat with **PDF documents**
- 📊 Read and query **CSV & Excel files**
- 📝 Process **plain text files**
- 💬 Contextual chat with memory (conversation history)
- ⚡ Real-time streaming responses
- 🧠 Dynamic prompt injection based on loaded content

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **OpenAI (GPT-3.5 Turbo)**
- **Document Loaders (LangChain Community)**
- **Conversation Memory (Buffer Memory)**

---

## 📁 Project Structure


.
├── app.py
├── loaders.py
├── requirements.txt
└── README.md


---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/gideon-ai.git
cd gideon-ai
Create a virtual environment:
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
Install dependencies:
pip install -r requirements.txt
Set your OpenAI API key:
export OPENAI_API_KEY=your_api_key_here

Or use .env / Streamlit secrets.

▶️ Running the App
streamlit run app.py
🧠 How It Works
1. Document Loading

The system supports multiple input types using LangChain loaders:

WebBaseLoader → Websites
YoutubeLoader → Video transcripts
PyPDFLoader → PDFs
CSVLoader → CSV files
UnstructuredExcelLoader → Excel files
TextLoader → Text files

Each source is converted into a unified text format.

📎 See implementation:

2. Dynamic Prompt Engineering

The assistant injects the loaded document directly into the system prompt:

Ensures responses are grounded in the content
Avoids hallucination (basic level)
Creates a contextual "knowledge base on the fly"
3. Conversational Memory

Uses:

ConversationBufferMemory

This allows the assistant to:

Remember previous messages
Maintain context across interactions

📎 Chat logic:

4. Streaming Responses

Responses are streamed in real time using:

chat.write_stream(...)

This improves UX and simulates real-time thinking.

📌 Key Highlights
🔥 Multi-source ingestion (rare in beginner projects)
🧠 Context injection via prompt (proto-RAG approach)
💬 Stateful chat with memory
⚡ Streaming output for better UX
🧩 Modular loader architecture
⚠️ Limitations
Not a full RAG (no embeddings / vector database)
Entire document is injected into prompt (token limitations)
No chunking or retrieval optimization
No authentication or multi-user support
🔮 Future Improvements
Implement vector database (FAISS / Pinecone / MongoDB Atlas)
Add document chunking + retrieval (true RAG)
Support multiple documents simultaneously
Improve prompt engineering (system control / guardrails)
Deploy as SaaS (multi-user)
Add file preview and metadata display
📷 Demo

Add screenshots or a GIF of the app here (highly recommended)

📄 License

MIT License

👨‍💻 Author

Developed by Vinícius Pires
