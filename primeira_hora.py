import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def primeira():
    # Ler o dataframe do arquivo Parquet
    df = pd.read_parquet('data/dataset_streamlit.parquet')

    # Selecionar as colunas relevantes
    colunas_selecionadas = ['h1_pressão_arterial_diastolica_maxima',
       'h1_ressao_arterial_iastolica_minima',
       'h1_pressao_arterial_diastolica_nao_invasiva_maxima',
       'h1_pressao_arterial_diastolica_nao_invasiva_minima',
       'h1_frequencia_cardiaca_maxima', 'h1_requencia_cardiaca_minima',
       'h1_pressao_arterial_media_maxima', 'h1_pressao_arterial_media_minima',
       'h1_pressao_arterial_media_nao_invasiva_maxima',
       'h1_pressao_arterial_media_nao_invasiva_minima',
       'h1_frequencia_respiratoria_maxima',
       'h1_frequencia_respiratoria_minima', 'h1_spO2_maximo', 'h1_spO2_minimo',
       'h1_pressao_arterial_sistolica_maxima',
       'h1_pressao_arterial_sistolica_minima',
       'h1_pressao_arterial_sistolica_nao_invasiva_maxima',
       'h1_pressão_arterial_sistolica_nao_invasiva_minima', 'morte_hospital']
    
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
primeira()
