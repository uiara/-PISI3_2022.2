import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def load_data():
    return pd.read_parquet('../data/renomeado_mediana_smoteenn.parquet', engine='pyarrow')


def knn():

    df = load_data()

    df = df[['ventilado_apache','d1_frequencia_cardiaca_maxima',
             'd1_frequencia_cardiaca_minima', 'h1_frequencia_respiratoria_maxima','d1_spO2_minimo',
             'd1_temperatura_minima', 'morte_hospital']]
    df = df.dropna()

    y = df['morte_hospital']
    X = df.drop(['morte_hospital'], axis=1)
    st.title("Análise do Modelo k-Nearest Neighbors (k-NN)")

    if len(X) == 0:
        st.warning("Não há dados suficientes para treinar o modelo.")
        return

    k_value = st.slider("Selecione o valor de k (n_neighbors):", min_value=1, max_value=20, value=3)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    knn_classifier = KNeighborsClassifier(n_neighbors=k_value)  
    knn_classifier.fit(X_train, y_train)
    X_test_scaled = knn_classifier._validate_data(X_test, reset=False)
    y_pred = knn_classifier.predict(X_test_scaled)

    accuracy = accuracy_score(y_test, y_pred)

    st.subheader("Acurácia do modelo:")
    st.text(f"{accuracy:.2f}")

    st.subheader("Relatório de Classificação:")
    st.text(classification_report(y_test, y_pred))

    st.subheader("Matriz de Confusão:")
    cm = confusion_matrix(y_test, y_pred)

    st.write("Matriz de Confusão:")
    st.write(cm)
