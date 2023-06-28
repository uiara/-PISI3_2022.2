from dicionario_dados import dic

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")

def home():
    st.title('Página 1 - Introdução')
    
    st.write('Introdução inicial dos dados')
    
    df = pd.read_parquet("data/dataset_renomeado.parquet")


    #with st.expander("Visualização dos dados", expanded=True):
    #    st.dataframe(df.head())
    st.write('Vizualição dos dados')
    st.dataframe(df.head())
    st.title('Dados Patient Survival Prediction')
    col1, col2, col3 = st.columns(3)# Calcular o total de pacientes
    
    total_pacientes = df.shape[0]

    # Calcular o número de pessoas que sobreviveram
    sobreviventes = df['morte_hospital'].value_counts()[0]

    # Calcular a porcentagem de sobreviventes em relação ao total de pacientes
    porcentagem_sobreviventes = (sobreviventes / total_pacientes) * 100
    
    # Exibir o valor total de participantes
    with col1:
        st.markdown(
            f"<div style='text-align: center; padding: 10px; width: 200px;'>"
            f"<span style='font-size: 40px'>{total_pacientes}</span>"
            f"<br>"
            f"<span style='font-size: 20px'>Total pacientes</span>"
            f"</div>",
            unsafe_allow_html=True
        )

    # Cálculo das porcentagens
    count = df['genero'].value_counts()
    percentages = count / len(df) * 100

    # Criação do Sunburst Plot
    fig = go.Figure(go.Sunburst(
        labels=['Total', 'Homem', 'Mulher'],
        parents=['', 'Total', 'Total'],
        values=[100, percentages['M'], percentages['F']],
    ))

    # Configurações de layout
    fig.update_layout(
        height=300,
        margin=dict(t=20, l=0, r=0, b=0),
    )

    # Exibir o número de sobreviventes e a porcentagem
    with col3:

        # Definir as opções para a seleção
        opcoes_coluna2 = ['Quantidade Total', 'Porcentagem']

        # Selecionar a opção escolhida
        #opcao_selecionada = st.selectbox("Escolha a exibição na coluna 2:", opcoes_coluna2)
        
        st.markdown(
            f"<div style='text-align: center; padding: 10px; width: 200px;'>"
            f"<span style='font-size: 30px'>{porcentagem_sobreviventes:.2f}%</span>"
            f"<br>"
            f"<span style='font-size: 16px'>Porcentagem de Sobreviventes</span>"
            f"</div>",
            unsafe_allow_html=True
        )

        # Cálculo das porcentagens
        count = df['genero'].value_counts()
        percentagens = count / len(df) * 100

        # Criação do Sunburst Plot
        fig = go.Figure(go.Sunburst(
            labels=['Total', 'Homem', 'Mulher'],
            parents=['', 'Total', 'Total'],
            values=[100, percentagens['M'], percentagens['F']],
        ))

        # Configurações de layout
        fig.update_layout(
            height=300,
            margin=dict(t=20, l=0, r=0, b=0),
        )

    # Exibição do Sunburst Plot no Streamlit
    with col2:
        st.plotly_chart(fig, use_container_width=True)
    
    genero_proporcao = df['genero'].value_counts(normalize=True)*100
    fig = plt.figure(figsize=(8, 6))
    genero_proporcao.plot(kind='pie')
    plt.xlabel('Gênero')
    plt.ylabel('Contagem')
    plt.title('Proporção por Gêneros')
    st.pyplot(fig)

    
    df['tipo_estadia_uti'] = df['tipo_estadia_uti'].replace({'admit':'Admitido', 'readmit':'Readmitido', 'transfer':'Transferido'})
    tipo_de_estadia_count = df['tipo_estadia_uti'].value_counts()
    fig = plt.figure(figsize = (6, 4))
    tipo_de_estadia_count.plot(kind='pie')
    plt.title("Tipos de Estadia UTI")
    plt.xlabel("Estadia")
    #plt.ylabel("Contagem")
    st.pyplot(fig)

    etinia_count = df['etnia'].value_counts()
    fig = plt.figure(figsize = (6, 4))
    df["etnia"].hist(bins = 40, ec = "k", alpha = .6, color = "royalblue")
    plt.title("Distribuição de Etnias")
    plt.xlabel("Etnia")
    plt.ylabel("Contagem")
    st.pyplot(fig)
    fonte_admissao_uti_count = df['fonte_admissao_uti'].value_counts()
    fig = plt.figure(figsize = (8, 6))
    df['fonte_admissao_uti'].hist(bins = 40, ec = "k", alpha = .6, color = "royalblue")
    plt.title("Tipos de Admissão na UTI")
    plt.xlabel("Admissão")
    plt.ylabel("Contagem")
    st.pyplot(fig)

    tipo_de_estadia_count = df['tipo_estadia_uti'].value_counts()
    df['tipo_estadia_uti'].replace({'admit':'Admitido', 'readmit':'Readmitido', 'transfer':'Transferido'})
    fig = plt.figure(figsize = (8, 6))
    df['tipo_estadia_uti'].hist(bins = 40, ec = "k", alpha = .6, color = "royalblue")
    plt.title("Tipos de Estadia UTI")
    plt.xlabel("Estadia")
    plt.ylabel("Contagem")
    st.pyplot(fig)
    
    doencas = st.selectbox("Selecione a doença", options = ('aids','cirrose', 'diabetes_mellitus', 'insuficiencia_hepatica',
                                                              'imunossupressao','leucemia',
                                                              'linfoma','tumor_solido_com_metastase')
    )

    doencas_counts = df[df[doencas] == 1].groupby('idade').size().reset_index(name='total_pessoas_com_{doencas}')

    fig= px.scatter(doencas_counts, x = 'idade', y='total_pessoas_com_{doencas}')

    fig.update_layout(
        title = f'IMC de pessoas com {doencas}',
        xaxis_title = 'IMC',
        yaxis_title = f'Total de Pessoas com {doencas}',
    )
    st.plotly_chart(fig)

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
    #'Página 3 - Gráficos': gráficos
}


# Título
st.title('Patient Survival Prediction')

# Seletor de página na barra lateral
page = st.sidebar.selectbox('Selecione a página', tuple(pages.keys()))

# Renderiza a página selecionada
pages[page]()