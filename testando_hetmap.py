import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o dataset
data = pd.read_parquet('data/dataset.parquet')

# Selecionar as colunas
col1 = st.sidebar.selectbox("Selecione a primeira coluna", data.columns)
col2 = st.sidebar.selectbox("Selecione a segunda coluna", data.columns)

# Calcular a correlação
correlation = data[[col1, col2]].corr()

# Criar o heatmap de correlação
fig = px.imshow(correlation)

# Configurar o layout
fig.update_layout(
    title="Heatmap de Correlação",
    xaxis_title=col1,
    yaxis_title=col2
)

# Exibir o gráfico
st.plotly_chart(fig)
