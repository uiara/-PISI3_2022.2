from sklearn.cluster import KMeans
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from clusterizar_dados import clusterizar_dados

# Carregando o dataset 
df = pd.read_parquet('C:/Users/A/Documents/PISI3_2022.2/data/dataset_renomeado.parquet')

df = df[['ventilado_apache','probabilidade_morte_na_uti_(apache_4a)', 'd1_frequencia_cardiaca_maxima','d1_frequencia_cardiaca_minima', 'h1_frequencia_respiratoria_maxima','d1_spO2_minimo','d1_temperatura_minima', 'morte_hospital']]
df = df.dropna()
def cluster():

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

        # Gráfico de dispersão 2D usando Plotly Express
        fig_2d = px.scatter(data_selected, x=data_selected.columns[0], y=data_selected.columns[1],
                            color=data_selected['cluster'].astype(str), title=f'Clusterização com K-means (2D)',
                            labels={'cluster': 'Cluster'}, color_discrete_sequence=px.colors.qualitative.Plotly)
        st.plotly_chart(fig_2d)

        # Gráfico de dispersão 3D usando Plotly Express
        if len(selected_columns) >= 3:
            fig_3d = px.scatter_3d(data_selected, x=data_selected.columns[0], y=data_selected.columns[1],
                                z=data_selected.columns[2], color=data_selected['cluster'].astype(str),
                                title=f'Clusterização com K-means (3D)', labels={'cluster': 'Cluster'},
                                color_discrete_sequence=px.colors.qualitative.Plotly)
            st.plotly_chart(fig_3d)

        
        # Contador de clusters
        cluster_count = pd.Series(kmeans.labels_).value_counts().sort_index()
        st.subheader("Contador de Clusters")
        st.table(pd.DataFrame({'Cluster': cluster_count.index + 1, 'Quantidade': cluster_count.values}))
        
