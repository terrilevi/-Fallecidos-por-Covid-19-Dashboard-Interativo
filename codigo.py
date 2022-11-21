import streamlit as st 
import pandas as pd
import numpy as np
import gdown
from streamlit_option_menu import option_menu

st.title('Fallecidos por COVID19')

with st.sidebar:
    selected = option_menu(
        menu_tittle="Menú Principal",
        options= ["Inicio", "Fallecidos", "Prueba", "Integrantes"],
    )


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
st.dataframe(data.head(20))
edades= data['EDAD_DECLARADA']
st.line_chart(edades)
