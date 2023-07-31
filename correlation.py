import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Carregar o dataset no formato Parquet
data = pd.read_csv('dataset_renomeado_onehot_sem_nulos.csv')

# Separar features e rótulo alvo
X = data.drop(columns=['morte_hospital'])  # Features
y = data['morte_hospital']  # Rótulo alvo

# Dividir o dataset em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instanciar o modelo Random Forest
rf_model = RandomForestClassifier()

# Treinar o modelo
rf_model.fit(X_train, y_train)

# Obter a importância das características
feature_importance = rf_model.feature_importances_

# Criar um DataFrame para visualização
feature_importance_df = pd.DataFrame({'Feature': X_train.columns, 'Importance': feature_importance})
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

# Visualizar a importância das características
top_10_features = feature_importance_df.head(10)
print(top_10_features)