# -*- coding: utf-8 -*-
"""GS02_FrontEnd.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p3Z5Q2u-DYnMaoKjlR03TkAkXM1omk-7

GLOBAL SOLUTION 2

Disciplina: Front End & Mobile
Development

NOME: Henzzo Fonseca De Morais RM: 97917

Erick Camargo Eleutério - RM: 99771

1. Carregamento e Limpeza de Dados:
"""

import pandas as pd

# Carregando dados
df = pd.read_csv('consumo_hidreletrico_brasil.csv')

# Exemplo de limpeza
df.dropna(inplace=True)  # Remove dados faltantes
df['data'] = pd.to_datetime(df['data'])  # Converte para formato de data
df.set_index('data', inplace=True)  # Define a data como índice

"""2. Implementação do Modelo ARIMA:"""

from statsmodels.tsa.arima.model import ARIMA

# Ajustando o modelo
modelo = ARIMA(df['consumo_hidreletrico'], order=(1, 1, 1))  # Ajuste o (p, d, q)
resultado = modelo.fit()

# Fazendo previsões
previsao = resultado.forecast(steps=30)  # Previsão para 30 dias

"""3. Implementação do WebApp no Streamlit:"""


import streamlit as st
import matplotlib.pyplot as plt

st.title("Previsão de Consumo Energético no Brasil")

# Input de Datas
data_inicial = st.date_input("Data inicial", value=pd.to_datetime("2022-01-01"))
data_final = st.date_input("Data final", value=pd.to_datetime("2022-12-31"))

# Exibindo previsões
fig, ax = plt.subplots()
ax.plot(previsao, label="Previsão de Consumo")
st.pyplot(fig)
