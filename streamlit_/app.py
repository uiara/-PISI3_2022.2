from path import load_data
from dicionario_dados import dic
from corr import pagina
from analise_grupos import grupos
from st_knn import knn
from DecisionTree import DecisionTree
from gradientboosting import gradient
from naive import nav
from progresso_dataset import progresso

import streamlit as st
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")

def home():

    folder_path = "../data"
    dataset_names = {
        "Dataset Original": "dataset.parquet",
        "Dataset Renomeado": "dataset_renomeado.parquet",
        "Dataset sem Valores Nulos": "dataset_renomeado_sem_nulos.parquet",
        "Dataset sem Valores Nulos e Aplicação do One Hot": "dataset_renamed_onehot_nonull.parquet",
        "Dataset sem Valores Nulos com Aplicação do One Hot Prenchido pela Média": "renomeado_media_onehot.parquet",
        "Dataset sem Valores Nulos com Aplicação do One Hot Prenchido pela Média e Balanceamento com SMOTEENN": "renomeado_media_smoteenn.parquet",
        "Dataset sem Valores Nulos com Aplicação do One Hot Prenchido pela Mediana": "renomeado_mediana_onehot.parquet",
        "Dataset sem Valores Nulos com Aplicação do One Hot Prenchido pela Mediana e Balanceamento com SMOTEENN": "renomeado_mediana_smoteenn.parquet",
    }

    st.title("Análise de Arquivos Parquet")

    if os.path.isdir(folder_path):
        file_paths = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".parquet"):
                    file_paths.append(os.path.join(root, file))

        st.write("Aqui estão todos os datasets disponíveis para visualização. No entanto, é importante observar que nos datasets em que a técnica One Hot foi aplicada, não é possível apresentar gráficos que dependam de dados categóricos.")
        selected_file_index = st.selectbox("Selecione um arquivo para análise:", list(dataset_names.keys()))

        selected_file_name = list(dataset_names.keys())[list(dataset_names.values()).index(dataset_names[selected_file_index])]

        selected_file_path = dataset_names[selected_file_name]

        dados = pd.read_parquet(os.path.join(folder_path, selected_file_path))

    st.header('Análise Exploratória de Dados')

    st.subheader('Variáveis Quantitativas')
    quantitativas = dados.select_dtypes(include=['int', 'float'])
    st.dataframe(quantitativas.describe())

    st.subheader('Variáveis Categóricas')
    categoricas = dados.select_dtypes(include=['object'])

    if not categoricas.empty:
        st.dataframe(categoricas.describe())
    else:
        st.write("Este dataset não contém variáveis categóricas. Portanto, os gráficos que dependem dessas variáveis não serão exibidos.")
    
    st.header('Gráficos Interativos')

    with st.expander("Histograma"):
        st.subheader('Histograma (Variáveis Quantitativas)')
        coluna_quantitativa = st.selectbox('Selecione uma coluna quantitativa', quantitativas.columns)
        fig_hist_quantitativa = px.histogram(dados, x=coluna_quantitativa, nbins=30)
        st.plotly_chart(fig_hist_quantitativa)


    with st.expander("Gráfico de Barras"):
        st.subheader('Gráfico de Barras (Variáveis Categóricas)')
        coluna_qualitativa = st.selectbox('Selecione uma coluna categóricas', categoricas.columns)
        contagem_qualitativa = dados[coluna_qualitativa].value_counts()
        fig_bar_qualitativa = px.bar(x=contagem_qualitativa.index, y=contagem_qualitativa.values)
        st.plotly_chart(fig_bar_qualitativa)
    
    with st.expander("Boxplot"):
        st.subheader('Boxplot')
        grupo_selecionado = st.selectbox('Selecione o Grupo', list(dados.keys()))
        fig = go.Figure()
        fig.add_trace(go.Box(y=dados[grupo_selecionado], name=grupo_selecionado))
        fig.update_layout(title='Boxplot', yaxis_title='Valores')
        st.plotly_chart(fig)

    with st.expander("Gráfico de Dispersão"):
        st.subheader('Gráfico de Dispersão (Quantitativas x Categóricas)')
        coluna_x = st.selectbox('Selecione uma coluna quantitativa para o eixo X', quantitativas.columns)
        coluna_y = st.selectbox('Selecione uma coluna quantitativa para o eixo Y', quantitativas.columns)
        coluna_cor = st.selectbox('Selecione uma coluna categóricas para a cor', categoricas.columns)
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

        dados['faixa_etaria'] = pd.cut(dados['idade'], bins=age_bins, labels=age_labels)

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
    'Página - ': progresso,
    'Página 3 - Correlação/grafico de correlação' : pagina,
    'Página 4 - Análise em Conjuntos' : grupos,
    'Página 5 - KNN' : knn,
    'Página 6 - Árvore de Decisão' : DecisionTree,
    'Página 7 - Gradient Boosting' : gradient,
    'Página 8 - Naive Bayes' : nav
}

page = st.sidebar.selectbox('Selecione a página', tuple(pages.keys()))



pages[page]()
