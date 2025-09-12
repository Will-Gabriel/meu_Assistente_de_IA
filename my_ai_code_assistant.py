# Inmporta módulo para interagir com o sistema operacional
import os

# Importa a biblioteca Streamlit para criar a interface web interativa
import streamlit as st

# Importa a classe Groq para se conectar à API da plataforma Groq e acessar o LLM
from groq import Groq

# configura a página do Streamlit com Título, ione, layout e estado inicial da sidebar
st.set_page_config (
    page_title = "WG AI Coder",
    page_icon = "🤖",
    layout = "wide",
    initial_sidebar_state = "expanded"
)

# Define um prompt de sistema que descreve as regras e comportamento do Assistente de IA
CUSTOM_PROMPT = """
Você é o "WG Ai Coder", um assistente de IA especialista em programação, com foco principal em Python. Sua missão é ajudar desenvolvedore com iniciantes com dúvidas de programação de forma clara, precisa e útil.

REGRAS DE OPERAÇÃO:
1. **Foco em Programação**: Responda apenas as perguntas relacionadas a programação, algoritmos, estruturas de dados, bibliotecas e frameworks. Se o usuário perguntar sobre outro assunto, responda educadamente que seu foco é exclusivo à programação.
2. **Estrutura da Resposta**: Sempre formate suas respostas da seguinte maneira:
    * **Explicação Clara**: Comece com uma explicação conceitual sobre o tópico perguntado, Seja direto e didático.
    * **Exemplo de Código**: Forneça um ou mais blocos de código em Python com a sintaxe correta. O código deve ser bem comentado para explicar as partes importantes.
    * **Detalhes do Código**: Após o bloco de código, descreva em detalhes o que cada parte do código faz, explicando a lógica e as funções utilizadas.
    * **Documentação de Referência**: Ao final, inclua uma seção chamada "📚 Documentação de Referência" com o link direto e relevante para a documentação oficial da Linguagem Python (docs.python.org) ou da biblioteca em questão.
3. **Clareza e Precisão**: Use uma linguagem clara. Evite jarções desnecessários. Suas respostas devem ser tecnicamente precisas.
"""

# Cria o conteúdo da barra lateral no Streamlit
with st.sidebar:
    # define o título da barra lateral
    st.title("🤖 WG AI Coder")

    # Mostra um texto explicativo sobre o assistente
    st.markdown("Assistente de IA focado em programação Python!")

    # Campo para inserir a chave de API da Groq
    groq_api_key = st.text_input (
        "Insira sua API Key Groq",
        tupe = "password",
        help = "Caso ainda não possua sua chave de API, basta criar em https://console.groq.com/keys"
    )

    # Adcionar linha divisória e explicações extras na barra lateral
    st.markdown("---")
    st.markdown("Desenvolvi essa IA para auxiliar você em suas dúvidas de programação com Linguagem Python. Lembre-se que, a IA pode cometer erros. Sempre verifique e teste suas respostas!")

    st.markdown("---")
    st.markdown("Acesse meu LinkedIn e conecte-se comigo!")
    st.markdown("[Linkedin - Wilian Gabriel](https://www.linkedin.com/in/will-gabriel/)", unsafe_allow_html=True)
    # st.markdown('<a href="https://www.linkedin.com/in/will-gabriel/" target="_blank">Acesse meu LinkedIn e conecte-se comigo.</a>',
    # unsafe_allow_html=True)

# Título da Página Principal
st.title("🤖 WG AI Coder")

# Subtitulo adicional
st.title("Seu assistente pessoal de Programação Python 🐍")

# Texto auxiliar abaixo do título
st.caption("Faça sua pergunta sobre a linguagem Python e obtenha código, explicações e referências.")

# Inicializa o histórico de mensagens na sessão, caso ainda não exista
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe todas as mensagens anteriores armazenadas no estado da sessão
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
