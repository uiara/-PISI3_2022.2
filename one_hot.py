import pandas as pd

df = pd.read_parquet('data/dataset_renomeado.parquet')

colunas_categoricas = ['etnia', 'genero', 'fonte_admissao_uti', 'tipo_estadia_uti', 'tipo_uti', 'sistema_corporal_apache_3j', 'sistema_corporal_apache_2']

df_encoded = pd.get_dummies(df, columns=colunas_categoricas, drop_first=True)

# Salvar o DataFrame com one-hot encoding em um arquivo CSV
df_encoded.to_csv('dataset_renomeado_onehot.csv', index=False)