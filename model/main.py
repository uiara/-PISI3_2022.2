#Algorítmo de regressão logística usando o sklearn

import pandas as pd
import pickle as pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
#divisão dos dados que serão usados e dados de resultado
def create_model(data):
    X = data.drop(['hospital_death'], axis = 1)
    Y = data['hospital_death']

#escalonamento basico
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
#divis~]ao em dados de teste e de treino
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
)

    model = LogisticRegression()
    model.fit(X_train, Y_train)

    #testar_modelo (regressão logística)
    Y_pred = model.predict(X_test)
    
    print('Precisão do modelo: ', accuracy_score(Y_test, Y_pred))
    
    print("relatorio de classificação: \n", classification_report(Y_test, Y_pred))
    return model, scaler


#faxina
def get_clean_data():
    data = pd.read_csv("data/dataset.csv")
#remover colunas irrelevantes
    data = data.drop(['encounter_id','patient_id','hospital_id','ethnicity', 'gender', 'icu_admit_source','icu_stay_type','icu_type','apache_3j_bodysystem','apache_2_bodysystem','Unnamed: 83'], axis=1)
    data = data.dropna(axis=0)
    


    return data

 

def main():
    data = get_clean_data()
    
    model, scaler = create_model(data)

    with open('model/model.pkl', 'wb')as f:
        pickle.dump(model,f)
    with open('model/scaler.pkl', 'wb')as f:
        pickle.dump(scaler,f)




if __name__ == '__main__':
    main()