from dicionario_dados import dic
from corr import pagina
from app_clusterizacao import cluster

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")



def carregar_dados():
    dados = pd.read_parquet('/home/bianka/PISI3_2022.2/data/dataset_streamlit.parquet')
    return dados


def home():
    
    dados = carregar_dados()

    st.header('Análise Exploratória de Dados')

    # Variáveis quantitativas
    st.subheader('Variáveis Quantitativas')
    quantitativas = dados.select_dtypes(include=['int', 'float'])
    st.dataframe(quantitativas.describe())

    # Variáveis qualitativas
    st.subheader('Variáveis Qualitativas')
    qualitativas = dados.select_dtypes(include=['object'])
    st.dataframe(qualitativas.describe())

    # Gráficos interativos
    st.header('Gráficos Interativos')

    # Gráfico de barras para variáveis qualitativas
    st.subheader('Gráfico de Barras (Variáveis Qualitativas)')
    coluna_qualitativa = st.selectbox('Selecione uma coluna qualitativa', qualitativas.columns)
    contagem_qualitativa = dados[coluna_qualitativa].value_counts()
    fig_bar_qualitativa = px.bar(x=contagem_qualitativa.index, y=contagem_qualitativa.values)
    st.plotly_chart(fig_bar_qualitativa)

    # Gráfico de histograma para variáveis quantitativas
    st.subheader('Histograma (Variáveis Quantitativas)')
    coluna_quantitativa = st.selectbox('Selecione uma coluna quantitativa', quantitativas.columns)
    fig_hist_quantitativa = px.histogram(dados, x=coluna_quantitativa, nbins=30)
    st.plotly_chart(fig_hist_quantitativa)

    # Gráfico de dispersão com marcação de cores para variáveis quantitativas e qualitativas
    st.subheader('Gráfico de Dispersão (Quantitativas x Qualitativas)')
    coluna_x = st.selectbox('Selecione uma coluna quantitativa para o eixo X', quantitativas.columns)
    coluna_y = st.selectbox('Selecione uma coluna quantitativa para o eixo Y', quantitativas.columns)
    coluna_cor = st.selectbox('Selecione uma coluna qualitativa para a cor', qualitativas.columns)

    fig_scatter = px.scatter(dados, x=coluna_x, y=coluna_y, color=coluna_cor)
    st.plotly_chart(fig_scatter)


pages = {
    'Página 1 - Introdução': home,
    'Página 2 - Dicionário': dic,
    'Página 3 - Correlação/grafico de correlação' : pagina,
    'Página 4 - Custerização' : cluster,
    #'Página 5 - Primeira Hora de Internamento' : primeira,
    #'Página 6 - Primeiras Vinte Quatro Horas' : vinte_quatro,
}

page = st.sidebar.selectbox('Selecione a página', tuple(pages.keys()))



pages[page]()
