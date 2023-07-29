import streamlit as st
import plotly_express as px
import pandas as pd

st.title("App de Teste - Visualização de Dados (usando o dataset.csv)")

st.sidebar.subheader("Opções")

def get_clean_data():
    data = pd.read_csv("data/dataset_onehot_filling_renomeadas.csv")
    # Remover colunas irrelevantes
    return data

clean_data = get_clean_data()

# Adicionar amostragem de dados
sampling_fraction = st.slider("Selecione a Fração de Amostragem de Dados", min_value=0.05, max_value=1.0, value=0.5, step=0.01)
sampled_data = clean_data.sample(frac=sampling_fraction, random_state=42)

# Adicionar um botão de rádio para filtrar mortes ou sobrevivências
filter_option = st.sidebar.radio("Filtrar por", ("Mostrar Todos", "Mortes", "Sobrevivências"))

if filter_option == "Mortes":
    filtered_data = sampled_data[sampled_data["morte_hospital"] == 1]
elif filter_option == "Sobrevivências":
    filtered_data = sampled_data[sampled_data["morte_hospital"] == 0]
else:
    filtered_data = sampled_data

# Exibir a contagem de mortes e sobrevivências
num_deaths = filtered_data["morte_hospital"].sum()
num_survivals = len(filtered_data) - num_deaths
st.write(f"Número de Mortes: {num_deaths}")
st.write(f"Número de Sobrevivências: {num_survivals}")

chart_select = st.sidebar.selectbox(
    label="Selecione o tipo de gráfico",
    options=["Dispersão", "Histograma", 'Boxplot', "Gráfico de Barras"]
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

elif chart_select == "Gráfico de Barras":
    st.sidebar.subheader("Configurar Gráfico de Barras")
    x_values = st.sidebar.selectbox('Selecione a coluna para o Gráfico de Barras', options=list(filtered_data.select_dtypes(include=['object']).columns))
    plot = px.bar(data_frame=filtered_data, x=x_values, color="morte_hospital")
    st.plotly_chart(plot)