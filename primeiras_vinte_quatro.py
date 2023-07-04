import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def vinte_quatro():
    # Ler o dataframe do arquivo Parquet
    df = pd.read_parquet('data/dataset_streamlit.parquet')

    # Selecionar as colunas relevantes
    colunas_selecionadas = ['d1_pressao_arterial_diastolica_maxima',
       'd1_pressao_arterial_diastolica_minima',
       'd1_pressao_arterial_diastolica_nao_invasiva_maxima',
       'd1_pressao_arterial_diastólica_nao_invasiva_minima',
       'd1_frequencia_cardiaca_maxima', 'd1_frequencia_cardiaca_minima',
       'd1_pressao_arterial_media_maxima', 'd1_pressao_arterial_media_minima',
       'd1_pressao_arterial_media_nao_invasiva_maxima',
       'd1_pressao_arterial_media_nao_invasiva_minima',
       'd1_frequencia_respiratoria_maxima',
       'd1_frequencia_respiratoria_minima', 'd1_spO2_maximo', 'd1_spO2_minimo',
       'd1_pressao_arterial_sistolica_maxima',
       'd1_pressao_arterial_sistolica_minima',
       'd1_pressao_arterial_sistolica_nao_invasiva_maxima',
       'd1_pressao_arterial_sistolica_nao_invasiva_minima',
       'd1_temperatura_maxima', 'd1_temperatura_minima','d1_glicose_maxima', 
       'd1_glicose_minima', 'd1_potassio_maximo',
       'd1_potassio_minimo', 'morte_hospital']
    
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
vinte_quatro()
