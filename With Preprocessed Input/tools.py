import os
import json
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains import RetrievalQA
import hashlib

def compute_file_hash(file_path):
    """Compute a hash for the contents of a file."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def create_vector_database(json_file_path):
    """Create a vector database using ChromaDB with Ollama embeddings."""
    ollama_embeddings = OllamaEmbeddings(model="llama3.2")
    persist_directory = "db"

    if os.path.exists(persist_directory) and os.path.exists(json_file_path):
        new_hash = compute_file_hash(json_file_path)
        hash_file = os.path.join(persist_directory, "data_hash.txt")
        if os.path.exists(hash_file):
            with open(hash_file, 'r') as f:
                existing_hash = f.read()
            if existing_hash == new_hash:
                print("No changes detected in data. Using existing embeddings.")
                return Chroma(persist_directory=persist_directory, embedding_function=ollama_embeddings)

    with open(json_file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    documents = [
        Document(page_content=item["content"], metadata={"title": item["title"], "url": item["url"]})
        for item in data
    ]
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=40)
    docs = text_splitter.split_documents(documents)

    vectordb = Chroma.from_documents(documents=docs, embedding=ollama_embeddings, persist_directory=persist_directory)
    vectordb.persist()

    new_hash = compute_file_hash(json_file_path)
    with open(os.path.join(persist_directory, "data_hash.txt"), 'w') as f:
        f.write(new_hash)

    return vectordb

def setup_retriever(vector_database):
    """Setup a retriever using the vector database."""
    return vector_database.as_retriever(search_kwargs={"k": 3})

def build_chatbot(retriever):
    """Build a chatbot using Ollama LLM."""
    llm = Ollama(model="llama3.2")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    return qa_chain