import streamlit as st
import pandas as pd
from pickle import load
import base64

# Cargar el modelo
model_path = "../models/model_randomforestclasiffier_42_sin_scal.sav"
with open(model_path, 'rb') as f:
    model = load(f)

# CSS para ajustar el ancho del contenedor y agregar una imagen de fondo
config_inic = f'''
<style>
.container {{
    max-width: 1000px;
    margin: auto;
    padding: 20px;
    border-radius: 10px;
           
}}
.title {{
    text-align: left;
    white-space: nowrap;
}}
.prediction {{
    color: orange;
    font-weight: bold;
    font-size: 20px;
{{        
</style>
'''
st.markdown(config_inic, unsafe_allow_html=True)


# Contenedor principal
with st.container():
    st.markdown("<h2 class='title'>Predicción Severidad de Accidentes Viales USA</h2>", unsafe_allow_html=True)
    st.write("<p style='color: gray;'>Introducir Valores (Características Tomadas de DataSet Accidentes Viales 2020)</p>", unsafe_allow_html=True)

    lat = st.number_input("Latitud. Min=24 / Max=50", format="%.6f", min_value=24.000000, max_value=50.000000, value=24.000000, step=0.000001)
    lng = st.number_input("Longitud. Min=-125 / Max=-68", format="%.6f", min_value=-125.000000, max_value=-68.000000, value=-125.000000, step=0.000001)
    temp = st.number_input("Temperatura (F). Min=0 / Max=110 ", format="%.2f", min_value=0.00, max_value=110.00, value=0.00, step=0.01)
    hmd = st.number_input("Humedad (%). Min=0 / Max=100", format="%.2f", min_value=0.00, max_value=100.00, value=0.00, step=0.01)

    st.markdown("<p style='color: black;'>Semáforo Cercano (Traffic_Signal_n):</p>", unsafe_allow_html=True)
    semaforo = st.radio("Selecciona una opción para Semáforo Cercano:", ["Sí", "No"],
                         key="semaforo", label_visibility="collapsed")
    sem = 1 if semaforo == "Sí" else 0

    st.markdown("<p style='color: black;'>Crepúsculo Noche (Civil_Twilight_n):</p>", unsafe_allow_html=True)
    crepusculo = st.radio("Selecciona una opción para Crepúsculo Noche:", ["Sí", "No"],
                         key="crepusculo", label_visibility="collapsed")
    crep = 1 if crepusculo == "Sí" else 0

    #st.write(f"Semáforo Cercano: {sem}")
    #st.write(f"Crepúsculo Noche: {crep}")

    if st.button("Predecir"):
        data = pd.DataFrame([[float(lat), float(lng), int(sem), int(crep), float(temp), float(hmd)]], 
                            columns=['Start_Lat', 'Start_Lng', 'Traffic_Signal_n', 'Civil_Twilight_n',
                                     'Temperature(F)', 'Humidity(%)'])

        st.write("Datos de Entrada:", data)

        prediction = model.predict(data)[0]
        pred_class = f"{prediction:.0f}"

        st.write(f"<p class='prediction'>La Predicción de la Severidad es: {pred_class}</p>", unsafe_allow_html=True)
