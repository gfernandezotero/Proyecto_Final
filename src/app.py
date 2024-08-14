import streamlit as st
import base64

# Configurar el modo ancho automáticamente
st.set_page_config(layout="wide")

# Función para cargar la imagen de fondo
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Cargar la imagen de fondo
background_image = get_base64_of_bin_file('my_app/fondo_claro.jpg')

# Aplicar el estilo CSS para la imagen de fondo y los inputs
page_bg_img = f'''
<style>
.stApp {{
  background-image: url("data:image/jpg;base64,{background_image}");
  background-size: initial;
}}
</style>
'''
# background-size: unset;

st.markdown(page_bg_img, unsafe_allow_html=True)


# Definir las páginas
port = st.Page(
    "my_app/home.py", title=" ", icon=":material/home:", default=True)

imp = st.Page(
    "my_app/pages/import.py", title="Importancia del Proyecto", icon=":material/dashboard:")
dat = st.Page(
    "my_app/pages/calidad.py", title="Calidad de los Datos", icon=":material/info:")

corr = st.Page(
    "my_app/pages/corr.py", title="Matriz de Correlación", icon=":material/grade:")

sens_mod = st.Page(
    "my_app/pages/modelos.py", title="Optimización de Modelos", icon=":material/settings:")

mod = st.Page("modelo.py", title="Modelo Desarrollado", icon=":material/model_training:")

# Crear la navegación
pg = st.navigation(
    {
        " ": [port],
        "Insights Proyecto": [imp, dat, corr, sens_mod],
        "Modelo Desarrollado": [mod],
    }
)

# Ejecutar la navegación
pg.run()

