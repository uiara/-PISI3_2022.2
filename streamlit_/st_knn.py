import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def load_data():
    return pd.read_csv('/home/bianka/PISI3_2022.2/data/dataset_renamed_onehot_nonull.csv')


def preprocess_data(df):
    df = df[['ventilado_apache','probabilidade_morte_na_uti_(apache_4a)', 'd1_frequencia_cardiaca_maxima',
             'd1_frequencia_cardiaca_minima', 'h1_frequencia_respiratoria_maxima','d1_spO2_minimo',
             'd1_temperatura_minima', 'morte_hospital']]
    df = df.dropna()

    y = df['morte_hospital']
    X = df.drop(['morte_hospital'], axis=1)

    return X, y
'''
def train_model(X_train, y_train):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    knn_classifier = KNeighborsClassifier(n_neighbors=3)
    knn_classifier.fit(X_train_scaled, y_train)

    return knn_classifier
'''
def knn():
    st.title("Análise do Modelo k-Nearest Neighbors (k-NN)")
    df = load_data()

    # Pré-processar os dados
    X, y = preprocess_data(df)

    if len(X) == 0:
        st.warning("Não há dados suficientes para treinar o modelo.")
        return

    k_value = st.slider("Selecione o valor de k (n_neighbors):", min_value=1, max_value=20, value=3)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    knn_classifier = KNeighborsClassifier(n_neighbors=k_value)  # Use the selected k_value
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





