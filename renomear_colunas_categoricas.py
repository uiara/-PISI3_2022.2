import pandas as pd

# Nome do arquivo CSV original
input_file = "dataset_renomeado_onehot.csv"

# Nome do arquivo Parquet com as colunas renomeadas
output_file = "dataset_renomeado_mais_onehot.csv"

# Ler o arquivo CSV original
df = pd.read_csv(input_file)

# Dicionário de mapeamento de colunas a serem renomeadas
mapeamento_colunas = {
    "sistema_corporal_apache_3j_Genitourinary": "sistema_corporal_apache_3j_Geniturinario",
    "sistema_corporal_apache_3j_Gynecological": "sistema_corporal_apache_3j_Ginecologico",
    "sistema_corporal_apache_3j_Hematological": "sistema_corporal_apache_3j_Hematologico",
    "sistema_corporal_apache_3j_Metabolic": "sistema_corporal_apache_3j_Metabolico",
    "sistema_corporal_apache_3j_Nusculoskeletal/Skin": "sistema_corporal_apache_3j_Nusculoesqueletico/Pele",
    "sistema_corporal_apache_3j_Neurological": "sistema_corporal_apache_3j_Neurologico",
    "sistema_corporal_apache_2_Haematologic": "sistema_corporal_apache_2_Hematologico",
    "sistema_corporal_apache_2_Metabolic": "sistema_corporal_apache_2_Metabolico",
    "sistema_corporal_apache_2_Neurologic": "sistema_corporal_apache_2_Neurologico",
    "sistema_corporal_apache_2_Renal/Genitourinary": "sistema_corporal_apache_2_Renal/Geniturinario",
    "sistema_corporal_apache_2_Respiratory": "sistema_corporal_apache_2_Respiratorio",
    "sistema_corporal_apache_2_Undefined Diagnoses": "sistema_corporal_apache_2_Diagnosticos Indefinidos",
    "sistema_corporal_apache_2_Undefined Diagnoses_1": "sistema_corporal_apache_2_Diagnosticos_1 Indefinidos",
}

# Renomear as colunas no DataFrame
df.rename(columns=mapeamento_colunas, inplace=True)

# Salvar o DataFrame com as colunas renomeadas em um novo arquivo Parquet
df.to_parquet(output_file, index=False)

print("Colunas renomeadas e o arquivo dataset_onehot_filling_renomeadas.parquet foi criado.")