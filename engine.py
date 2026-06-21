import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain_classic.chains import RetrievalQA

# Set up local directories
DATA_DIR = "./data"
DB_DIR = "./chroma_db"

# Initialize local AI components
# This loads a tiny, 100% offline 40MB math model directly into Python memory
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
llm = Ollama(model="phi3", temperature=0.1)

def index_pdfs():
    """Reads all PDFs in the data folder and saves them into an offline database"""
    documents = []
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        
    for file in os.listdir(DATA_DIR):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(DATA_DIR, file))
            documents.extend(loader.load())
            
    if not documents:
        return False

    # Split long text into small, readable chunks for the CPU
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)
    
    # Store text math vectors inside your laptop disk
    Chroma.from_documents(texts, embeddings, persist_directory=DB_DIR)
    return True

def query_knowledge_base(user_question):
    """Searches the local database and answers using the offline AI"""
    if os.path.exists(DB_DIR) and len(os.listdir(DATA_DIR)) > 0:
        db = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)
        retriever = db.as_retriever(search_kwargs={"k": 2})
        
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm, 
            chain_type="stuff", 
            retriever=retriever
        )
        
        system_prompt = f"System Command: You are an NDLEA tactical assistant. Answer concisely using ONLY the provided document details. Query: {user_question}"
        return qa_chain.run(system_prompt)
    else:
        return "System Warning: No documents have been indexed yet. Please drop a PDF into the data folder and click index."