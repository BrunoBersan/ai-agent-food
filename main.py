import streamlit as st
from src.agents.cardapio_agent import build_cardapio_agent
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis de ambiente (.env)

st.set_page_config(page_title="Assistente de Cardápio", page_icon="🍽️")

st.title("🍽️ Quer uma ajuda?")
st.write("Faça perguntas sobre o cardápio, e eu te responderei com base nas informações cadastradas.")
user_question = st.text_input("Digite sua pergunta sobre o cardápio:")

# Inicializa o agente só uma vez
@st.cache_resource
def get_agent():
    return build_cardapio_agent()

agent = get_agent()

if st.button("Perguntar"):
    if not user_question.strip():
        st.warning("Por favor, digite uma pergunta.")
    else:
        with st.spinner("Pensando..."):
            # AQUI ESTÁ A MUDANÇA PRINCIPAL:
            # Use .invoke() e acesse a chave 'result'
            response = agent.invoke({"query": user_question})
            result_text = response.get('result', 'Não foi possível obter uma resposta.')
            source_docs = response.get('source_documents', []) # Opcional: para exibir as fontes

            st.success("Resposta:")
            st.write(result_text)