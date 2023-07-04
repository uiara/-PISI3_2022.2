import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def passado():
    # Ler o dataframe do arquivo Parquet
    df = pd.read_parquet('data/dataset_streamlit.parquet')

    # Selecionar as colunas relevantes
    colunas_selecionadas = ['idade', 'imc', 'cirurgia_eletiva', 'etnia', 'genero', 'altura', 'aids', 'cirrose', 'diabetes_mellitus',
                           'insuficiencia_hepatica', 'imunossupressao', 'leucemia', 'linfoma', 'tumor_solido_com_metastase', 'morte_hospital']

    # Calcular a matriz de correlação
    correlation_matrix = df[colunas_selecionadas].corr()

    # Criar o heatmap da correlação
    fig = go.Figure(data=go.Heatmap(
        z=correlation_matrix.values,
        x=correlation_matrix.columns,
        y=correlation_matrix.columns,
        colorscale='Viridis'))

    # Personalizar o layout do heatmap
    fig.update_layout(
        title="Matriz de Correlação",
        xaxis_title="Colunas",
        yaxis_title="Colunas",
        width=800,
        height=600)

    # Exibir o heatmap no Streamlit
    st.plotly_chart(fig)

# Chamar a função para exibir o heatmap de correlação
passado()
