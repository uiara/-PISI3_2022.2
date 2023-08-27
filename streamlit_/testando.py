import streamlit as st
import pandas as pd
import plotly.express as px

# Seu DataFrame de dados (substitua isso pelo seu próprio DataFrame)
# Certifique-se de que seu DataFrame tenha as colunas mencionadas em colunas_para_histograma
# Substitua df_training pelo nome do seu DataFrame
df_training = pd.read_csv('/home/bianka/PISI3_2022.2/data/dataset.csv')

# Título do aplicativo Streamlit
st.title("Histograma Interativo")

# Sidebar para seleção de opções
st.sidebar.header("Opções")
hospital_death = st.sidebar.radio("Filtrar por hospital_death", ["Todos", "0", "1"])

# Filtramos o dataset com base na opção selecionada.
if hospital_death == '0':
    df_filtered = df_training[df_training['hospital_death'] == 0]
elif hospital_death == '1':
    df_filtered = df_training[df_training['hospital_death'] == 1]  
else:
    df_filtered = df_training.copy()

# Lista de colunas para criar histogramas
colunas_para_histograma = [
    'encounter_id', 'patient_id', 'hospital_id', 'age', 'bmi',  # Adicione todas as colunas desejadas aqui
]

# Loop pelas colunas e cria histogramas
for coluna in colunas_para_histograma:
    st.plotly_chart(px.histogram(df_filtered, x=coluna, title=coluna + ', Hospital_death (' + hospital_death + ')'))

# Exemplo de como você pode adicionar outros elementos ao aplicativo Streamlit, se necessário
# st.write("Outros elementos aqui")
