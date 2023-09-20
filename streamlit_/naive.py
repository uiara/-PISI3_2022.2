import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix

st.title('Classificação com Naive Bayes')
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

nb_model = train_naive_bayes()

y_pred = nb_model.predict(X_test)
#f1
st.subheader('Relatório de Classificação:')
report = classification_report(y_test, y_pred)
st.text(report)

st.subheader('Matriz de Confusão:')
cm = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots()
sns.heatmap(cm, annot=True, fmt="d", cmap="YlGnBu", cbar=False, square=True, ax=ax) 
ax.set_xlabel('Previsto', fontsize=12)
ax.set_ylabel('Real', fontsize=12)
ax.set_title('Matriz de Confusão', fontsize=16)
st.pyplot(fig)
