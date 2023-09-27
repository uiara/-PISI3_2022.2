from path import load_data

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def grupos():
    df = load_data()

    st.title("Análise em Conjuntos")

    introducao = ''' 
    '''
    st.markdown(introducao)
    st.title('Histograma de Idade, Gênero e Mortalidade Hospitalar')
    st.write('Este é um gráfico de histograma que mostra a distribuição das idades e a mortalidade hospitalar.')

    fig = px.histogram(df[['idade','genero','morte_hospital','imc']].dropna(), x="idade", y="morte_hospital", color="genero",
                   marginal="violin", # or violin, rug
                   hover_data=df[['idade','genero','morte_hospital','imc']].columns)
    st.plotly_chart(fig)

    st.header("Gráfico de Dispersão - Taxa de Sobrevivência em Diferentes Tipos de UTI")
    st.write("Taxa de sobrevivência em diferentes tipos de Unidades de Terapia Intensiva (UTI) com base na idade dos pacientes.")

    ICU_type = df[['tipo_uti', 'idade', 'morte_hospital']]

    # Tradução dos valores na coluna 'tipo_uti'
    ICU_type['tipo_uti'] = ICU_type['tipo_uti'].replace({
        'CTICU': 'CCU-CTICU',
        'Cardiac ICU': 'CCT-CTICU',
        'CSICU': 'SICU'
    })

    ICU_df = ICU_type.groupby(['tipo_uti', 'idade']).mean().reset_index()
    ICU_df['count'] = ICU_type.groupby(['tipo_uti', 'idade']).count().reset_index()['morte_hospital']

    fig = px.scatter(ICU_df, x="idade", y="morte_hospital", size="count", color="tipo_uti",
                    hover_name="tipo_uti", log_x=False, size_max=60)

    fig.update_layout(
        title_text="<b>Taxa de sobrevivência em diferentes tipos de UTI<b>"
    )
    fig.update_yaxes(title_text="<b>Média de Mortes Hospitalares<b>")
    fig.update_xaxes(title_text="<b>Idade<b>")
    st.plotly_chart(fig)

