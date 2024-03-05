#!/usr/bin/env python
# coding: utf-8


# In[8]:


import streamlit as st
import pandas as pd


# In[9]:


st.set_page_config(page_title="O site do time mais brabo de tecnologia!")

with st.container():
    st.title("Participantes do time mais brabo de tecnologia")
    st.image("logo vitrine.jpg", caption="Logo mais bonito de todos os e-commereces de todas as galáxias")
    st.write("Informações dos brabos do time tech")
    
def coletar_pedidos():
    input_pedidos = st.text_area("Cole aqui os números dos pedidos: ", height=200)
    pedidos = input_pedidos.split("/n")
    st.write("Pedidos Inseridos")
    for pedido in pedidos:
        st.write(pedido)

@st.cache_data
def carregar_tabela():
    tabela = pd.read_csv("tabela.csv")
    return tabela


st.write(carregar_tabela())


# In[ ]:




