import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def inter():
    # Ler o dataframe do arquivo Parquet
    df = pd.read_parquet('data/dataset_streamlit.parquet')

    # Selecionar as colunas relevantes
    colunas_selecionadas = ['fonte_admissao_uti', 'tipo_estadia_uti', 'tipo_uti',
       'dias_de_permanencia_pre_uti', 'peso', 'diagnostico_pache_2',
       'diagnostico_apache_3j', 'apache_pos_operatorio', 'arf_apache',
       'gcs_olhos_apache', 'gcs_motor_apache', 'gcs_incapaz_apache',
       'gcs_verbal_pache', 'frequencia_cardiaca_apache', 'intubado_apache',
       'map_apache', 'frequencia_respiratoria_pache', 'temperatura_apache',
       'ventilado_apache','sistema_corporal_apache_3j','sistema_corporal_apache_2', 'morte_hospital']
    
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
inter()
