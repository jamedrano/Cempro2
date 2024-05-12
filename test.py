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

#Creating section in sidebar
st.sidebar.write("****A) Cargar Archivo de Datos en Excel****")
