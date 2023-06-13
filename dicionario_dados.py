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
            'Descrição': '...'
        },
        {
            'Número':27,
            'Coluna': 'frequencia_respiratoria_pache',
            'Descrição':'...'
        },
        {
            'Número':28,
            'Coluna': 'temperatura_apache',
            'Descrição':'...'
        },
        {
            'Número':29,
            'Coluna': 'ventilado_apache',
            'Descrição':'...'
        },
        {
            'Número':30,
            'Coluna': 'd1_pressao_arterial_diastolica_maxima',
            'Descrição':'...'
        },
        {
            'Número':31,
            'Coluna': 'd1_pressao_arterial_diastolica_minima',
            'Descrição':'...'
        },
        {
            'Número':32,
            'Coluna': 'd1_pressao_arterial_diastolica_nao_invasiva_maxima',
            'Descrição':'...'
        },
        {
            'Número':33,
            'Coluna': 'd1_pressao_arterial_diastólica_nao_invasiva_minima',
            'Descrição':'...'
        },
        {
            'Número':34,
            'Coluna': 'd1_frequencia_cardiaca_maxima',
            'Descrição':'...'
        },
        {
            'Número':35,
            'Coluna': 'd1_frequencia_cardiaca_minima',
            'Descrição':'...'
        },
        {
            'Número':36,
            'Coluna':  'd1_pressao_arterial_media_maxima',
            'Descrição':'...'
        },
        {
            'Número':37,
            'Coluna': 'd1_pressao_arterial_media_minima',
            'Descrição':'...'
        },
        {
            'Número':38,
            'Coluna': 'd1_pressao_arterial_media_nao_invasiva_maxima',
            'Descrição':'...'
        },
        {
            'Número':39,
            'Coluna': 'd1_pressao_arterial_media_nao_invasiva_minima',
            'Descrição':'...'
        },
        {
            'Número':40,
            'Coluna': 'd1_frequencia_respiratoria_maxima',
            'Descrição':'...'
        },
        {
            'Número':41,
            'Coluna': 'd1_frequencia_respiratoria_minima',
            'Descrição':'...'
        },
        {
            'Número':42,
            'Coluna': 'd1_spO2_maximo',
            'Descrição':'...'
        },
        {
            'Número':43,
            'Coluna': 'd1_spO2_minimo',
            'Descrição':'...'
        },
        {
            'Número':44,
            'Coluna': 'd1_pressao_arterial_sistolica_maxima',
            'Descrição':'...'
        },
        {
            'Número':45,
            'Coluna': 'd1_pressao_arterial_sistolica_minima',
            'Descrição':'...'
        },
        {
            'Número':46,
            'Coluna': 'd1_pressao_arterial_sistolica_nao_invasiva_maxima',
            'Descrição':'...'
        },
        {
            'Número':47,
            'Coluna': 'd1_pressao_arterial_sistolica_nao_invasiva_minima',
            'Descrição':'...'
        },
        {
            'Número':48,
            'Coluna': 'd1_temperatura_maxima',
            'Descrição':'...'
        },
        {
            'Número':49,
            'Coluna': 'd1_temperatura_minima',
            'Descrição':'...'
        },
        {
            'Número':50,
            'Coluna': 'h1_pressão_arterial_diastolica_maxima',
            'Descrição':'...'
        },
        {
            'Número':51,
            'Coluna': 'h1_pressao_arterial_iastolica_minima',
            'Descrição':'...'
        },
        {
            'Número':52,
            'Coluna': 'd1_pressao_arterial_diastolica_nao_invasiva_maxima',
            'Descrição':'...'
        },
        {
            'Número':53,
            'Coluna': 'd1_pressao_arterial_diastólica_nao_invasiva_minima',
            'Descrição':'...'
        },
        {
            'Número':54,
            'Coluna': 'd1_frequencia_cardiaca_maxima',
            'Descrição':'...'
        },
        {
            'Número':55,
            'Coluna':  'd1_frequencia_cardiaca_minima',
            'Descrição':'...'
        },
        {
            'Número':56,
            'Coluna': 'd1_pressao_arterial_media_maxima',
            'Descrição':'...'
        },
        {
            'Número':57,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':58,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':59,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':60,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':61,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':62,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':63,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':64,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':65,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':66,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':67,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':68,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':69,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':70,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':71,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':72,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':73,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':74,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':75,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':76,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':77,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':78,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':79,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':80,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':81,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':82,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':83,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':84,
            'Coluna': '...',
            'Descrição':'...'
        },
        {
            'Número':85,
            'Coluna': '...',
            'Descrição':'...'
        }
    ]


    
    
    
    
    
    
    
    
    
    st.markdown("### Dicionário de Dados")
    st.markdown("| Número | Coluna | Descrição |\n| --- | --- | --- |\n" + "\n".join([f"| {item['Número']} | {item['Coluna']} | {item['Descrição']} |" for item in dic]))

