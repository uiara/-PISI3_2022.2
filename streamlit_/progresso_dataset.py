import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Carregar os dados
data = pd.read_csv('data/dataset_renamed_onehot_nonull.csv')

# Separar features e rótulo alvo
X = data.drop(columns=['morte_hospital'])
y = data['morte_hospital'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo
rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)

# Calcular a importância das características
feature_importance = rf_model.feature_importances_
feature_importance_df = pd.DataFrame({'Feature': X_train.columns, 'Importance': feature_importance})
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

# Criar página Streamlit
st.title('Visualização da Importância das Características')
st.write('Aqui estão as 10 características mais importantes para a previsão de mortalidade hospitalar:')

top_10_features = feature_importance_df.head(10)
st.dataframe(top_10_features)

# Gráfico de barras
st.write('Gráfico de Importância das Características')
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=top_10_features)
plt.xlabel('Importância')
plt.ylabel('Características')
st.pyplot(plt)