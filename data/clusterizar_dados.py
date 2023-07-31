import pandas as pd
from sklearn.cluster import KMeans

def clusterizar_dados(data, n_clusters):
    # Aplicar o algoritmo K-means
    kmeans = KMeans(n_clusters=n_clusters, n_init=10)
    data['cluster'] = kmeans.fit_predict(data)
    return data


df = pd.read_parquet('data/dataset_renomeado.parquet')

colunas_deletar = ['id_ncontro', 'id_paciente', 'id_hospital','id_uti']
df = df.drop(columns=colunas_deletar)

df = df[['ventilado_apache','probabilidade_morte_na_uti_(apache_4a)', 'd1_frequencia_cardiaca_maxima','d1_frequencia_cardiaca_minima', 'h1_frequencia_respiratoria_maxima','d1_spO2_minimo','d1_temperatura_minima', 'morte_hospital']]
df = df.dropna()

#calculado a partir do arquivo determinando_n_clusters(elbow)
n_clusters = 2

data = clusterizar_dados(df, n_clusters)

print(data)
