import pandas as pd
import numpy as np

df = pd.read_parquet('data/dataset_renomeado.parquet')

colunas_deletar = ['id_ncontro', 'id_paciente', 'id_hospital','id_uti']
df = df.drop(columns=colunas_deletar)

df = df[['ventilado_apache', 'd1_frequencia_cardiaca_maxima', 'h1_frequencia_respiratoria_maxima', 'morte_hospital']]
df = df.dropna()

import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Pré-processamento (normalização dos dados)
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# Lista para armazenar os valores da inércia
inertia_values = []

# Número máximo de clusters que você deseja testar (por exemplo, de 1 a 10 clusters)
max_clusters = 10

# Realizar o K-Means para diferentes valores de K e calcular a inércia
for k in range(1, max_clusters+1):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df_scaled)
    inertia_values.append(kmeans.inertia_)

# Criar o gráfico interativo usando o Plotly
fig = px.line(x=range(1, max_clusters+1), y=inertia_values, title='Método do Cotovelo para Encontrar o Número Ideal de Clusters')
fig.update_layout(xaxis_title='Número de Clusters (K)', yaxis_title='Inércia')
fig.show()

import plotly.express as px
import plotly.graph_objects as go
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# Pré-processamento (normalização dos dados)
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# Número de clusters escolhido com base no Método do Cotovelo
numero_clusters_escolhido = 5

# Executar o K-Means com o número de clusters escolhido
kmeans_escolhido = KMeans(n_clusters=numero_clusters_escolhido, random_state=42)
kmeans_escolhido.fit(df_scaled)

# Adicionar as previsões de cluster de volta ao DataFrame original
df['Cluster'] = kmeans_escolhido.labels_

# Criar o gráfico interativo utilizando o Plotly
fig = px.scatter(df, x='morte_hospital', y='Cluster', color='Cluster', title='Clusterização com K-Means')
fig.show()
