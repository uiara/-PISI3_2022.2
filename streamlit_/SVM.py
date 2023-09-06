import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report,  confusion_matrix
from imblearn.combine import SMOTEENN  # Importe o SMOTEENN

# Carregar o conjunto de dados
@st.cache_data
def load_data():

    data = pd.read_parquet("C:/Users/leogo/OneDrive/Área de Trabalho/PISI3_2022.2-main/data/decisionTree_dataset.parquet")
    data = data[['ventilado_apache','d1_frequencia_cardiaca_maxima',
         'd1_frequencia_cardiaca_minima', 'h1_frequencia_respiratoria_maxima','h1_frequencia_respiratoria_minima',
         'd1_spO2_maximo', 'd1_spO2_minimo','d1_temperatura_maxima','d1_temperatura_minima', 'morte_hospital']]
    return data

#interface
def svm():
    data = load_data()

    # Definir as features (X) e a coluna alvo (y)
    X = data.drop("morte_hospital", axis=1)
    y = data["morte_hospital"]

    # Dividir o conjunto de dados em treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Aplicar o SMOTEENN para balancear as classes
    smoteenn = SMOTEENN(random_state=42)
    X_resampled, y_resampled = smoteenn.fit_resample(X_train, y_train)

    # Criar um aplicativo Streamlit
    st.title("Aplicativo SVM para Prever Mortes Hospitalares")

    # Definir hiperparâmetros
    C = st.slider("Parâmetro C (Regularização)", 0.01, 10.0, 1.0)
    kernel = st.selectbox("Kernel", ("linear", "poly", "rbf", "sigmoid"))

   # Treinar o modelo SVM com os dados resampleados
    st.write("Treinando o modelo SVM com SMOTEENN...")
    model = SVC(C=C, kernel=kernel, random_state=42)
    model.fit(X_resampled, y_resampled)

    # Fazer previsões no conjunto de teste
    y_pred = model.predict(X_test)

    # Exibir métricas de avaliação
    st.write("Relatório de Classificação:")
    report = classification_report(y_test, y_pred)
    st.write(report)

    # Visualizar a matriz de confusão
    st.write("Matriz de Confusão:")
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
    plt.xlabel("Previsto")
    plt.ylabel("Real")
    st.pyplot(plt)

    # Previsão para um exemplo
    st.sidebar.title("Previsão para um Exemplo")
    example = {}
    for feature in X.columns:
        example[feature] = st.sidebar.number_input(f"Insira o valor para {feature}", min_value=0)

    if st.sidebar.button("Prever"):
        example_df = pd.DataFrame([example])
        prediction = model.predict(example_df)
        if prediction[0] == 0:
            st.sidebar.write("Previsão: Sobreviveu")
        else:
            st.sidebar.write("Previsão: Morreu")
