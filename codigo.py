import streamlit as st

st.tittle("Streamlit Sliders")
st.subheader("Slider 1:")
x = st.slider('A number between 0-100')
st.write("Slider number:", x)