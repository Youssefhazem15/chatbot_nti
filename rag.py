# rag.py
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Load PDF
loader = PyPDFLoader("Hands_On_Large_Language_Models_Language_Understanding_and_Generation.pdf")
documents = loader.load()

# Split into chunks
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)

# Embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create FAISS index
faiss_index = FAISS.from_documents(chunks, embedding_model)

# Save to disk
faiss_index.save_local("faiss_index")
print("✅ FAISS index saved!")
