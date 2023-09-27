from path import load_data
from dicionario_dados import dic
from corr import pagina
from app_clusterizacao import cluster
from analise_grupos import grupos
from st_knn import knn
from DecisionTree import DecisionTree

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")

def home():
    
    dados = load_data()

    st.header('Análise Exploratória de Dados')

    st.subheader('Variáveis Quantitativas')
    quantitativas = dados.select_dtypes(include=['int', 'float'])
    st.dataframe(quantitativas.describe())

    st.subheader('Variáveis Categóricas')
    categoricas = dados.select_dtypes(include=['object'])
    st.dataframe(categoricas.describe())

    # Gráficos interativos
    st.header('Gráficos Interativos')

    # Gráfico de barras para variáveis categoricas
    with st.expander("Gráfico de Barras"):
        st.subheader('Gráfico de Barras (Variáveis Categóricas)')
        coluna_qualitativa = st.selectbox('Selecione uma coluna qualitativa', categoricas.columns)
        contagem_qualitativa = dados[coluna_qualitativa].value_counts()
        fig_bar_qualitativa = px.bar(x=contagem_qualitativa.index, y=contagem_qualitativa.values)
        st.plotly_chart(fig_bar_qualitativa)

    # Gráfico de histograma para variáveis quantitativas
    with st.expander("Histograma"):
        st.subheader('Histograma (Variáveis Quantitativas)')
        coluna_quantitativa = st.selectbox('Selecione uma coluna quantitativa', quantitativas.columns)
        fig_hist_quantitativa = px.histogram(dados, x=coluna_quantitativa, nbins=30)
        st.plotly_chart(fig_hist_quantitativa)

    # Gráfico boxplot

    with st.expander("Boxplot"):
        st.subheader('Boxplot')
        grupo_selecionado = st.selectbox('Selecione o Grupo', list(dados.keys()))
        fig = go.Figure()
        fig.add_trace(go.Box(y=dados[grupo_selecionado], name=grupo_selecionado))
        fig.update_layout(title='Boxplot', yaxis_title='Valores')
        st.plotly_chart(fig)

    with st.expander("Gráfico de Dispersão"):
        # Gráfico de dispersão com marcação de cores para variáveis quantitativas e categoricas
        st.subheader('Gráfico de Dispersão (Quantitativas x Categóricas)')
        coluna_x = st.selectbox('Selecione uma coluna quantitativa para o eixo X', quantitativas.columns)
        coluna_y = st.selectbox('Selecione uma coluna quantitativa para o eixo Y', quantitativas.columns)
        coluna_cor = st.selectbox('Selecione uma coluna qualitativa para a cor', categoricas.columns)
        fig_scatter = px.scatter(dados, x=coluna_x, y=coluna_y, color=coluna_cor)
        st.plotly_chart(fig_scatter)

    with st.expander("Gráfico de Bolha"):

        st.title('Análise Dinâmica por Faixa Etária')

        categorical_columns = dados.select_dtypes(include=['object']).columns
        numeric_columns = dados.select_dtypes(include=['number']).columns

        categorical_column = st.selectbox('Selecione a Coluna Categórica:', categorical_columns)

        numeric_column = st.selectbox('Selecione a Coluna Numérica:', numeric_columns)

        age_bins = [0, 30, 40, 50, 60, 70, 80, float('inf')]
        age_labels = ['0-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80+']

        # Atribua cada valor de idade a um intervalo e crie uma nova coluna 'faixa_etaria'
        dados['faixa_etaria'] = pd.cut(dados['idade'], bins=age_bins, labels=age_labels)

        # Agrupa e agrega os dados com base na coluna categórica escolhida e nas faixas etárias
        df_grouped = dados.groupby([categorical_column, 'faixa_etaria']).mean().reset_index()
        df_grouped['contagem'] = dados.groupby([categorical_column, 'faixa_etaria']).count().reset_index()['morte_hospital']

        fig = px.scatter(df_grouped, x="faixa_etaria", y=numeric_column, size="contagem", color=categorical_column,
                        hover_name=categorical_column, log_x=False, size_max=60)
        fig.update_layout(title_text=f"<b>{numeric_column} por Faixa Etária<b>")
        fig.update_yaxes(title_text=f"<b>{numeric_column}<b>")
        fig.update_xaxes(title_text="<b>Faixa Etária<b>")

        st.plotly_chart(fig)


pages = {
    'Página 1 - Introdução': home,
    'Página 2 - Dicionário': dic,
    'Página 3 - Correlação/grafico de correlação' : pagina,
    'Página 4 - Análise em Conjuntos' : grupos,
    'Página 5 - Clusterização' : cluster,
    'Página 6 - KNN' : knn,
    'Página 7 - DecisionTree' : DecisionTree,
}

page = st.sidebar.selectbox('Selecione a página', tuple(pages.keys()))



pages[page]()
