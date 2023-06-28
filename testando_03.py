import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o dataset
df = pd.read_parquet('data/dataset.parquet')

# Obter a lista de colunas de doenças
doencas_cols = ['aids', 'cirrhosis', 'diabetes_mellitus', 'hepatic_failure','leukemia','lymphoma']

# Selecionar a coluna de doença
doenca_selecionada = st.selectbox("Selecione a coluna de doença:", doencas_cols)


# Filtrar o dataframe com base na coluna de doença selecionada
df_doenca_selecionada = df[df[doenca_selecionada] == 1]

# Calcular o total de pessoas com AIDS em cada idade
aids_count = df_doenca_selecionada.groupby('age').size().reset_index(name='total_pessoas')

# Criar o título dinâmico
titulo = f"Total de Pessoas com {doenca_selecionada} por Idade "

# Criar o gráfico de dispersão
fig = px.scatter(aids_count, x='age', y='total_pessoas')

# Atualizar o layout do gráfico
fig.update_layout(
    title=titulo,
    xaxis_title="Idade",
    yaxis_title="Total de Pessoas ",
)

# Apresentar o gráfico no Streamlit
st.plotly_chart(fig)