# Assistente de Cardápio com GPT-4o

Este projeto implementa um assistente virtual inteligente baseado em LLM (modelo de linguagem de grande escala) da OpenAI, especificamente o **GPT-4o**, para responder a perguntas sobre o cardápio de um restaurante. O sistema foi desenvolvido utilizando **LangChain**, **Streamlit**, e **FAISS** para indexação semântica dos dados.

---

## Objetivo

Criar uma aplicação interativa capaz de compreender e responder dúvidas dos clientes com base nas informações do cardápio fornecido em texto. O foco é demonstrar a aplicação prática de IA generativa e recuperação de contexto (RAG - Retrieval-Augmented Generation).

---

## Arquitetura

O sistema está dividido em três principais componentes:

### 1. **LLM e Cadeia de Resposta (`RetrievalQA`)**
Utiliza-se o `ChatOpenAI` (com o modelo `gpt-4o`) como motor de linguagem, acoplado a um `retriever` semântico (FAISS) que retorna documentos similares ao contexto da pergunta do usuário.

### 2. **Vetorização de Conteúdo**
O conteúdo do cardápio (`cardapio_preparado.txt`) é carregado, dividido em blocos e convertido em vetores utilizando os embeddings da OpenAI. O resultado é indexado com o **FAISS**, uma biblioteca eficiente de busca vetorial.

### 3. **Interface do Usuário**
Desenvolvida com **Streamlit**, a interface oferece um campo de entrada para perguntas, processa a resposta e exibe de forma interativa e responsiva.

---

## Execução

### Pré-requisitos

- Python 3.11
- Chave de API da OpenAI
- Arquivo `.env` com sua chave:
  ```
  OPENAI_API_KEY=sk-...
  ```

### Instalação

```bash
pip install -r requirements.txt
```

### Executar o App

```bash
streamlit run main.py
```

---

## Tecnologias Utilizadas

- **LangChain**: Orquestração da cadeia de LLM + RAG
- **OpenAI GPT-4o**: Modelo de linguagem natural
- **FAISS**: Indexação e busca semântica
- **Streamlit**: Interface web interativa
- **dotenv**: Gerenciamento de variáveis de ambiente

---

## Estrutura do Projeto

```
.
├── app.py                         # Interface com o usuário (Streamlit)
├── requirements.txt
├── .env                           # (não versionado) API Key
└── src/
    ├── agents/
    │   └── cardapio_agent.py      # Construção da cadeia LLM + Retriever
    ├── data/
    │   └── cardapio_preparado.txt # Fonte de dados usada para busca
    ├── models/
    │   └── llm.py                 # Instancia o modelo GPT-4o
    ├── prompts/
    │   └── cardapio_prompt.py     # Template do prompt customizado
    └── vectorstore/
        └── indexer.py             # Indexa e carrega o FAISS
```

---

## Possíveis Extensões

- Adicionar opção de chat contínuo (com histórico de mensagens)
- Suporte a múltiplos cardápios (por restaurante)
- Integração com TTS (text-to-speech) ou comandos por voz
- Deploy em nuvem (Streamlit Cloud, Hugging Face Spaces, etc.)

---

## Sobre

Este projeto foi desenvolvido como exercício prático para aplicação de técnicas modernas de NLP e RAG utilizando LLMs em um cenário real de atendimento ao cliente.

---

## Contato

Em caso de dúvidas ou sugestões, fique à vontade para entrar em contato via [seu-email ou LinkedIn].