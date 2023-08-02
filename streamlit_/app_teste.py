import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans

# Carregar os dados (substitua 'seu_arquivo.csv' pelo nome do arquivo CSV contendo seus dados)
dados = pd.read_parquet('data/dataset_streamlit.parquet')


# Título da aplicação
st.title('Análise de Agrupamento com K-means')

# Selecionar as colunas para a análise de agrupamento usando uma barra de rolagem
colunas_analise = st.multiselect('Selecione as colunas para a análise de agrupamento', list(dados.columns))

# Selecionar o número de clusters usando uma barra de rolagem
num_clusters = st.slider('Selecione o número de clusters', min_value=2, max_value=10, value=4)

if colunas_analise:
    # Realizar a análise de agrupamento
    dados_analise = dados[colunas_analise]

    # Normalizar os dados (opcional, dependendo das características das variáveis)
    # dados_analise = (dados_analise - dados_analise.mean()) / dados_analise.std()

    # Aplicar o algoritmo de agrupamento K-means
    modelo = KMeans(n_clusters=4)  # Defina o número de clusters desejado
    modelo.fit(dados_analise)
    dados['grupo'] = modelo.labels_

    # Visualizar os grupos usando Plotly
    fig = px.scatter_3d(dados, x=colunas_analise[0], y=colunas_analise[1], z=colunas_analise[2], color='grupo')
    st.plotly_chart(fig)