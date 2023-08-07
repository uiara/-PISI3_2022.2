import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

data = pd.read_csv('data/dataset_renomeado_onehot_nonull.csv')

# Separar features e rótulo alvo
X = data.drop(columns=['probabilidade_morte_na_uti_(apache_4a)'])
y = data['probabilidade_morte_na_uti_(apache_4a)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar e treinar o modelo de regressão linear
reg_model = LinearRegression()
reg_model.fit(X_train, y_train)

# DataFrame para visualização dos coeficientes
coef_df = pd.DataFrame({'Feature': X_train.columns, 'Coefficient': reg_model.coef_})
coef_df = coef_df.sort_values(by='Coefficient', ascending=False)

top_10_features = coef_df.head(10)
print(top_10_features)