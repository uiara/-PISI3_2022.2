import streamlit as st
import pandas as pd

# Carregando os datasets
data_original = pd.read_csv('data/dataset.csv')
data_complete = pd.read_parquet('data/dataset_renomeado.parquet')  
data_nonull_onehot = pd.read_parquet('data/renomeado_nonull_onehot.parquet')  
data_mediana_onehot = pd.read_parquet('data/renomeado_mediana_onehot.parquet')
data_media_onehot = pd.read_parquet('data/renomeado_media_onehot.parquet')  

# Interface do Streamlit
st.title('Visualização do dataset em diferentes etapas de Normalização.')
selected_dataset = st.selectbox('Selecione um dataset:', ['Original','Renomeado', 'Modificado Onehot sem nulos', 'Modificado Onehot preenchimento por mediana', 'Modificado Onehot preenchimento por media'])

if selected_dataset == 'Original':
    st.subheader('Dataset Original')
    st.write(data_original)
    st.write("Dataset original do kaggle 'Patient survival prediction' sem alterações podemos notar valores nulos e colunas de ID de pacientes ")

elif selected_dataset == 'Renomeado':
    st.subheader('Dataset Traduzido')
    st.write(data_complete)
    st.write("Dataset alterado, ainda com valores nulos mas com colunas traduzidas para o português.")

elif selected_dataset == 'Modificado Onehot sem nulos':
    st.subheader('Dataset aplicado o método Onehot com remoção de linhas com valores nulos ')
    st.write(data_nonull_onehot)
    st.write("Dataset alterado, linhas com valores nulos são removidas, nota-se uma perda consideravel de linhas dessa maneira. Valores do tipo 'float' são convertidos para integrais, e é aplicado o método onehot em colunas categóricas; Essas colunas geradas são traduzidas.")

elif selected_dataset == 'Modificado Onehot preenchimento por mediana':
    st.subheader('Dataset aplicado o método Onehot com preenchimento de valores nulos por mediana')
    st.write(data_mediana_onehot)
    st.write("Dataset alterado, valores nulos são preenchidos com a mediana obtida de outros valores da coluna. Valores do tipo 'float' são convertidos para integrais, e é aplicado o método onehot em colunas categóricas; Essas colunas geradas são traduzidas.")

elif selected_dataset == 'Modificado Onehot preenchimento por media':
    st.subheader('Dataset aplicado método Onehot com preenchimento de valores nulos  por media')
    st.write(data_media_onehot)
    st.write("Dataset alterado, valores nulos são preenchidos com a média obtida de outros valores da coluna na visualização pode ser notada a repetição excessiva de certos valores como idade e peso. Valores do tipo 'float' são convertidos para integrais, e é aplicado o método onehot em colunas categóricas; Essas colunas geradas são traduzidas .")