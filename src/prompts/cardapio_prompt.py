from langchain.prompts import PromptTemplate

def get_prompt():
    template = """
Você é um assistente de atendimento de restaurante. Use as informações abaixo sobre o cardápio para responder à pergunta do cliente.

Contexto:
{context}

Pergunta:
{question}

Resposta útil e educada:
"""

    return PromptTemplate(
        input_variables=["context", "question"],
        template=template.strip()
    )
