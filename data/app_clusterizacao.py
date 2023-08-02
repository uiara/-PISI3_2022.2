
from sklearn.cluster import KMeans
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from clusterizar_dados import clusterizar_dados

# Carregando o dataset 
df = pd.read_parquet('dataset_renomeado.parquet')

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

# Obtenha as colunas disponíveis no dataset
available_columns = df.columns.tolist()

# Interface para selecionar as colunas para as features
st.sidebar.title("Selecione as colunas para as features")
selected_columns = st.sidebar.multiselect("Colunas", available_columns)

if len(selected_columns) == 0:
    st.warning("Por favor, selecione pelo menos 2 coluna.")
    
else:
    
    # Obtenha os dados selecionados pelo usuário
    data_selected = df[selected_columns]

    # Execute o algoritmo K-means para clusterização
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    data_selected['cluster'] = kmeans.fit_predict(data_selected)

    # Cores para os clusters
    colors = ['red', 'green', 'blue', 'orange', 'purple']

    # Criar o gráfico de dispersão
    plt.figure(figsize=(10, 6))
    for i in range(n_clusters):
        cluster_data = data_selected[data_selected['cluster'] == i]
        plt.scatter(cluster_data.iloc[:, 0], cluster_data.iloc[:, 1], s=50, color=colors[i], label=f'Cluster {i + 1}')

    # Exibir os centróides dos clusters em um marcador especial
    centroids = kmeans.cluster_centers_[:, :2]
    plt.scatter(centroids[:, 0], centroids[:, 1], s=200, color='black', marker='X', label='Centroids')

    # Personalizar o gráfico
    plt.xlabel(selected_columns[0])
    plt.ylabel(selected_columns[1])
    plt.title(f'Clusterização com K-means (n_clusters={n_clusters})')
    plt.legend()
    plt.grid(True)

    # Exibir o gráfico usando Streamlit
    st.pyplot(plt)
    
    # Contador de clusters
    cluster_count = pd.Series(kmeans.labels_).value_counts().sort_index()
    st.subheader("Contador de Clusters")
    st.table(pd.DataFrame({'Cluster': cluster_count.index + 1, 'Quantidade': cluster_count.values}))
    

# Plotando gráficos
#st.subheader('Gráficos dos Clusters')
#plt.figure(figsize=(8, 6))
#sns.scatterplot(data=clusterized_data, x='morte_hospital', y='d1_temperatura_minima', hue='cluster', palette='Set1')
#plt.title('Clusters de acordo com morte_hospital e d1_temperatura_minima')
#st.pyplot(plt)

#plt.figure(figsize=(8, 6))
#sns.scatterplot(data=clusterized_data, x='morte_hospital', y='d1_spO2_minimo', hue='cluster', palette='Set1')
#plt.title('Clusters de acordo com morte_hospital e d1_spO2_minimo')
#st.pyplot(plt)

