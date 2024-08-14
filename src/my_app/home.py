import streamlit as st

# Crear tres columnas con proporciones 1:5:1
col1, col2, col3 = st.columns([1, 5, 1])

# Insertar la imagen en la columna del medio
with col2:
    st.image('my_app/portada.png', use_column_width=True)