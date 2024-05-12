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
    data.columns = data.columns.str.strip()
    for col in data.columns:
      if data[col].dtype == 'O':
        data[col] = data[col].str.strip()    
    return data
  data = load_data(uploaded_file,sh,h)
 
  
  with tab1:
    st.write( '### 1. Datos Cargados ')
    st.dataframe(data, use_container_width=True)

  with tab2:
    st.write( '### 2. Descripción de los Datos ')
    selected = st.radio( "**B) Seleccione lo que desea ver de los datos?**", 
                                    ["Dimensiones",
                                     "Descripcion de las Variables",
                                    "Estadisticas Descriptivas", 
                                    "Tabulacion de Valores de las Columnas"])
   
    if selected == 'Descripcion de las Variables':
     fd = data.dtypes.reset_index().rename(columns={'index':'Field Name',0:'Field Type'}).sort_values(by='Field Type',ascending=False).reset_index(drop=True)
     st.dataframe(fd, use_container_width=True)
    
    elif selected == 'Estadisticas Descriptivas':
     ss = pd.DataFrame(data.describe(include='all').round(2).fillna(''))
     st.dataframe(ss, use_container_width=True)
    
    elif selected == 'Tabulacion de Valores de las Columnas':           
     sub_selected = st.sidebar.radio( "*Which field should be investigated?*",data.select_dtypes('object').columns)
     vc = data[sub_selected].value_counts().reset_index().rename(columns={'count':'Count'}).reset_index(drop=True)
     st.dataframe(vc, use_container_width=True)
    
    else:
     st.write('###### The data has the dimensions :',data.shape)

   
  
    
    
    
