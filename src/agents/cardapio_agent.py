from langchain.chains import RetrievalQA
from src.models.llm import load_llm
from src.vectorstore.indexer import load_vectorstore
from src.prompts.cardapio_prompt import get_prompt

def build_cardapio_agent():
    retriever = load_vectorstore().as_retriever(search_type="similarity", search_kwargs={"k": 5})
    llm = load_llm()
    prompt = get_prompt()
 
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )
    return chain
