import streamlit as st
import pandas as pd

#Cargar el DataFrame
@st.cache_data
def load_data():
    return pd.read_csv("data/StudentPerformanceFactors.csv")

df = load_data()

st.header("ANALISIS EXPLORATORIO")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Número de filas:", value=df.shape[0], border=True)
    