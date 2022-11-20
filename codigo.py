import streamlit as st 
import pandas as pd
import numpy as np

st.title('Titulo del Proyecto')

color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)


st.title('WORLD CUP')
