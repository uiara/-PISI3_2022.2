import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


df = pd.read_parquet('data/dataset_renomeado.parquet')

colunas_deletar = ['id_ncontro', 'id_paciente', 'id_hospital','id_uti']
df = df.drop(columns=colunas_deletar)

df = df[['ventilado_apache','idade','imc' ,'d1_frequencia_cardiaca_maxima', 'h1_frequencia_respiratoria_maxima', 'morte_hospital']]
df = df.dropna()

import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)


inertia_values = []


max_clusters = 10

for k in range(1, max_clusters+1):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df_scaled)
    inertia_values.append(kmeans.inertia_)

fig = px.line(x=range(1, max_clusters+1), y=inertia_values, title='Método do Cotovelo para Encontrar o Número Ideal de Clusters')
fig.update_layout(xaxis_title='Número de Clusters (K)', yaxis_title='Inércia')
fig.show()


scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

numero_clusters_escolhido = 5

kmeans_escolhido = KMeans(n_clusters=numero_clusters_escolhido, random_state=42)
kmeans_escolhido.fit(df_scaled)

df['Cluster'] = kmeans_escolhido.labels_

fig = px.scatter_3d(df, z='imc', y='idade',
                     x='morte_hospital',
                     color='morte_hospital',
                     title='Clusterização com K-Means')
fig.show()
