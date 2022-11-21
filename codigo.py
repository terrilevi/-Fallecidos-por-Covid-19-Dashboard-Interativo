import streamlit as st 
import pandas as pd
import numpy as np
import gdown
import os


st.title('Fallecidos por COVID19')

st.title('Fallecidos por COVID19')


# id = 1dSRlbtutz10Lgb4wiYPcWaK3w5QMUH8O
@st.experimental_memo
def download_data():
    #https://drive.google.com/uc?id=YOURFILEID\
    url = "https://drive.google.com/uc?id=1dSRlbtutz10Lgb4wiYPcWaK3w5QMUH8O"
    output = 'data.csv'
    gdown.download(url,output,quiet = False)

download_data()
#vamos a sacar el primer millon de datos:
data = pd.read_csv('data.csv', sep = ';', parse_dates= ['FECHA_CORTE', 'FECHA_FALLECIMIENTO'])
st.dataframe(data.head(20))
#df = df.drop(columns = ["FECHA_CORTE","FECHA_FALLECIMIENTO","EDAD_DECLARADA","SEXO", "CLASIFICACION_DEF", "DEPARTAMENTO", "PROVINCIA", "DISTRITO", "UBIGEO", "UUID"])


#edad = np.sort(df['EDAD_DECLARADA'].dropna().unique())          
#sexo = np.sort(df['SEXO'].dropna().unique())

edad= data['EDAD_DECLARADA']
sexo= data['SEXO']
departamento= data['DEPARTAMENTO'].unique()

#edad= df['EDAD_DECLARADA'].unique().tolist()
#edad = np.sort(df['EDAD_DECLARADA'].dropna().unique())

#crear un slider de edad
edad_selector = st.slider('Edad del fallecido: ',
                         min_value = min(edad),
                         max_value = max(edad),
                         value = (min(edad), max(edad)))


#sexo_selector = st.multiselect('SEXO:', sexo, default = ciudad)
st.write(sexo)
st.write(departamento)
opcion_departamento = st.selectbox('Selecciona un departamento:', departamento)

number = st.number_input('Ingrese un numero')
st.write('El numero es ', number)
