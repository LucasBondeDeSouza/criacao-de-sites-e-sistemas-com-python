import streamlit as st
from openai import OpenAI

modelo = OpenAI(opi_key="")

st.write("### ChatBot com IA")

# Session_state = memoria do streamlit
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# Adicionar uma mensagem 
# st.session_state["lista_mensagens"].append(mensagem)

# Exibir o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

if mensagem_usuario:
    # Exibir a resposta do usuário na tela
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    # Resposta da IA
    resposta_modelo = modelo.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-3.5-turbo"
    )
    resposta_ia = resposta_modelo.choices[0].message.content

    # Exibir a resposta da IA na tela
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)