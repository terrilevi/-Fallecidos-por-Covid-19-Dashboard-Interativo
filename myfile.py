import streamlit as st
import pandas as pd
import numpy as np
from datetime import time, datetime, date

st.title('HOLA MUNDO')
st.write('Hola que tal xd')

Tasa_de_felicidad = st.slider("Tasa_de_felicidad", 0, 5, step=1)
st.write("El numero ingresado es {}".format(Tasa_de_felicidad))
st.write(f'Numero escogido: {Tasa_de_felicidad}')

st.code(
    """
    st.title('HOLA MUNDO')
st.write('Hola que tal xd')

Tasa_de_felicidad = st.slider("Tasa_de_felicidad", 0, 5, step=1)
st.write("El numero ingresado es {}".format(Tasa_de_felicidad))
st.write(f'Numero escogido: {Tasa_de_felicidad}')
    """
)

#creamos calendario
d = st.date_input(
        "Fecha de cumpleaños",
         date(2019, 7, 6))
st.write('Tu cumpleaños es:', d)

#creamos una casilla de seleccion
option = st.selectbox(
            '¿Cómo desearía ser contactado/a?',
            ('Email', 'Teléfono', 'Whatsapp'))
st.write('Seleccionó:', option)

"""
n = st.slider("n", 5,100, step=1)
chart_data = pd.DataFrame(np.random.randn(n),columns=['data'])
st.line_chart(chart_data)
"""


n = st.slider("n", 5,100, step=1)
chart_data = pd.DataFrame(np.array([np.random.randn(n), np.random.randn(n)]).T,columns=['data1', 'data2'])
st.line_chart(chart_data)


#df = pd.DataFrame(
#np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#columns=['lat', 'lon'])
df = pd.DataFrame(
    [[-12.043542584593608, -77.03599151024925]],
    columns=['lat', 'lon']
)
st.map(df)