import pandas as pd
import plotly.express as px
import streamlit as st

# Lendo os dados
car_data = pd.read_csv('vehicles.csv') # Lendo o CSV na raiz

# Criando um cabeçalho
st.header('Análise de Vendas de Veículos Usados')
st.write('Bem-vindo ao dashboard interativo de anúncios de carros!')

# Criando caixas de seleção interativas
build_histogram = st.checkbox('Criar um histograma')
build_scatter = st.checkbox('Criar um gráfico de dispersão')

# Lógica do Histograma
if build_histogram:
    st.write('Criando um histograma para a coluna odometer...')
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# Lógica do Gráfico de Dispersão
if build_scatter:
    st.write('Criando um gráfico de dispersão relacionando odômetro e preço...')
    # criar um gráfico de dispersão
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_scatter, use_container_width=True)
    