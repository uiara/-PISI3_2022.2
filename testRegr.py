from dicionario_dados import dic

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error, r2_score



def regressor():
    st.title('Treinamento do modelo através de Regressão')
    df = pd.read_parquet("data/dataset_renomeado.parquet")

    sel_col, dis_col = st.columns(2)

    #comprimento do caminho mais longo da raiz da árvore até a folha.
    max_depth = sel_col.slider("Profundidade máxima do modelo?", min_value=10, max_value=100, value=50, step=10)

    #n_estimators : Este é o número de árvores que você deseja construir antes de obter a votação máxima ou as médias das previsões. 
    # Quanto maior o número de árvores melhor o desempenho, mas torna o código mais lento.
    n_estimators = sel_col.selectbox("Quantas árvores terá o modelo?", options=[100,200,300,'Sem limites'], index = 0)

    sel_col.text("Estas são as features (colunas) do dataset:")
    sel_col.write(df.columns)

    input_features = sel_col.text_input("Qual coluna deve ser usada como input features?", 'apache_pos_operatorio')

    df[input_features] = df[input_features].apply(int)
    df[input_features] = np.reshape(df[input_features](1,df[input_features].size))
     
    if n_estimators == 'Sem limites':
        regr = RandomForestRegressor(max_depth=max_depth)
    else:
        regr = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)

    #fazendo a conversão para int
    df[input_features] = df[input_features].apply(int)

    #feature que iremos adicionar para comparação
    x = df[input_features]
    #fearture que iremos usar como base para o output
    df['morte_hospital'] = df['morte_hospital'].apply(int)
    y = df["morte_hospital"].apply(int)
    y = pd.factorize(df['morte_hospital'](1,df['morte_hospital'].size))

    regr.fit(x,y)
    prediction = regr.predict(y)
    
    #
    dis_col.subheader('Mean absolute error of the model is:')
    dis_col.write(mean_absolute_error(y, prediction))

    #
    dis_col.subheader('Mean absolute porcentage error of the model is:')
    dis_col.write(mean_absolute_percentage_error(y,prediction))

    #A função mean_squared_error calcula o erro quadrático médio, uma métrica de risco correspondente ao valor esperado do erro ao quadrado (quadrático) ou perda.
    dis_col.subheader('Mean square error of the model is:')
    dis_col.write(mean_squared_error(y, prediction))

    #
    dis_col.subheader('Mean r2_error of the model is:')
    dis_col.write(r2_score(y,prediction))

# Seletor de página
pages = {
    'Página 1 - teste': regressor
}

# Título
st.title('Patient Survival Prediction')

# Seletor de página na barra lateral
page = st.sidebar.selectbox('Selecione a página', tuple(pages.keys()))

# Renderiza a página selecionada
pages[page]()
