import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Anuncio de ventas de coches en USA') # crear un encabezado
hist_button = st.button('Construir histograma') # crear un botón
     
if hist_button: # al hacer clic en el botón

    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')  # escribir un mensaje
         
    fig = px.histogram(car_data, x='odometer', title='Distribución de Kilometraje - Odómetro')  # crear un histograma
     
    st.plotly_chart(fig, use_container_width=True)  # mostrar un gráfico plotly interactivo


build_scatter = st.checkbox('Construir un diagrama de dispersión - Kilometraje vs Precio')  # crear una casilla de verificación

if build_scatter:       # si la casilla de verificación está seleccionada
    st.write('Creación de un diagrama de dispersión, relación entre distancia y precio')  # escribir un mensaje

    fig_scatter = px.scatter(car_data, x='odometer', y='price', title='Diagrama de dispersión de la relación kilometraje y precio', hover_data=['model', 'model_year'])  # crear un diagrama de dispersión

    st.plotly_chart(fig_scatter, use_container_width=True)

st.write('Ahora se puede analizar los datos observando los gráficos')