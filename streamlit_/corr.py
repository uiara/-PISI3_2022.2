import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px




def carregar_dados():
    dados = pd.read_parquet('/home/bianka/PISI3_2022.2/data/dataset_streamlit.parquet')

    return dados

def pagina():
    df = carregar_dados()

    colunas_anterior_internamento = ['idade', 'imc', 'cirurgia_eletiva', 'etnia', 'genero', 'altura', 'aids', 'cirrose', 'diabetes_mellitus',
                            'insuficiencia_hepatica', 'imunossupressao', 'leucemia', 'linfoma', 'tumor_solido_com_metastase', 
                            'sistema_corporal_apache_3j', 'sistema_corporal_apache_2',
                            'probabilidade_morte_no_hospital_(apache_4a)',
                            'probabilidade_morte_na_uti_(apache_4a)',
                            'morte_hospital']

    colunas_durante_internamento = ['fonte_admissao_uti', 'tipo_estadia_uti', 'tipo_uti',
        'dias_de_permanencia_pre_uti', 'peso', 'diagnostico_pache_2',
        'diagnostico_apache_3j', 'apache_pos_operatorio', 'arf_apache',
        'gcs_olhos_apache', 'gcs_motor_apache', 'gcs_incapaz_apache',
        'gcs_verbal_pache', 'frequencia_cardiaca_apache', 'intubado_apache',
        'map_apache', 'frequencia_respiratoria_pache', 'temperatura_apache',
        'ventilado_apache','sistema_corporal_apache_3j','sistema_corporal_apache_2', 
        'probabilidade_morte_no_hospital_(apache_4a)',
        'probabilidade_morte_na_uti_(apache_4a)',
        'morte_hospital']

    colunas_primeira_hora = ['pressao_arterial_diastolica_maxima_primeira_hora',
       'pressao_arterial_iastolica_minima_primeira_hora',
       'pressao_arterial_diastolica_nao_invasiva_maxima_primeira_hora',
       'pressao_arterial_diastolica_nao_invasiva_minima_primeira_hora',
       'frequencia_cardiaca_maxima_primeira_hora',
       'requencia_cardiaca_minima_primeira_hora',
       'pressao_arterial_media_maxima_primeira_hora',
       'pressao_arterial_media_minima_primeira_hora',
       'pressao_arterial_media_nao_invasiva_maxima_primeira_hora',
       'pressao_arterial_media_nao_invasiva_minima_primeira_hora',
       'frequencia_respiratoria_maxima_primeira_hora',
       'frequencia_respiratoria_minima_primeira_hora',
       'spO2_maximo_primeira_hora', 'spO2_minimo_primeira_hora',
       'pressao_arterial_sistolica_maxima_primeira_hora',
       'pressao_arterial_sistolica_minima_primeira_hora',
       'pressao_arterial_sistolica_nao_invasiva_maxima_primeira_hora',
       'pressão_arterial_sistolica_nao_invasiva_minima_primeira_hora', 
       'sistema_corporal_apache_3j', 'sistema_corporal_apache_2',
       'probabilidade_morte_no_hospital_(apache_4a)',
       'probabilidade_morte_na_uti_(apache_4a)',
       'morte_hospital']


    colunas_primeiras_vinte_quatro = ['pressao_arterial_diastolica_maxima_primeiras_24_horas',
       'pressao_arterial_diastolica_minima_primeiras_24_horas',
       'pressao_arterial_diastolica_nao_invasiva_maxima_primeiras_24_horas',
       'pressao_arterial_diastólica_nao_invasiva_minima_primeiras_24_horas',
       'frequencia_cardiaca_maxima_primeiras_24_horas',
       'frequencia_cardiaca_minima_primeiras_24_horas',
       'pressao_arterial_media_maxima_primeiras_24_horas',
       'pressao_arterial_media_minima_primeiras_24_horas',
       'pressao_arterial_media_nao_invasiva_maxima_primeiras_24_horas',
       'pressao_arterial_media_nao_invasiva_minima_primeiras_24_horas',
       'frequencia_respiratoria_maxima_primeiras_24_horas',
       'frequencia_respiratoria_minima_primeiras_24_horas',
       'spO2_maximo_primeiras_24_horas', 'spO2_minimo_primeiras_24_horas',
       'pressao_arterial_sistolica_maxima_primeiras_24_horas',
       'pressao_arterial_sistolica_minima_primeiras_24_horas',
       'pressao_arterial_sistolica_nao_invasiva_maxima_primeiras_24_horas',
       'pressao_arterial_sistolica_nao_invasiva_minima_primeiras_24_horas',
       'temperatura_maxima_primeiras_24_horas',
       'temperatura_minima_primeiras_24_horas',
       'glicose_maxima_primeiras_24_horas',
       'glicose_minima_primeiras_24_horas',
       'potassio_maximo_primeiras_24_horas',
       'potassio_minimo_primeiras_24_horas',
       'sistema_corporal_apache_3j', 'sistema_corporal_apache_2',
       'probabilidade_morte_no_hospital_(apache_4a)',
       'probabilidade_morte_na_uti_(apache_4a)',
       'morte_hospital']

    st.title("Análise em Correlação")

    introducao = '''
    Os dados foram divididos em quatro conjuntos de colunas, com base na origem das informações.
    '''
    st.markdown(introducao)
    #with st.expander("Heatmap"):
    st.header("Antes de Ser Internado")
    st.info("Este conjunto contém as colunas que representam os dados do paciente antes de sua admissão no hospital.")

    correlation_matrix = df[colunas_anterior_internamento].corr()
    fig = go.Figure(data=go.Heatmap(
        z=correlation_matrix.values,
        x=correlation_matrix.columns,
        y=correlation_matrix.columns,
        colorscale='Viridis'))
    fig.update_layout(
        title="Matriz de Correlação",
        xaxis_title="Colunas",
        yaxis_title="Colunas",
        width=800,
        height=600)
    st.plotly_chart(fig)

    #with col2:
    st.header("Durante o Internamento")
    st.info("Nesse conjunto, estão as colunas que representam os dados coletados durante o período de internação do paciente.")

    correlation_matrix = df[colunas_durante_internamento].corr()
    fig = go.Figure(data=go.Heatmap(
        z=correlation_matrix.values,
        x=correlation_matrix.columns,
        y=correlation_matrix.columns,
        colorscale='Viridis'))
    fig.update_layout(
        title="Matriz de Correlação",
        xaxis_title="Colunas",
        yaxis_title="Colunas",
        width=800,
        height=600)
    st.plotly_chart(fig)

    #with col3:
    st.header("Primeira Hora de Internamento")
    st.info("Aqui estão as colunas que contêm os dados específicos coletados durante a primeira hora do paciente internado.")

    correlation_matrix = df[colunas_primeira_hora].corr()
    fig = go.Figure(data=go.Heatmap(
        z=correlation_matrix.values,
        x=correlation_matrix.columns,
        y=correlation_matrix.columns,
        colorscale='Viridis'))
    fig.update_layout(
        title="Matriz de Correlação",
        xaxis_title="Colunas",
        yaxis_title="Colunas",
        width=800,
        height=600)
    st.plotly_chart(fig)

    #with col4:
    st.header("Primeiras Vinte e Quatro Horas de Internamento")
    st.info("Este conjunto de colunas engloba os dados coletados durante as primeiras vinte e quatro horas de internação do paciente.")

    correlation_matrix = df[colunas_primeiras_vinte_quatro].corr()
    fig = go.Figure(data=go.Heatmap(
        z=correlation_matrix.values,
        x=correlation_matrix.columns,
        y=correlation_matrix.columns,
        colorscale='Viridis'))
    fig.update_layout(
        title="Matriz de Correlação",
        xaxis_title="Colunas",
        yaxis_title="Colunas",
        width=800,
        height=600)
    st.plotly_chart(fig)


