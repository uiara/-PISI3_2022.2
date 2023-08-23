import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from imblearn.under_sampling import RandomUnderSampler



# Carregar o conjunto de dados
@st.cache_data
def load_data():

    data = pd.read_parquet("C:/Users/leogo/OneDrive/Área de Trabalho/PISI3_2022.2-main/data/decisionTree_dataset.parquet")
    colunas_deletar = ['id_ncontro','id_paciente','id_hospital','id_uti','altura','peso','cirurgia_eletiva','genero_M'
                       ,'etnia_Asian','etnia_Caucasian','etnia_Hispanic','etnia_Native American','etnia_Other/Unknown'
                       ,'tipo_uti_CSICU','tipo_uti_CTICU','tipo_uti_Cardiac ICU','tipo_uti_MICU','tipo_uti_Med-Surg ICU'
                       ,'tipo_uti_Neuro ICU', 'tipo_uti_SICU','gcs_olhos_apache','gcs_motor_apache','gcs_incapaz_apache'
                       ,'gcs_verbal_pache','arf_apache']
    data = data.drop(columns=colunas_deletar)
    return data


# Interface
def DecisionTree():


    st.title("Análise do Árvore de Decisão")
    st.sidebar.header("Configurações")

    # Carregar os dados
    data = load_data()

    # Selecionar colunas para recursos e alvo
    features = st.sidebar.multiselect("Selecione as colunas de recursos", data.columns, "imc")
    target = "morte_hospital"

    # Dividir o conjunto de dados em treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(data[features], data[target], test_size=0.2, random_state=42)


    # Aplicar undersampling nas classes majoritárias
    undersampler = RandomUnderSampler(random_state=42)
    X_resampled, y_resampled = undersampler.fit_resample(X_train, y_train)


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
