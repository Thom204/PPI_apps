import streamlit as st

# Título de la app
st.title("Mi primera app")

# Autor de la app
st.write("Esta app fue elaborada por Thomas Monnier Granda.")

# Preguntar el nombre del usuario
nombre_usuario = st.text_input("Ingresa tu nombre")

# Si el usuario ha ingresado un nombre, mostrar el mensaje de bienvenida
if nombre_usuario:
    mensaje = f"{nombre_usuario}, te doy la bienvenida a mi primera app."
    st.write(mensaje)
