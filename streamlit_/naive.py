import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, precision_score, recall_score, f1_score

st.title('Classificação com Naive Bayes e Random Forest')

@st.cache
def load_data():
    data = pd.read_parquet("data/renomeado_mediana_smoteenn.parquet")
    return data

data = load_data()

X = data.drop("morte_hospital", axis=1)
y = data["morte_hospital"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

st.sidebar.subheader('Hiperparâmetros do Modelo Naive Bayes')

@st.cache
def train_naive_bayes():
    nb_model = GaussianNB()
    nb_model.fit(X_train, y_train)
    return nb_model

@st.cache
def train_random_forest():
    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(X_train, y_train)
    return rf_model

nb_model = train_naive_bayes()
rf_model = train_random_forest()
y_pred_nb = nb_model.predict(X_test)
y_pred_rf = rf_model.predict(X_test)
st.subheader('Relatório de Classificação (Naive Bayes):')
report_nb = classification_report(y_test, y_pred_nb)
st.text(report_nb)
st.subheader('Relatório de Classificação (Random Forest):')
report_rf = classification_report(y_test, y_pred_rf)
st.text(report_rf)

# desempenho para o Random Forest
precision_rf = precision_score(y_test, y_pred_rf)
recall_rf = recall_score(y_test, y_pred_rf)
f1_rf = f1_score(y_test, y_pred_rf)

# desempenho para o Naive Bayes
precision_nb = precision_score(y_test, y_pred_nb)
recall_nb = recall_score(y_test, y_pred_nb)
f1_nb = f1_score(y_test, y_pred_nb)

metrics_data = pd.DataFrame({
    'Métrica': ['Precisão', 'Recall', 'F1-Score'],
    'Naive Bayes': [precision_nb, recall_nb, f1_nb],
    'Random Forest': [precision_rf, recall_rf, f1_rf]
})

# gráfico de barras para comparar 
st.subheader('Comparação das Métricas de Desempenho')
fig, ax = plt.subplots()
metrics_data.set_index('Métrica').plot(kind='bar', ax=ax)
plt.xticks(rotation=0)
plt.xlabel('Métrica')
plt.ylabel('Valor')
plt.title('Comparação das Métricas de Desempenho entre Naive Bayes e Random Forest')
st.pyplot(fig)