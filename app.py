import streamlit as st
import pandas as pd
import plotly_express as px
car_data = pd.read_csv("C:/Users/mora_/OneDrive/Documentos/Bootcamp Tripleten/Actividades DA-42/Proyecto Sprint 7/Proyecto_Sprint_7/vehicles_us.csv")
st.header('Venta de Coches - EEUU')

hist_button = st.button('Construir histograma') # crear un botón
     
if hist_button: # al hacer clic en el botón
         # escribir un mensaje
         st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
         fig = px.histogram(car_data, x="model")
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig, use_container_width=True)

graph_button = st.button('Construir gráfico de dispersión') # crear un botón
     
if graph_button: # al hacer clic en el botón
         # escribir un mensaje
         st.write('Creación de un gráfico de dispesión para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
         fig = px.scatter(car_data, x="model")
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig, use_container_width=True)