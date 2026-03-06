import streamlit as st

st.write('# escreve algo aí jorge')
mensagem = st.chat_input("Escreva sua mensagem aqui")

st.chat_message('user').write(mensagem)

print(mensagem)


