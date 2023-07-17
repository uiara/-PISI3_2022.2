import streamlit as st
import pickle as pickle
import pandas as pd
import plotly.graph_objects as go
#modelo de visualização dos dados cardiológicos obtidos no dataset
def get_clean_data():
    data = pd.read_csv("data/dataset.csv")
#remover colunas não utilizadas/a serem implementadas
    data = data.drop(['encounter_id','patient_id','hospital_id','ethnicity', 'gender', 'icu_admit_source','icu_stay_type','icu_type','apache_3j_bodysystem','apache_2_bodysystem','Unnamed: 83'], axis=1)
    data = data.dropna(axis=0)
    


    return data


def add_sidebar():
    st.sidebar.header("valores apache")


    data = get_clean_data()

    input_dic ={}

    slider_labels = [
            ("Idade", "age"),
            ("IMC","bmi"),
            ("Frequência cardíaca","heart_rate_apache"),
            ("pressão arterial média apache","map_apache"),
            ("frequencia respiratória apache","resprate_apache"),
            ("Temperatura","temp_apache"),
            ("Frequencia cardiaca maxima (1 hora)","h1_heartrate_max"),
            ("Frequencia cardiaca minima (1 hora)","h1_heartrate_min"),
            ("Frequencia cardiaca media maxima (1 dia)","d1_mbp_max"),
            ("Frequencia cardiaca media minima (1 dia)","d1_mbp_min")

    ]
#entradas são floats , coleta de inputs
    for label, key in slider_labels:
        input_dic[key] = st.sidebar.slider(
            label=label,
            min_value=float(0),
            max_value=float(data[key].max()),
            value=float(data[key].mean())
        )
    return input_dic    

def escalar_valores(input_dic):
    data = get_clean_data()

    X = data
    scaled_dic = {}
    for key, value in input_dic.items():
        max_val = X[key].max()
        min_val = X[key].min()
        escalar = (value - min_val) / (max_val - min_val)
        scaled_dic[key] = escalar

    return scaled_dic


def grafico_radar(input_data):

    input_data = escalar_valores(input_data)

    categories = ['idade','imc','frequencia_cardiaca_pache','pressão_media_apache','frequencia_respiratoria_pache','temperatura_apache','d1_frequencia_cardiaca_maxima','d1_frequencia_cardiaca_minima','d1_pressao_arterial_media_maxima','d1_pressao_arterial_media_minima']

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
      r=[
          input_data['age'],input_data['bmi'],input_data['heart_rate_apache'],input_data['map_apache'],
          input_data['resprate_apache'],input_data['temp_apache'],input_data['h1_heartrate_max'],
          input_data['h1_heartrate_min'],input_data['d1_mbp_max'],input_data['d1_mbp_min']
      ],
      theta=categories,
      fill='toself',
      name='Product A'
    ))

    fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 1]
    )),
  showlegend=False
    )
    return fig



def main():
    #print("streamlit")
    st.set_page_config(
        page_title="previsao de mortalidade",
        page_icon=": médico :",
        layout="wide",
        initial_sidebar_state="expanded"
    )
#input data é o que está sendo retornado pela sidebar
    input_data = add_sidebar()
    st.write(input_data)


    with st.container():
        st.title("Dados cardiológicos do paciente")
        st.write("insira os dados obtidos sobre o paciente na UTI")
    
    col1, col2 = st.columns([4,1])   

    with col1:
        radar_chart = grafico_radar(input_data)
        st.plotly_chart(radar_chart)
    with col2:
        st.write("coluna 2")     


if __name__ == '__main__':
    main()