import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Ler o dataframe do arquivo Parquet
df = pd.read_parquet('data/dataset_streamlit.parquet')

# Colunas referentes à primeira hora
primeira_hora_colunas = [
    'h1_pressão_arterial_diastolica_maxima',
    'h1_ressao_arterial_iastolica_minima',
    'h1_pressao_arterial_diastolica_nao_invasiva_maxima',
    'h1_pressao_arterial_diastolica_nao_invasiva_minima',
    'h1_frequencia_cardiaca_maxima',
    'h1_frequencia_cardiaca_minima',
    'h1_pressao_arterial_media_maxima',
    'h1_pressao_arterial_media_minima',
    'h1_pressao_arterial_media_nao_invasiva_maxima',
    'h1_pressao_arterial_media_nao_invasiva_minima',
    'h1_frequencia_respiratoria_maxima',
    'h1_frequencia_respiratoria_minima',
    'h1_spO2_maximo',
    'h1_spO2_minimo',
    'h1_pressao_arterial_sistolica_maxima',
    'h1_pressao_arterial_sistolica_minima',
    'h1_pressao_arterial_sistolica_nao_invasiva_maxima',
    'h1_pressao_arterial_sistolica_nao_invasiva_minima'
]

# Colunas referentes às primeiras 24 horas
primeiras_24_horas_colunas = [
    'd1_pressao_arterial_diastolica_maxima',
    'd1_pressao_arterial_diastolica_minima',
    'd1_pressao_arterial_diastolica_nao_invasiva_maxima',
    'd1_pressao_arterial_diastólica_nao_invasiva_minima',
    'd1_frequencia_cardiaca_maxima',
    'd1_frequencia_cardiaca_minima',
    'd1_pressao_arterial_media_maxima',
    'd1_pressao_arterial_media_minima',
    'd1_pressao_arterial_media_nao_invasiva_maxima',
    'd1_pressao_arterial_media_nao_invasiva_minima',
    'd1_frequencia_respiratoria_maxima',
    'd1_frequencia_respiratoria_minima',
    'd1_spO2_maximo',
    'd1_spO2_minimo',
    'd1_pressao_arterial_sistolica_maxima',
    'd1_pressao_arterial_sistolica_minima',
    'd1_pressao_arterial_sistolica_nao_invasiva_maxima',
    'd1_pressao_arterial_sistolica_nao_invasiva_minima',
    'd1_temperatura_maxima',
    'd1_temperatura_minima',
    'd1_glicose_maxima',
    'd1_glicose_minima',
    'd1_potassio_maximo',
    'd1_potassio_minimo'
]

# Seleção para a primeira hora
st.sidebar.markdown("## Primeira Hora")
primeira_hora_opcao_selecionada = st.sidebar.selectbox("Selecione a opção para análise:", primeira_hora_colunas)

# Seleção para as primeiras 24 horas
st.sidebar.markdown("## Primeiras 24 Horas")
primeiras_24_horas_opcao_selecionada = st.sidebar.selectbox("Selecione a opção para análise:", primeiras_24_horas_colunas)

# Filtrar o dataframe mantendo apenas as colunas selecionadas para a primeira hora
df_primeira_hora = df[[primeira_hora_opcao_selecionada]]

# Filtrar o dataframe mantendo apenas as colunas selecionadas para as primeiras 24 horas
df_primeiras_24_horas = df[[primeiras_24_horas_opcao_selecionada]]

# Criar figura e adicionar os dados selecionados
fig = go.Figure()
fig.add_trace(go.Bar(x=['Primeira Hora'], y=[df_primeira_hora.iloc[0, 0]], name=primeira_hora_opcao_selecionada))
fig.add_trace(go.Bar(x=['Primeiras 24 Horas'], y=[df_primeiras_24_horas.iloc[0, 0]], name=primeiras_24_horas_opcao_selecionada))

# Personalizar o layout do gráfico
fig.update_layout(
    title='Análise do Resultado',
    xaxis_title='Período',
    yaxis_title='Resultado',
    barmode='stack'
)

# Exibir o gráfico no Streamlit
st.plotly_chart(fig)