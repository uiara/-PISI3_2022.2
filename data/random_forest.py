import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_parquet('/home/bianka/PISI3_2022.2/data/dataset_renomeado.parquet')
df = df[['ventilado_apache','tipo_estadia_uti', 'd1_frequencia_cardiaca_maxima',
         'd1_frequencia_cardiaca_minima', 'h1_frequencia_respiratoria_maxima',
         'd1_spO2_minimo','d1_temperatura_minima', 'morte_hospital']]
df = df.dropna()

one_hot_encoded = pd.get_dummies(df['tipo_estadia_uti'])
df = pd.concat([df, one_hot_encoded], axis=1)

def categorizar_fc_maxima(fc):
    if fc < 60:
        return 'primeiras_24_horas_frequencia_cardiaca_maxima_muito_baixa'
    elif 60 <= fc < 70:
        return 'primeiras_24_horas_frequencia_cardiaca_maxima_baixa'
    elif 70 <= fc < 100:
        return 'primeiras_24_horas_frequencia_cardiaca_maxima_normal'
    elif 100 <= fc < 120:
        return 'primeiras_24_horas_frequencia_cardiaca_maxima_elevada'
    else:
        return 'primeiras_24_horas_frequencia_cardiaca_maxima_muito_elevada'

df['categoria_fc_maxima'] = df['d1_frequencia_cardiaca_maxima'].apply(categorizar_fc_maxima)

one_hot_encoded = pd.get_dummies(df['categoria_fc_maxima'])

df = pd.concat([df, one_hot_encoded], axis=1)

df = df.drop('categoria_fc_maxima', axis=1)