# importo y renombro stremlit
import streamlit as st
import groq
st.set_page_config(page_title='CHAT GPT BY JU', page_icon="🤨")
MODELOS = ['llama3-8b-8192', 'llama3-70b-8192']
#configurar pagina
def configurar_pagina():
    st.title('BIENVENIDO')

#Crear un cliente
def crear_cliente_groq():
    groq_api_key = st.secrets['GROQ_API_KEY']    
    return groq.Groq(api_key=groq_api_key)

#mostrar la barra lateral
def mostrar_sidebar():
    st.sidebar.title('elegi tu modelo favorito')
    modelo = st.sidebar.selectbox('',MODELOS,index=0)
    st.write(f'**Elegiste el modelo{modelo}**')
    return modelo


#inicializar el estado del chat
def inicializar_estado_chat():
    if "mensajes" not in st.session_state:
        st.session_state.mensajes =  [] #lista


#mostrar mensajes ´revios
def obtener_mensajes_previos():
    for mensaje in st.session_state.mensajes:
        with st.chat_message(mensaje['role']):
            st.markdown(mensaje["content"])

#obtener mensaje usuario
def obtener_mensaje_usuario():
    return st.chat_input("escribe tu mensaje")


#guardar los mensajes
def agregar_mensajes_previos(role, content):
    st.session_state.mensajes.append({"role": role, "content":content})

#mostrar los mensajes en pantalla
def mostrar_mensaje(role, content):
    with st.chat_message(role):
        st.markdown(content)

#creacion del modelo de groq
def ejecutar_chat():
    cliente = crear_cliente_groq()
    modelo = mostrar_sidebar()

    inicializar_estado_chat()
    mensaje_usuario = obtener_mensaje_usuario()
    obtener_mensajes_previos()
    

    if mensaje_usuario:
        agregar_mensajes_previos("user",mensaje_usuario)
        mostrar_mensaje("user",mensaje_usuario)

        respuesta_contenido = obtener_respuestas_modelo(cliente, modelo, st.session_state.
        mensajes )
        agregar_mensajes_previos("assistant", respuesta_contenido)
        mostrar_mensaje("assistant",respuesta_contenido)


#llamar al modelo del groq
def obtener_respuestas_modelo(cliente, modelo, mensaje):
    respuesta = cliente.chat.completions.create(
        model = modelo,
        messages=mensaje,
        stream=False 

    )
    return respuesta.choices[0].message.content




#EJECUTAR APP
if __name__ == '__main__':
    ejecutar_chat()  
    

                









