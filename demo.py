import streamlit as st
from PIL import Image

# Variables con la imagen y el texto LaTeX
image_path = "example.jpg"  # Reemplázalo con la ruta de tu imagen
latex_text = r"E = mc^2"  # Ejemplo de texto en LaTeX

# Cargar la imagen
image = Image.open(image_path)

# Interfaz en Streamlit
st.title("Visor de Imagen con LaTeX")

# Mostrar imagen
st.image(image, caption="Imagen de ejemplo", use_column_width=True)

# Mostrar texto en LaTeX
st.latex(latex_text)

# Agregar opción para cambiar el texto
new_latex_text = st.text_input("Escribe una nueva ecuación LaTeX:", value=latex_text)

# Mostrar el nuevo texto si cambia
if new_latex_text:
    st.latex(new_latex_text)
