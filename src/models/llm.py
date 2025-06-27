from langchain.chat_models import ChatOpenAI

def load_llm():
    """
    Retorna o modelo de linguagem (LLM) configurado com GPT-4o da OpenAI.
    """
    return ChatOpenAI(
        model_name="gpt-4o",
        temperature=0,
        max_tokens=512
    )
