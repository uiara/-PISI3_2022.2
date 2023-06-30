import streamlit as st

def dic():

    dic =[
        {
            'Número': 1,
            'Coluna': 'id_encontro',
            'Descrição': 'Identificador exclusivo associado a uma estadia na unidade do paciente'
        },
        {
            'Número': 2,
            'Coluna': 'id_paciente',
            'Descrição': 'Identificador único associado a um paciente'
        },
        {
            'Número': 3,
            'Coluna': 'id_hospital',
            'Descrição': 'Identificador único associado a um hospital'
        },
        {
            'Número': 4,
            'Coluna': 'idade',
            'Descrição': 'A idade do paciente na admissão na unidade'
        },
        {
            'Número': 5,
            'Coluna': 'imc',
            'Descrição': 'O índice de massa corporal da pessoa na admissão na unidade'
        },
        {
            'Número': 6,
            'Coluna': 'cirurgia_eletiva',
            'Descrição': 'Se o paciente foi internado no hospital para uma operação cirúrgica eletiva'
        },
        {
            'Número': 7,
            'Coluna': 'etnia',
            'Descrição': 'A tradição nacional ou cultural comum à qual a pessoa pertence'
        },
        {
            'Número': 8,
            'Coluna': 'genero',
            'Descrição': 'Sexo do paciente'
        },
        {
            'Número': 9,
            'Coluna': 'altura',
            'Descrição': 'A altura da pessoa na admissão da unidade'
        },
        {
            'Número': 10,
            'Coluna': 'fonte_admissao_uti',
            'Descrição': 'A localização do paciente antes de ser admitido na unidade'
        },
        {
            'Número': 11,
            'Coluna': 'id_uti',
            'Descrição': 'Um identificador único para a unidade em que o paciente foi internado'
        },
        {
            'Número': 12,
            'Coluna': 'tipo_estadia_uti',
            'Descrição': 'Se o paciente foi internado ou transferido'
        },
        {
            'Número': 13,
            'Coluna': 'tipo_uti',
            'Descrição': 'Classificação que indica o tipo de atendimento que a unidade é capaz de prestar'
        },
        {
            'Número': 14,
            'Coluna': 'dias_de_permanencia_pre_uti',
            'Descrição': 'O tempo de permanência do paciente entre a internação hospitalar e a internação na unidade'
        },
        {
            'Número': 15,
            'Coluna': 'peso',
            'Descrição': 'O peso (massa corporal) da pessoa na admissão na unidade'
        },
        {
            'Número': 16,
            'Coluna': 'diagnostico_pache_2',
            'Descrição': 'O diagnóstico APACHE II para admissão na UTI'
        },
        {
            'Número': 17,
            'Coluna': 'apache_3j_diagnostico',
            'Descrição': 'O código de subdiagnóstico APACHE III-J que melhor descreve o motivo da admissão na UTI'
        },
        {
            'Número': 18,
            'Coluna': 'status_operativo_pache',
            'Descrição': 'O status operativo do APACHE; 1 para pós-operatório, 0 para não-operatório'
        },
        {
            'Número': 19,
            'Coluna': 'arf_pache',
            'Descrição': 'Se o paciente teve insuficiência renal aguda durante as primeiras 24 horas de permanência na unidade'
        },
        {
            'Número': 20,
            'Coluna': 'abertura_ocular_pache',
            'Descrição': 'O componente de abertura ocular da Escala de Coma de Glasgow medido durante as primeiras 24 horas'
        },
        {
            'Número': 21,
            'Coluna': 'componente_motor_pache',
            'Descrição': 'O componente motor da Escala de Coma de Glasgow medido durante as primeiras 24 horas'
        },
        {
            'Número': 22,
            'Coluna': 'incapaz_avaliar_pache',
            'Descrição': 'Se a Escala de Coma de Glasgow não pôde ser avaliada devido à sedação do paciente'
        },
        {
            'Número': 23,
            'Coluna': 'componente_verbal_pache',
            'Descrição': 'O componente verbal da Escala de Coma de Glasgow medido durante as primeiras 24 horas'
        },
        {
            'Número': 24,
            'Coluna': 'frequencia_cardiaca_pache',
            'Descrição': 'A frequência cardíaca medida durante as primeiras 24 horas'
        },
        {
            'Número': 25,
            'Coluna': 'intubado_pache',
            'Descrição': 'Se o paciente foi intubado no momento da gasometria arterial de maior pontuação'
        },
        {
            'Número':26,
            'Coluna': 'map_apache',
            'Descrição': 'A pressão arterial média medida durante as primeiras 24 horas'
        },
        {
            'Número':27,
            'Coluna': 'frequencia_respiratoria_pache',
            'Descrição':'A frequência respiratória medida durante as primeiras 24 horas'
        },
        {
            'Número':28,
            'Coluna': 'temperatura_apache',
            'Descrição':'A temperatura medida durante as primeiras 24 horas'
        },
        {
            'Número':29,
            'Coluna': 'ventilado_apache',
            'Descrição':'Se o paciente foi ventilado de forma invasiva no momento da gasometria arterial de maior pontuação'
        },
        {
            'Número':30,
            'Coluna': 'd1_pressao_arterial_diastolica_maxima',
            'Descrição':'A pressão arterial diastólica mais alta do paciente durante as primeiras 24 horas de permanência na unidade, medida de forma não invasiva ou invasiva'
        },
        {
            'Número':31,
            'Coluna': 'd1_pressao_arterial_diastolica_minima',
            'Descrição':'A pressão arterial diastólica mais baixa do paciente durante as primeiras 24 horas de permanência na unidade, medida de forma não invasiva ou invasiva'
        },
        {
            'Número':32,
            'Coluna': 'd1_pressao_arterial_diastolica_nao_invasiva_maxima',
            'Descrição':'A pressão arterial diastólica mais alta do paciente durante as primeiras 24 horas de permanência na unidade, medida de forma não invasiva'
        },
        {
            'Número':33,
            'Coluna': 'd1_pressao_arterial_diastólica_nao_invasiva_minima',
            'Descrição':'A pressão arterial diastólica mais baixa do paciente durante as primeiras 24 horas de permanência na unidade, medida de forma não invasiva'
        },
        {
            'Número':34,
            'Coluna': 'd1_frequencia_cardiaca_maxima',
            'Descrição':'A frequência cardíaca mais alta do paciente durante as primeiras 24 horas de permanência na unidade'
        },
        {
            'Número':35,
            'Coluna': 'd1_frequencia_cardiaca_minima',
            'Descrição':'A frequência cardíaca mais baixa do paciente durante as primeiras 24 horas de permanência na unidade'
        },
        {
            'Número':36,
            'Coluna':  'd1_pressao_arterial_media_maxima',
            'Descrição':'A pressão arterial média mais alta do paciente durante as primeiras 24 horas de permanência na unidade, medida de forma não invasiva ou invasiva'
        },
        {
            'Número':37,
            'Coluna': 'd1_pressao_arterial_media_minima',
            'Descrição':'A pressão arterial média mais baixa do paciente durante as primeiras 24 horas de permanência na unidade, medida de forma não invasiva ou invasiva'
        },
        {
            'Número':38,
            'Coluna': 'd1_pressao_arterial_media_nao_invasiva_maxima',
            'Descrição':'A pressão arterial média mais alta do paciente durante as primeiras 24 horas de permanência na unidade, medida de forma não invasiva'
        },
        {
            'Número':39,
            'Coluna': 'd1_pressao_arterial_media_nao_invasiva_minima',
            'Descrição':'A pressão arterial média mais baixa do paciente durante as primeiras 24 horas de permanência na unidade, medida de forma não invasiva'
        },
        {
            'Número':40,
            'Coluna': 'd1_frequencia_respiratoria_maxima',
            'Descrição':'A frequência respiratória mais alta do paciente durante as primeiras 24 horas de permanência na unidade'
        },
        {
            'Número':41,
            'Coluna': 'd1_frequencia_respiratoria_minima',
            'Descrição':'A frequência respiratória mais baixa do paciente durante as primeiras 24 horas de permanência na unidade'
        },
        {
            'Número':42,
            'Coluna': 'd1_spO2_maximo',
            'Descrição':'A maior saturação periférica de oxigênio do paciente durante as primeiras 24 horas de permanência na unidade'
        },
        {
            'Número':43,
            'Coluna': 'd1_spO2_minimo',
            'Descrição':'A saturação periférica de oxigênio mais baixa do paciente durante as primeiras 24 horas de permanência na unidade'
        },
        {
            'Número':44,
            'Coluna': 'd1_pressao_arterial_sistolica_maxima',
            'Descrição':'A pressão arterial sistólica mais alta do paciente durante as primeiras 24 horas de permanência na unidade, medida de forma não invasiva ou invasiva'
        },
        {
            'Número':45,
            'Coluna': 'd1_pressao_arterial_sistolica_minima',
            'Descrição':'A pressão arterial sistólica mais baixa do paciente durante as primeiras 24 horas de permanência na unidade, medida de forma não invasiva ou invasiva'
        },
        {
            'Número':46,
            'Coluna': 'd1_pressao_arterial_sistolica_nao_invasiva_maxima',
            'Descrição':'A pressão arterial sistólica mais alta do paciente durante as primeiras 24 horas de permanência na unidade, medida de forma não invasiva'
        },
        {
            'Número':47,
            'Coluna': 'd1_pressao_arterial_sistolica_nao_invasiva_minima',
            'Descrição':'A pressão arterial sistólica mais baixa do paciente durante as primeiras 24 horas de internação na unidade, medida de forma invasiva'
        },
        {
            'Número':48,
            'Coluna': 'd1_temperatura_maxima',
            'Descrição':'A temperatura central mais alta do paciente durante as primeiras 24 horas de permanência na unidade, medida de forma invasiva'
        },
        {
            'Número':49,
            'Coluna': 'd1_temperatura_minima',
            'Descrição':'A temperatura central mais baixa do paciente durante as primeiras 24 horas de permanência na unidade'
        },
        {
            'Número':50,
            'Coluna': 'h1_pressão_arterial_diastolica_maxima',
            'Descrição':'A pressão arterial diastólica mais alta do paciente durante a primeira hora de permanência na unidade, medida de forma não invasiva ou invasiva'
        },
        {
            'Número':51,
            'Coluna': 'h1_pressao_arterial_iastolica_minima',
            'Descrição':'A pressão arterial diastólica mais baixa do paciente durante a primeira hora de permanência na unidade, medida de forma não invasiva ou invasiva'
        },
        {
            'Número':52,
            'Coluna': 'd1_pressao_arterial_diastolica_nao_invasiva_maxima',
            'Descrição':'A pressão arterial diastólica mais alta do paciente durante a primeira hora de permanência na unidade, medida de forma invasiva'
        },
        {
            'Número':53,
            'Coluna': 'd1_pressao_arterial_diastólica_nao_invasiva_minima',
            'Descrição':'A pressão arterial diastólica mais baixa do paciente durante a primeira hora de permanência na unidade, medida de forma invasiva'
        },
        {
            'Número':54,
            'Coluna': 'd1_frequencia_cardiaca_maxima',
            'Descrição':'A frequência cardíaca mais alta do paciente durante a primeira hora de permanência na unidade'
        },
        {
            'Número':55,
            'Coluna':  'd1_frequencia_cardiaca_minima',
            'Descrição':'A frequência cardíaca mais baixa do paciente durante a primeira hora de permanência na unidade'
        },
        {
            'Número':56,
            'Coluna': 'd1_pressao_arterial_media_maxima',
            'Descrição':'A pressão arterial média mais alta do paciente durante a primeira hora de permanência na unidade, medida de forma não invasiva ou invasiva'
        },
        {
            'Número':57,
            'Coluna': 'd1_pressao_arterial_media_minima',
            'Descrição':'A pressão arterial média mais baixa do paciente durante a primeira hora de permanência na unidade, medida de forma não invasiva ou invasiva'
        },
        {
            'Número':58,
            'Coluna': 'pressão arterial_media_nao_invasiva_maxima',
            'Descrição':'A pressão arterial média mais alta do paciente durante a primeira hora de permanência na unidade, medida de forma não invasiva'
        },
        {
            'Número':59,
            'Coluna': 'pressão arterial_media_nao_invasiva_minima',
            'Descrição':'A pressão arterial média mais baixa do paciente durante a primeira hora de permanência na unidade, medida de forma não invasiva'
        },
        {
            'Número':60,
            'Coluna': 'frequencia_respiratoria_maxima',
            'Descrição':'A frequência respiratória mais alta do paciente durante a primeira hora de permanência na unidade'
        },
        {
            'Número':61,
            'Coluna': 'frequencia_respiratoria_minima',
            'Descrição':'A frequência respiratória mais baixa do paciente durante a primeira hora de permanência na unidade'
        },
        {
            'Número':62,
            'Coluna': 'h1_spO2_max',
            'Descrição':'A maior saturação periférica de oxigênio do paciente durante a primeira hora de permanência na unidade'
        },
        {
            'Número':63,
            'Coluna': 'h1_spO2_min',
            'Descrição':'A menor saturação periférica de oxigênio do paciente durante a primeira hora de permanência na unidade'
        },
        {
            'Número':64,
            'Coluna': 'h1_pressao_arterial_sistolica_maxima',
            'Descrição':'A pressão arterial sistólica mais alta do paciente durante a primeira hora de permanência na unidade, medida de forma não invasiva ou invasiva'
        },
        {
            'Número':65,
            'Coluna': 'h1_pressao_arterial_sistolica_minima',
            'Descrição':'A pressão arterial sistólica mais baixa do paciente durante a primeira hora de permanência na unidade, medida de forma não invasiva ou invasiva'
        },
        {
            'Número':66,
            'Coluna': 'h1_pressao_arterial_sistolica_nao_invasiva_maxima',
            'Descrição':'A pressão arterial sistólica mais alta do paciente durante a primeira hora de permanência na unidade, medida de forma não invasiva'
        },
        {
            'Número':67,
            'Coluna': 'h1_pressao_arterial_sistolica_nao_invasiva_minima',
            'Descrição':'A pressão arterial sistólica mais baixa do paciente durante a primeira hora de permanência na unidade, medida de forma não invasiva'
        },
        {
            'Número':68,
            'Coluna': 'd1_gricose_maxima',
            'Descrição':'A maior concentração de glicose do paciente em seu soro ou plasma durante as primeiras 24 horas de permanência na unidade'
        },
        {
            'Número':69,
            'Coluna': 'd1_gricose_minima',
            'Descrição':'A menor concentração de glicose do paciente em seu soro ou plasma durante as primeiras 24 horas de internação'
        },
        {
            'Número':70,
            'Coluna': 'd1_potassio_maximo',
            'Descrição':'A maior concentração de potássio para o paciente em seu soro ou plasma durante as primeiras 24 horas de permanência na unidade'
        },
        {
            'Número':71,
            'Coluna': 'd1_potassio_minimo',
            'Descrição':'A menor concentração de potássio para o paciente em seu soro ou plasma durante as primeiras 24 horas de permanência na unidade'
        },
        {
            'Número':72,
            'Coluna': 'probabilidade_de_morte_no_hospital_(apache_4a)',
            'Descrição':'A previsão probabilística APACHE IVa de mortalidade intra-hospitalar para o paciente que utiliza o escore APACHE III e outras covariáveis, incluindo o diagnóstico'
        },
        {
            'Número':73,
            'Coluna': 'probabilidade_morte_na_uti_(apache_4a)',
            'Descrição':'A previsão probabilística APACHE IVa de mortalidade na UTI para o paciente que utiliza o escore APACHE III e outras covariáveis, incluindo diagnóstico'
        },
        {
            'Número':74,
            'Coluna': 'aids',
            'Descrição':'Se o paciente tem um diagnóstico definitivo de síndrome da imunodeficiência adquirida (AIDS) (não somente HIV positivo)'
        },
        {
            'Número':75,
            'Coluna': 'cirrose',
            'Descrição':'Se o paciente tem uma história de uso pesado de álcool com hipertensão portal e varizes, outras causas de cirrose com evidência de hipertensão portal e varizes ou cirrose comprovada por biópsia. Essa comorbidade não se aplica a pacientes com transplante hepático funcionante'
        },
        {
            'Número':76,
            'Coluna': 'diabetes_mellitus',
            'Descrição':'Se o paciente foi diagnosticado com diabetes, juvenil ou adulto, que requer medicação'
        },
        {
            'Número':77,
            'Coluna': 'insuficiencia_hepatica',
            'Descrição':'Se o paciente tem cirrose e complicações adicionais, incluindo icterícia e ascite, sangramento gastrointestinal superior, encefalopatia hepática ou coma'
        },
        {
            'Número':78,
            'Coluna': 'imunossupressao',
            'Descrição':'Se o paciente teve seu sistema imunológico suprimido nos seis meses anteriores à admissão na UTI por qualquer um dos seguintes motivos: radioterapia, quimioterapia, uso de drogas imunossupressoras não citotóxicas, esteróides em altas doses (pelo menos 0,3 mg/kg/dia de metilprednisolona ou equivalente por pelo menos 6 meses)'
        },
        {
            'Número':79,
            'Coluna': 'leucemia',
            'Descrição':'Se o paciente foi diagnosticado com leucemia mielóide aguda ou crônica, leucemia linfocítica aguda ou crônica ou mieloma múltiplo'
        },
        {
            'Número':80,
            'Coluna': 'linfoma',
            'Descrição':'Se o paciente foi diagnosticado com linfoma não-Hodgkin'
        },
        {
            'Número':81,
            'Coluna': 'tumor_solido_com_metastase',
            'Descrição':'Se o paciente foi diagnosticado com qualquer carcinoma de tumor sólido (incluindo melanoma maligno) que tenha evidência de metástase'
        },
        {
            'Número':82,
            'Coluna': 'sistema_corporal_apache_3j',
            'Descrição':'Grupo de diagnóstico de admissão para APACHE III'
        },
        {
            'Número':83,
            'Coluna': 'sistema_corporal_apache_2',
            'Descrição':'Grupo de diagnóstico de admissão para APACHE II'
        },
        {
            'Número':84,
            'Coluna': 'Unnamed: 83',
            'Descrição':'Sem descrição'
        },
        {
            'Número':85,
            'Coluna': 'morte_hospital',
            'Descrição':'Se o paciente morreu durante esta hospitalização'
        }
    ]


    
    
    
    
    
    
    
    
    
    st.markdown("### Dicionário de Dados")
    st.markdown("| Número | Coluna | Descrição |\n| --- | --- | --- |\n" + "\n".join([f"| {item['Número']} | {item['Coluna']} | {item['Descrição']} |" for item in dic]))

