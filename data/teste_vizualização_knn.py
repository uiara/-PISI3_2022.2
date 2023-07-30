import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA


df = pd.read_parquet('data/dataset_renomeado.parquet')

colunas_deletar = ['id_ncontro', 'id_paciente', 'id_hospital','id_uti']
df = df.drop(columns=colunas_deletar)

df = df[['ventilado_apache', 'd1_frequencia_cardiaca_maxima', 'h1_frequencia_respiratoria_maxima', 'morte_hospital']]
df = df.dropna()

y = df['morte_hospital']
X = df.drop(['morte_hospital'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn_classifier = KNeighborsClassifier(n_neighbors=5)  

knn_classifier.fit(X_train_scaled, y_train)


y_pred = knn_classifier.predict(X_test_scaled)


pca = PCA(n_components=2)
X_test_pca = pca.fit_transform(X_test_scaled)


X_test_pca_df = pd.DataFrame(X_test_pca, columns=['Componente 1', 'Componente 2'])
X_test_pca_df['Classe Prevista'] = y_pred


fig = px.scatter(X_test_pca_df, x='Componente 1', y='Componente 2', color='Classe Prevista',
                 title='Visualização das Classes Previstas com KNN (PCA)')
fig.show()
