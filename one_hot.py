import pandas as pd

df = pd.read_csv('data/dataset.csv')

colunas_categoricas = ['ethnicity', 'gender', 'icu_admit_source', 'icu_stay_type', 'icu_type', 'apache_3j_bodysystem', 'apache_2_bodysystem']

df_encoded = pd.get_dummies(df, columns=colunas_categoricas)

# Selecionar apenas as colunas categóricas criadas
colunas_criadas = df_encoded.columns[df_encoded.columns.str.startswith(tuple(colunas_categoricas))]

# Criar um novo DataFrame com as colunas categóricas criadas
df_categoricas_criadas = df_encoded[colunas_criadas]

# Salvar as colunas categóricas criadas em um arquivo CSV
df_categoricas_criadas.to_csv('colunas_categoricas_criadas.csv', index=False)