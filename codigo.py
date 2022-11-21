import streamlit as st 
import pandas as pd
import numpy as np
import gdown


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
data = pd.read_csv('data.csv', sep = ';', nrows=1000000, parse_dates= ['FECHA_CORTE', 'FECHA_FALLECIMIENTO'])
st.dataframe(data.head(5))


#edad= data['EDAD_DECLARADA']
#edad= df['EDAD_DECLARADA'].unique().tolist()
edad = np.sort(df['EDAD_DECLARADA'].dropna().unique())

#crear un slider de edad
edad_selector = st.slider('Edad del fallecido: ',
                          min_value = min(edad),
                          max_value = max(edad),
                          value = (min(edad), max(edad)))







