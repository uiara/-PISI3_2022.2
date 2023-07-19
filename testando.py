import streamlit as st
import pandas as pd
import plotly.express as px

#def carregar_dados():
df = pd.read_parquet('data/dataset_streamlit.parquet')
    #return dados

#def pagina():
#df = carregar_dados()

colunas_anterior_internamento = ['idade', 'imc', 'cirurgia_eletiva', 'etnia', 'genero', 'altura', 'aids', 'cirrose', 'diabetes_mellitus',
                        'insuficiencia_hepatica', 'imunossupressao', 'leucemia', 'linfoma', 'tumor_solido_com_metastase', 'morte_hospital']

colunas_durante_internamento = ['fonte_admissao_uti', 'tipo_estadia_uti', 'tipo_uti',
    'dias_de_permanencia_pre_uti', 'peso', 'diagnostico_pache_2',
    'diagnostico_apache_3j', 'apache_pos_operatorio', 'arf_apache',
    'gcs_olhos_apache', 'gcs_motor_apache', 'gcs_incapaz_apache',
    'gcs_verbal_pache', 'frequencia_cardiaca_apache', 'intubado_apache',
    'map_apache', 'frequencia_respiratoria_pache', 'temperatura_apache',
    'ventilado_apache','sistema_corporal_apache_3j','sistema_corporal_apache_2', 'morte_hospital']

colunas_primeira_hora = ['h1_pressão_arterial_diastolica_maxima',
    'h1_ressao_arterial_iastolica_minima',
    'h1_pressao_arterial_diastolica_nao_invasiva_maxima',
    'h1_pressao_arterial_diastolica_nao_invasiva_minima',
    'h1_frequencia_cardiaca_maxima', 'h1_requencia_cardiaca_minima',
    'h1_pressao_arterial_media_maxima', 'h1_pressao_arterial_media_minima',
    'h1_pressao_arterial_media_nao_invasiva_maxima',
    'h1_pressao_arterial_media_nao_invasiva_minima',
    'h1_frequencia_respiratoria_maxima',
    'h1_frequencia_respiratoria_minima', 'h1_spO2_maximo', 'h1_spO2_minimo',
    'h1_pressao_arterial_sistolica_maxima',
    'h1_pressao_arterial_sistolica_minima',
    'h1_pressao_arterial_sistolica_nao_invasiva_maxima',
    'h1_pressão_arterial_sistolica_nao_invasiva_minima', 'morte_hospital']


colunas_primeiras_vinte_quatro = ['d1_pressao_arterial_diastolica_maxima',
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

# Configurar o aplicativo Streamlit
st.title('Gráfico de Correlação')
st.write('Selecione duas listas para visualizar a correlação entre elas.')

# Exibir opções para selecionar as listas
selected_lista1 = st.selectbox('Selecione a primeira lista:', (colunas_anterior_internamento, colunas_durante_internamento, colunas_primeira_hora, colunas_primeiras_vinte_quatro))
selected_lista2 = st.selectbox('Selecione a segunda lista:', (colunas_anterior_internamento, colunas_durante_internamento, colunas_primeira_hora, colunas_primeiras_vinte_quatro))

# Verificar se duas listas foram selecionadas
if selected_lista1 != selected_lista2:
    # Concatenar as duas listas selecionadas
    selected_columns = selected_lista1 + selected_lista2

    # Carregar o dataset com as colunas selecionadas
    #df = pd.read_csv('seu_dataset.csv', usecols=selected_columns)

    # Gerar o gráfico de correlação usando a biblioteca Plotly
    corr_df = df.corr()
    fig = px.imshow(corr_df)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.write('Por favor, selecione duas listas diferentes.')



# Configurar o aplicativo Streamlit
st.title('Gráfico de Correlação')
st.write('Selecione 2 conjuntos de colunas para visualizar a correlação.')

# Exibir opções para selecionar os conjuntos de colunas
selected_columns = st.multiselect('Selecione os conjuntos de colunas:', df.columns)

# Verificar se exatamente 2 conjuntos de colunas foram selecionados
if len(selected_columns) == 2:
    # Gerar o gráfico de correlação usando a biblioteca Plotly
    corr_df = df[selected_columns].corr()
    fig = px.imshow(corr_df)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.write('Por favor, selecione exatamente 2 conjuntos de colunas.')

