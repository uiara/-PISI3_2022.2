import streamlit as st
import plotly_express as px
import pandas as pd

st.title("App de Teste - Visualização de Dados (usando o dataset.csv)")

st.sidebar.subheader("Opções")

def get_clean_data():
    data = pd.read_csv("data/dataset_streamlit_sem_nulos_onehot.csv")
    # Remover colunas irrelevantes
    return data

clean_data = get_clean_data()

# Adicionar amostragem de dados
sampling_fraction = st.slider("Selecione a Fração de Amostragem de Dados", min_value=0.05, max_value=1.0, value=0.5, step=0.01)
sampled_data = clean_data.sample(frac=sampling_fraction, random_state=42)

# Adicionar um botão de rádio para filtrar mortes, sobrevivências, cirurgia eletiva, foi intubado ou não foi intubado
filter_option = st.sidebar.radio("Filtrar por", ("Mostrar Todos", "Mortes", "Sobrevivências", "Cirurgia Eletiva", "Não Cirurgia Eletiva", "Foi Intubado", "Não Foi Intubado"))

if filter_option == "Mostrar Todos":
    filtered_data = sampled_data
elif filter_option == "Mortes":
    filtered_data = sampled_data[sampled_data["morte_hospital"] == 1]
elif filter_option == "Sobrevivências":
    filtered_data = sampled_data[sampled_data["morte_hospital"] == 0]
elif filter_option == "Cirurgia Eletiva":
    filtered_data = sampled_data[sampled_data["cirurgia_eletiva"] == 1]
elif filter_option == "Não Cirurgia Eletiva":
    filtered_data = sampled_data[sampled_data["cirurgia_eletiva"] == 0]
elif filter_option == "Foi Intubado":
    filtered_data = sampled_data[sampled_data["intubado_apache"] == 1]
elif filter_option == "Não Foi Intubado":
    filtered_data = sampled_data[sampled_data["intubado_apache"] == 0]

# Exibir a contagem de mortes, sobrevivências, cirurgia eletiva, foi intubado e não foi intubado
num_deaths = filtered_data["morte_hospital"].sum()
num_survivals = len(filtered_data) - num_deaths
st.write(f"Número de Mortes: {num_deaths}")
st.write(f"Número de Sobrevivências: {num_survivals}")

chart_select = st.sidebar.selectbox(
    label="Selecione o tipo de gráfico",
    options=["Dispersão", "Histograma", "Boxplot", "Heatmap"]
)

colunas_numericas = list(sampled_data.select_dtypes(['float', 'int']).columns)

custom_palette = ['#B76B5D', '#C83030'] 

if chart_select == "Dispersão":
    st.sidebar.subheader("Configurar Dispersão")
    x_values = st.sidebar.selectbox('Eixo X', options=colunas_numericas)
    y_values = st.sidebar.selectbox('Eixo Y', options=colunas_numericas)

    color_discrete_map = {0: custom_palette[0], 1: custom_palette[1]}
    plot = px.scatter(data_frame=filtered_data, x=x_values, y=y_values, color="morte_hospital", color_discrete_map=color_discrete_map)
    st.plotly_chart(plot)

elif chart_select == "Histograma":
    st.sidebar.subheader("Configurar Histograma")
    x_values = st.sidebar.selectbox('Selecione a coluna para o histograma', options=colunas_numericas)
    plot = px.histogram(data_frame=filtered_data, x=x_values, color_discrete_sequence=custom_palette)
    st.plotly_chart(plot)

elif chart_select == "Boxplot":
    st.sidebar.subheader("Configurar Boxplot")
    x_values = st.sidebar.selectbox('Eixo X', options=colunas_numericas)
    y_values = st.sidebar.selectbox('Eixo Y', options=colunas_numericas)
    plot = px.box(data_frame=filtered_data, x=x_values, y=y_values, color_discrete_sequence=custom_palette)
    st.plotly_chart(plot)

elif chart_select == "Heatmap":
    st.subheader("Configurar Heatmap")

    # Calcular a matriz de correlação apenas para as colunas numéricas do dataset filtrado
    matriz_correlacao = filtered_data[colunas_numericas].corr()

    # Encontrar as colunas com maiores correlações
    num_colunas_maior_correlacao = 110
    colunas_maior_correlacao = matriz_correlacao.abs().nlargest(num_colunas_maior_correlacao, "cirurgia_eletiva").index
    st.write("Colunas com Maior Correlação:")
    st.write(colunas_maior_correlacao)

    # Visualizar o heatmap de correlação com as colunas selecionadas
    heatmap_data = filtered_data[colunas_maior_correlacao]
    st.write(heatmap_data.corr().style.background_gradient(cmap='coolwarm'))

    high_correlations = matriz_correlacao.abs().unstack().sort_values(ascending=False).reset_index()
    high_correlations = high_correlations[high_correlations['level_0'] != high_correlations['level_1']]  # Remover correlações da mesma coluna
    high_correlations = high_correlations[(high_correlations[0] > 0.4) & (high_correlations[0] < 1.0)]

    # Exibir as correlações
    st.write("Correlações com valor maior que 0.4 e menor que 1.0:")
    for index, row in high_correlations.iterrows():
        st.write(f"{row['level_0']} - {row['level_1']}: {row[0]}")