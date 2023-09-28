import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from imblearn.combine import SMOTEENN 

def load_data():

    data = pd.read_parquet("../data/decisionTree_dataset.parquet")
    data = data[['ventilado_apache','d1_frequencia_cardiaca_maxima',
         'd1_frequencia_cardiaca_minima', 'h1_frequencia_respiratoria_maxima','h1_frequencia_respiratoria_minima',
         'd1_spO2_maximo', 'd1_spO2_minimo','d1_temperatura_maxima','d1_temperatura_minima', 'morte_hospital']]
    return data


def DecisionTree():
    st.title("Análise do Árvore de Decisão")
    st.sidebar.header("Configurações")

    data = load_data()
    features = st.sidebar.multiselect("Selecione as colunas de recursos", data.columns, 'morte_hospital')
    target = "morte_hospital"

    X_train, X_test, y_train, y_test = train_test_split(data[features], data[target], test_size=0.33, random_state=42)

    sampler = SMOTEENN(sampling_strategy='auto', random_state=42)
    X_resampled, y_resampled = sampler.fit_resample(X_train, y_train)


    # Hiperparâmetros
    max_depth = st.sidebar.slider("Profundidade máxima da árvore", 1, 20, 3)

    # Treinar o modelo
    model = DecisionTreeClassifier(max_depth=max_depth)
    model.fit(X_resampled, y_resampled)

    # Avaliar o modelo
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    st.header("Avaliação do Modelo")
    st.write("Acurácia:", accuracy)

    st.subheader("Relatório de Classificação")
    class_report = classification_report(y_test, y_pred, target_names=["Sobreviveu", "Morreu"])
    st.text(class_report)

    st.subheader("Matriz de Confusão")
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    st.pyplot(plt)

if __name__ == "__main__":
    DecisionTree()
