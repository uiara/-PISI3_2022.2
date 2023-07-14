import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
#divisão dos dados que serão usados e dados de resultado
def create_model(data):
    X = data.drop(['hospital_death'], axis = 1)
    Y = data['diagnosis']

#escalonamento basico
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
#divis~]ao em dados de teste e de treino
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
)

    model = LogisticRegression()
    model.fit(X_train, Y_train)

    #testar_modelo
    Y_pred = model.predict(X_test)
    print('Precisão do modelo: ', accuracy_score(Y_test, Y_pred))
    print("Classificação: \n", classification_report(Y_test, Y_pred))
    return model, scaler



def get_clean_data():
    data = pd.read_csv("data/dataset.csv")
#remover colunas irrelevantes
    data = data.drop(['encounter_id','patient_id','hospital_id'], axis=1)


    return data

 

def main():
    data = get_clean_data()
    
    model, scaler = create_model(data)


if __name__ == '__main__':
    main()