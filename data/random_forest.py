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

def categorizar_fr(fr):
    if fr < 12:
        return 'primeira_hora_frequencia_respiratoria_maxima_muito_baixa'
    elif 12 <= fr < 16:
        return 'primeira_hora_frequencia_respiratoria_maxima_baixa'
    elif 16 <= fr < 20:
        return 'primeira_hora_frequencia_respiratoria_maxima_normal'
    elif 20 <= fr < 24:
        return 'primeira_hora_frequencia_respiratoria_maxima_elevada'
    else:
        return 'primeira_hora_frequencia_respiratoria_maxima_muito elevada'

df['categoria_frequencia_respiratoria_maxima'] = df['h1_frequencia_respiratoria_maxima'].apply(categorizar_fr)

one_hot_encoded = pd.get_dummies(df['categoria_frequencia_respiratoria_maxima'])

df = pd.concat([df, one_hot_encoded], axis=1)

df = df.drop('categoria_frequencia_respiratoria_maxima', axis=1)

df = df[~((df['d1_spO2_minimo'] <= 20))]

def categorize_saturacao(sat):
    if sat < 85:
        return 'saturacao_primieras_vinte_quatro_horas_minima_muito_baixa'
    elif sat < 90:
        return 'saturacao_primieras_vinte_quatro_horas_minima_baixa'
    elif sat < 95:
        return 'saturacao_primieras_vinte_quatro_horas_minima_moderada'
    elif sat < 100:
        return 'saturacao_primieras_vinte_quatro_horas_minima_boa'


df['categoria_d1_spO2_minimo'] = df['d1_spO2_minimo'].apply(categorizar_fr)

one_hot_encoded = pd.get_dummies(df['categoria_d1_spO2_minimo'])

df = pd.concat([df, one_hot_encoded], axis=1)

df = df.drop('categoria_d1_spO2_minimo', axis=1)

def categorize_temperatura(temp):
    if temp < 35:
        return 'temperatura_minima_primieras_vinte_quatro_horas_hipotermia'
    if temp < 37:
        return 'temperatura_minima_primieras_vinte_quatro_horas_normal'
    if temp >= 37:
        return 'temperatura_minima_primieras_vinte_quatro_horas_febre'
    
df['categoria_d1_temperatura_minima'] = df['d1_temperatura_minima'].apply(categorize_temperatura)

one_hot_encoded = pd.get_dummies(df['categoria_d1_temperatura_minima'])

df = pd.concat([df, one_hot_encoded], axis=1)

df = df.drop('categoria_d1_temperatura_minima', axis=1)

df = df.drop(['d1_frequencia_cardiaca_maxima',
       'd1_frequencia_cardiaca_minima', 'h1_frequencia_respiratoria_maxima',
       'd1_spO2_minimo', 'd1_temperatura_minima','tipo_estadia_uti'], axis=1)


X = df.iloc[:, :-1]  
y = df.iloc[:, -1]  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

random_forest = RandomForestClassifier(n_estimators=100, random_state=42)

random_forest.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = random_forest.predict(X_test)

# Calcular a acurácia das previsões
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Matriz de Confusão
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

# Relatório de Classificação
class_report = classification_report(y_test, y_pred)
print("Classification Report:")
print(class_report)
