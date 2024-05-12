import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import io
import pygwalker as pyg

from xgboost import XGBRegressor
from xgboost import XGBClassifier

from sklearn.model_selection import train_test_split
import sklearn.metrics as mt

def preprocess(data):
  data.columns = data.columns.str.strip()
  for col in data.columns:
    if data[col].dtype == 'O':
      data[col] = data[col].str.strip()
  

st.set_page_config(page_title='Modelo Predictivo Resistencia a la Compresión CEMPRO', page_icon=None, layout="wide")

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Datos', 'Descripcion Datos', 'Graficos', 'Modelo', 'Descargar Datos'])

st.sidebar.write("****Cargar Archivo de Datos en Excel****")
uploaded_file = st.sidebar.file_uploader("*Upload file here*")

if uploaded_file is not None:
  sh = st.sidebar.selectbox("*Que hoja contiene los datos?*",pd.ExcelFile(uploaded_file).sheet_names)
  h = st.sidebar.number_input("*Que fila contiene los nombres de columnas?*",0,100)
  @st.cache_data(experimental_allow_widgets=True)
  def load_data(uploaded_file,sh,h):
    data = pd.read_excel(uploaded_file,header=h,sheet_name=sh,engine='openpyxl')
    return data
  data = load_data(uploaded_file,sh,h)

  data = preprocess(data)
  
  with tab1:
    st.write( '### 1. Datos Cargados ')
    st.dataframe(data, use_container_width=True)

  
    
    
    
