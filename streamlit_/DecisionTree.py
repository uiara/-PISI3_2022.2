import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o conjunto de dados
@st.cache_data
def load_data():

    data = pd.read_csv("C:/Users/leogo/OneDrive/Área de Trabalho/PISI3_2022.2-main/data/decisionTree_dataset.csv")
    colunas_deletar = ['id_ncontro', 'id_paciente', 'id_hospital','id_uti']
    data = data.drop(columns=colunas_deletar)
    return data

# Interface
def DecisionTree():
    st.title("Análise do Árvore de Decisão")
    st.sidebar.header("Configurações")

    # Carregar os dados
    data = load_data()

    # Selecionar colunas para recursos e alvo
    features = st.sidebar.multiselect("Selecione as colunas de recursos", data.columns)
    target = "morte_hospital"

    # Dividir o conjunto de dados em treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(data[features], data[target], test_size=0.2, random_state=42)

    # Hiperparâmetros
    max_depth = st.sidebar.slider("Profundidade máxima da árvore", 1, 20, 3)

    # Treinar o modelo
    model = DecisionTreeClassifier(max_depth=max_depth)
    model.fit(X_train, y_train)

    # Avaliar o modelo
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    st.header("Avaliação do Modelo")
    st.write("Acurácia:", accuracy)

    # Relatório de Classificação
    st.subheader("Relatório de Classificação")
    class_report = classification_report(y_test, y_pred, target_names=["Sobreviveu", "Morreu"])
    st.text(class_report)

    # Matriz de Confusão
    st.subheader("Matriz de Confusão")
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    st.pyplot(plt)

if __name__ == "__main__":
    DecisionTree()
