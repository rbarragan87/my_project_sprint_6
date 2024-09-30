import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar de datos
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

# Crear el encabezado
st.header('Vehicles_US')

# Crear casillas de verificación

mostrar_histograma = st.checkbox('Mostrar Histograma')
mostrar_dispersion = st.checkbox('Mostrar Diagrama de Dispersión')

if mostrar_histograma:
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_with=True)

if mostrar_dispersion:
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_with=True)

