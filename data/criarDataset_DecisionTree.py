import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Carregar o arquivo CSV
nome_arquivo = 'C:/Users/leogo/OneDrive/Área de Trabalho/PISI3_2022.2-main/data/dataset_renomeado_onehot.csv'
df = pd.read_csv(nome_arquivo)

# Remover colunas com mais de 30% de valores ausentes
threshold = 0.3
data_cleaned = df.dropna(thresh=len(df) * (1 - threshold), axis=1)

# Preencher valores ausentes com a mediana
data_preenchido = df.fillna(df.median())

# Salvar o novo conjunto de dados tratado
data_preenchido.to_parquet("data\decisionTree_dataset.parquet", index=False)
