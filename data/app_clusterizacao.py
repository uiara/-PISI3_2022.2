import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from clusterizar_dados import clusterizar_dados

# Carregando o dataset 
df = pd.read_parquet('data/dataset_renomeado.parquet')

colunas_deletar = ['id_ncontro', 'id_paciente', 'id_hospital','id_uti']
df = df.drop(columns=colunas_deletar)

df = df[['ventilado_apache','probabilidade_morte_na_uti_(apache_4a)', 'd1_frequencia_cardiaca_maxima','d1_frequencia_cardiaca_minima', 'h1_frequencia_respiratoria_maxima','d1_spO2_minimo','d1_temperatura_minima', 'morte_hospital']]
df = df.dropna()

# Interface do Streamlit
st.title('Aplicação de Clusterização com Streamlit')

# Número de clusters definido pelo usuário
n_clusters = st.sidebar.slider('Selecione o número de clusters:', 2, 10, 2)

# Executando a clusterização
clusterized_data = clusterizar_dados(df, n_clusters)

# Visualização dos dados clusterizados
st.subheader('Dados Clusterizados')
st.write(clusterized_data)

print(df.columns)

# Plotando gráficos
st.subheader('Gráficos dos Clusters')
plt.figure(figsize=(8, 6))
sns.scatterplot(data=clusterized_data, x='morte_hospital', y='d1_temperatura_minima', hue='cluster', palette='Set1')
plt.title('Clusters de acordo com Feature1 e Feature2')
st.pyplot(plt)

plt.figure(figsize=(8, 6))
sns.scatterplot(data=clusterized_data, x='morte_hospital', y='d1_spO2_minimo', hue='cluster', palette='Set1')
plt.title('Clusters de acordo com Feature1 e Feature3')
st.pyplot(plt)
