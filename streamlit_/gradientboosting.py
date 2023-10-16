import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report,  confusion_matrix

def gradient():
    data = pd.read_parquet("../data/renomeado_mediana_smoteenn.parquet")
    
    X = data.drop("morte_hospital", axis=1)
    y = data["morte_hospital"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    report = classification_report(y_test, y_pred)
    print("Relatório de Classificação:")
    st.text(report)

    st.text("Matriz de Confusão:")
    cm = confusion_matrix(y_test, y_pred)
    st.text(cm)
