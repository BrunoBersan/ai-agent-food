from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import TokenTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import os

INDEX_PATH = "faiss_index"
CARDAPIO_PATH = './data/cardapio_preparado.txt'

def load_vectorstore():
        
        loader = TextLoader('src/data/cardapio_preparado.txt', encoding='utf-8')
        docs = loader.load()
        
        splitter = TokenTextSplitter(chunk_size=300, chunk_overlap=100)
        documents = splitter.split_documents(docs)
        
        embedding_model = OpenAIEmbeddings()
        vectorstore = FAISS.from_documents(documents, embedding_model)
        
        vectorstore.save_local(INDEX_PATH)
        return vectorstore
