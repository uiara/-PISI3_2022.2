from dicionario_dados import dic

import streamlit as st
import pandas as pd


def home():
    st.title('Página 1 - Introdução')
    
    st.write('Introdução inicial dos dados')
    
    df = pd.read_parquet("data/dataset_renomeado.parquet")
    
    st.write('Vizualição dos dados')
    st.dataframe(df.head())
    st.write('Quantidades de linhas e colunas')
    st.write(df.shape)
    st.write('Tipo dos dados')
    st.write(df.dtypes)
    st.write('Descrição dos dados:')
    st.write(df.describe())
    st.write('Aqui estão as contagens de valores nulos por coluna:')
    null_counts = df.isnull().sum().sort_values(ascending=False)
    for column, count in null_counts.items():
        if count > 0:
            st.write(f"{column}: {count}")
 

def graficos():
    st.title('Graficos do dataset Patient Survival Prediction')
    df = pd.read_parquet("data/dataset_renomeado.parquet")
   
    genero_proporcao = df['genero'].value_counts(normalize=True)*100

    plt.style.use("ggplot")
    fig = plt.figure(figsize=(8, 6))
    genero_proporcao.plot(kind='pie')
    plt.xlabel('Gênero')
    plt.ylabel('Contagem')
    plt.title('Proporção por Gêneros')
    st.pyplot(fig)


    etinia_count = df['etnia'].value_counts()
    fig = plt.figure(figsize = (8, 6))
    df["etnia"].hist(bins = 40, ec = "k", alpha = .6, color = "royalblue")
    plt.title("Distribuição de Etnias")
    plt.xlabel("Etnia")
    plt.ylabel("Contagem")
    st.pyplot(fig)
    
    doencas = st.selectbox("Selecione a doença", options = ('aids','cirrose', 'diabetes_mellitus', 'insuficiencia_hepatica',
                                                              'imunossupressao','leucemia',
                                                              'linfoma','tumor_solido_com_metastase')
    )

    doencas_counts = df[df[doencas] == 1].groupby('idade').size().reset_index(name = f'total_pessoas_com_{doencas}')

    fig= px.scatter(doencas_counts, x = 'idade', y = f'total_pessoas_com_{doencas}')

    fig.update_layout(
        title = f'Total de Pessoas com {doencas} por Idade',
        xaxis_title = 'Idade',
        yaxis_title = f'Total de Pessoas com {doencas}',
    )

    st.plotly_chart(fig)
    ##
    doencas_counts = df[df[doencas] == 1].groupby('imc').size().reset_index(name = f'total_pessoas_com_{doencas}')

    fig= px.scatter(doencas_counts, x = 'imc', y = f'total_pessoas_com_{doencas}')

    fig.update_layout(
        title = f'IMC de pessoas com {doencas}',
        xaxis_title = 'IMC',
        yaxis_title = f'Total de Pessoas com {doencas}',
    )

    st.plotly_chart(fig)
# Seletor de página
pages = {
    'Página 1 - Introdução': home,
    'Página 2 - Dicionário': dic,
    'Página 3 - Gráficos': gráficos
}

# Título
st.title('Patient Survival Prediction')

# Seletor de página na barra lateral
page = st.sidebar.selectbox('Selecione a página', tuple(pages.keys()))

# Renderiza a página selecionada
pages[page]()
