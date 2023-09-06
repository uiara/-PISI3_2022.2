import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report,  confusion_matrix


# Carregar o conjunto de dados

def load_data():

    data = pd.read_parquet("C:/Users/leogo/OneDrive/Área de Trabalho/PISI3_2022.2-main/data/renomeado_mediana_smoteenn.parquet")
   
    return data

data = load_data()

# Definir as features (X) e a coluna alvo (y)
X = data.drop("morte_hospital", axis=1)
y = data["morte_hospital"]

# Dividir o conjunto de dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Treinar o modelo SVM com os dados resampleados
print("Treinando o modelo SVM com SMOTEENN...")
model = SVC(C=1.0, kernel='rbf', random_state=42)  # Você pode ajustar os hiperparâmetros aqui
model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = model.predict(X_test)

# Exibir métricas de avaliação
print("Relatório de Classificação:")
report = classification_report(y_test, y_pred)
print(report)

# Visualizar a matriz de confusão
print("Matriz de Confusão:")
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.xlabel("Previsto")
plt.ylabel("Real")
plt.show()
