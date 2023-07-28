import pandas as pd

df = pd.read_parquet('data/dataset_streamlit.parquet')

colunas_categoricas = ['etnia', 'genero', 'fonte_admissao_uti', 'tipo_estadia_uti', 'tipo_uti', 'sistema_corporal_apache_3j', 'sistema_corporal_apache_2']

df_encoded = pd.get_dummies(df, columns=colunas_categoricas)

# Selecionar apenas as colunas categóricas criadas
colunas_criadas = df_encoded.columns[df_encoded.columns.str.startswith(tuple(colunas_categoricas))]

# Criar um novo DataFrame com as colunas categóricas criadas
df_categoricas_criadas = df_encoded[colunas_criadas]

# Salvar as colunas categóricas criadas em um arquivo CSV
df_categoricas_criadas.to_csv('colunas_categoricas_criadas_trad.csv', index=False)