import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("/Users/cesar/My_projects/Sprint7_repo-1/vehicles_us.csv")

# Encabezado de la aplicación
st.header("Análisis de Datos de Vehículos en Venta")

# Sección para histogramas
st.subheader("Distribución de Precios y Años de Modelo")

col1, col2 = st.columns(2)

with col1:
    if st.button("Mostrar Histograma de Precios"):
        fig = px.histogram(df, x='price',
                           title='Distribución de Precios de Vehículos',
                           labels={'price': 'Precio ($)'},
                           nbins=50)
        fig.update_layout(bargap=0.1)
        st.write("Distribución de precios de los vehículos en el dataset:")
        st.plotly_chart(fig, use_container_width=True)

with col2:
    if st.button("Mostrar Histograma de Años de Modelo"):
        fig = px.histogram(df, x='model_year',
                           title='Distribución de Años de Modelo',
                           labels={'model_year': 'Año del Modelo'},
                           nbins=30)
        st.write("Distribución de años de modelo de los vehículos:")
        st.plotly_chart(fig, use_container_width=True)
