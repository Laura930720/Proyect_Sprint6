import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar el conjunto de datos
car_data = pd.read_csv('vehicles_us.csv') 

# Mostrar un encabezado
st.header('Análisis de vehículos estadounidenses')



# crear una casilla de verificación
build_histogram1 = st.checkbox('Distancias recorridas (histograma)')
build_histogram2 = st.checkbox('Precios de automóviles/distancia recorrida (gráfico de dispersión)')

if build_histogram1: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma referente al precio de automóviles')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer", color="transmission")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if build_histogram2: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    
    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price", color='fuel')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
       

