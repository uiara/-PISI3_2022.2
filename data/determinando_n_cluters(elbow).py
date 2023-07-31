import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Calcular a soma dos erros quadrados dentro dos clusters (SSE) para cada valor:
def find_optimal_clusters(data, max_clusters):
    sse = []
    for n_clusters in range(1, max_clusters+1):
        kmeans = KMeans(n_clusters=n_clusters, n_init=10)  # setar o n_init para evitar erro de versao
        kmeans.fit(data)
        sse.append(kmeans.inertia_)
    return sse

# carregar dataset
df = pd.read_parquet('data/dataset_renomeado.parquet')

colunas_deletar = ['id_ncontro', 'id_paciente', 'id_hospital','id_uti']
df = df.drop(columns=colunas_deletar)

df = df[['ventilado_apache','probabilidade_morte_na_uti_(apache_4a)', 'd1_frequencia_cardiaca_maxima','d1_frequencia_cardiaca_minima', 'h1_frequencia_respiratoria_maxima','d1_spO2_minimo','d1_temperatura_minima', 'morte_hospital']]
df = df.dropna()

# Maximo de clusters para tentar
max_clusters = 10

# achando o SSE para diferentes numeros de clusters
sse_values = find_optimal_clusters(df, max_clusters)

# plot do grafico de cotovelo
plt.figure(figsize=(8, 6))
plt.plot(range(1, max_clusters+1), sse_values, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('SSE (Sum of Squared Errors)')
plt.title('Elbow Method to Determine the Number of Clusters')
plt.show()

#O número ideal de clusters é geralmente escolhido no ponto em que a curva começa a nivelar
#formando um "cotovelo". Esse ponto indica que adicionar mais clusters não levará a uma redução significativa na SSE
#sugerindo que o número de clusters encontrado nesse ponto é uma escolha razoável.
