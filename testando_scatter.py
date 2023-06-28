import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o dataset
#@st.cache_data(allow_output_mutation=True)
def load_data():
    data = pd.read_parquet('data/dataset.parquet')
    return data

# Função para criar o Scatter Plot
@st.cache_data
def create_scatter_plot(x_data, y_data):
    fig = px.scatter(x=x_data, y=y_data)
    return fig

# Carregar o dataset
data = load_data()

# Obter as colunas do dataset
columns = data.columns.tolist()

# Interface para seleção das colunas
x_column = st.sidebar.selectbox("Selecione a coluna para o eixo X", columns)
y_column = st.sidebar.selectbox("Selecione a coluna para o eixo Y", columns)

# Obter os dados para o Scatter Plot
x_data = data[x_column]
y_data = data[y_column]

# Criar o Scatter Plot
fig = create_scatter_plot(x_data, y_data)
st.plotly_chart(fig)
