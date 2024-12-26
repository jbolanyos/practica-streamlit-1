import streamlit as st
import pandas as pd

#Cargar el DataFrame
#@st.cache_data
#def load_data():
#    return pd.read_csv("data/StudentPerformanceFactors.csv")

#df = load_data()

st.header("PROYECTO FIFA - ANÁLISIS EXPLORATORIO DE DATOS")

#st.image("utils/1241.jpg")

#Cargamos los datos del archivo csv:
url='https://drive.google.com/file/d/1TS8BpC3CBTlEHlCSlHfIDlbgSE4jDL5q/view?usp=sharing'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
df = pd.read_csv(url)

#st.header("ANALISIS EXPLORATORIO")

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Número de filas:", value=df.shape[0], border=True)

st.table(df.head(5))