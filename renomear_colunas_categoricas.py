import pandas as pd

# Carregar o arquivo CSV
nome_arquivo = 'data/dataset_renomeado_onehot_nonull.csv'  # Substitua pelo caminho correto
dataframe = pd.read_csv(nome_arquivo)

# Dicionário de mapeamento dos nomes das colunas
mapeamento_colunas = {
    "sistema_corporal_apache_3j_Genitourinary": "sistema_corporal_apache_3j_Geniturinario",
    "sistema_corporal_apache_3j_Gynecological": "sistema_corporal_apache_3j_Ginecologico",
    "sistema_corporal_apache_3j_Hematological": "sistema_corporal_apache_3j_Hematologico",
    "sistema_corporal_apache_3j_Metabolic": "sistema_corporal_apache_3j_Metabolico",
    "sistema_corporal_apache_3j_Musculoskeletal/Skin": "sistema_corporal_apache_3j_musculoesqueletico/Pele",
    "sistema_corporal_apache_3j_Neurological": "sistema_corporal_apache_3j_Neurologico",
    "sistema_corporal_apache_3j_Respiratory": "sistema_corporal_apache_3j_Respiratorio",
    "sistema_corporal_apache_2_Haematologic": "sistema_corporal_apache_2_Hematologico",
    "sistema_corporal_apache_2_Metabolic": "sistema_corporal_apache_2_Metabolico",
    "sistema_corporal_apache_2_Neurologic": "sistema_corporal_apache_2_Neurologico",
    "sistema_corporal_apache_2_Renal/Genitourinary": "sistema_corporal_apache_2_Renal/Geniturinario",
    "sistema_corporal_apache_2_Respiratory": "sistema_corporal_apache_2_Respiratorio",
    "sistema_corporal_apache_2_Undefined Diagnoses": "sistema_corporal_apache_2_Diagnosticos_Indefinidos",
    "sistema_corporal_apache_2_Undefined Diagnoses_1": "sistema_corporal_apache_2_Diagnosticos_1_Indefinidos"
}

# Renomear as colunas
dataframe.rename(columns=mapeamento_colunas, inplace=True)

# Salvar o DataFrame modificado em um novo arquivo CSV
novo_nome_arquivo = 'data/dataset_renamed_onehot_nonull.csv'  # Substitua pelo caminho correto
dataframe.to_csv(novo_nome_arquivo, index=False)