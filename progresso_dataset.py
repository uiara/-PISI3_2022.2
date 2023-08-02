import streamlit as st
import pandas as pd

# Carregando os datasets
data_original = pd.read_csv('data/dataset.csv')
data_complete = pd.read_parquet('data/dataset_renomeado.parquet')  
data_no_nulls = pd.read_parquet('data/dataset_renomeado_sem_nulos.parquet')  
data_modified_nonull = pd.read_csv('data/dataset_renomeado_onehot_sem_nulos.csv')
data_modified_filling = pd.read_csv('data/dataset_onehot_filling_renomeadas.csv')  

# Interface do Streamlit
st.title('Visualização de Datasets em Diferentes Etapas de Normalização')
selected_dataset = st.selectbox('Selecione um dataset:', ['Original','Renomeado', 'Sem Nulos', 'Modificado Onehot sem nulos', 'Modificado Onehot com preenchimento'])

if selected_dataset == 'Original':
    st.subheader('Dataset Original')
    st.write(data_original)
elif selected_dataset == 'Renomeado':
    st.subheader('Dataset Traduzido')
    st.write(data_complete)    
elif selected_dataset == 'Sem Nulos':
    st.subheader('Dataset Traduzido sem Valores Nulos')
    st.write(data_no_nulls)
elif selected_dataset == 'Modificado Onehot sem nulos':
    st.subheader('Dataset com Método Onehot Sem Valores Nulos')
    st.write(data_modified_nonull)
elif selected_dataset == 'Modificado Onehot com preenchimento':
    st.subheader('Dataset com Método Onehot Com Preenchimento')
    st.write(data_modified_filling)