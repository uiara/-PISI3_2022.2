import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report,  confusion_matrix

data = pd.read_parquet("../data/renomeado_mediana_smoteenn.parquet")
   
X = data.drop("morte_hospital", axis=1)
y = data["morte_hospital"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

print("Treinando o modelo SVM com SMOTEENN...")
model = SVC(C=1.0, kernel='rbf', random_state=42)  # Você pode ajustar os hiperparâmetros aqui
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Exibir métricas de avaliação
st.text("Relatório de Classificação:")
report = classification_report(y_test, y_pred)
st.text(report)

# Visualizar a matriz de confusão
print("Matriz de Confusão:")
cm = confusion_matrix(y_test, y_pred)
st.text(cm)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.xlabel("Previsto")
plt.ylabel("Real")
plt.show()
