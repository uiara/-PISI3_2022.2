import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_parquet('/home/bianka/PISI3_2022.2/data/dataset_streamlit.parquet')

# Streamlit app
def main():
    st.title('Análise Dinâmica por Tipo de UTI')

    # Sidebar - Escolha a coluna categórica
    categorical_column = st.sidebar.selectbox('Selecione a Coluna Categórica:', df.columns)

    # Sidebar - Escolha a coluna numérica para o eixo y
    numeric_column = st.sidebar.selectbox('Selecione a Coluna Numérica para o Eixo Y:', df.columns)

    # Crie intervalos de idade (você pode ajustar os intervalos conforme necessário)
    age_bins = [0, 30, 40, 50, 60, 70, 80, float('inf')]
    age_labels = ['0-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80+']

    # Atribua cada valor de idade a um intervalo e crie uma nova coluna 'faixa_etaria'
    df['faixa_etaria'] = pd.cut(df['idade'], bins=age_bins, labels=age_labels)

    # Agrupe e agregue os dados com base na coluna categórica escolhida e nas faixas etárias
    df_grouped = df.groupby([categorical_column, 'faixa_etaria']).mean().reset_index()
    df_grouped['contagem'] = df.groupby([categorical_column, 'faixa_etaria']).count().reset_index()['morte_hospital']

    # Crie o gráfico usando Plotly Express
    fig = px.scatter(df_grouped, x="faixa_etaria", y=numeric_column, size="contagem", color=categorical_column,
                     hover_name=categorical_column, log_x=False, size_max=60)
    fig.update_layout(title_text=f"<b>{numeric_column} por Faixa Etária para diferentes Tipos de UTI<b>")
    fig.update_yaxes(title_text=f"<b>{numeric_column}<b>")
    fig.update_xaxes(title_text="<b>Faixa Etária<b>")

    # Mostre o gráfico usando Streamlit
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()
