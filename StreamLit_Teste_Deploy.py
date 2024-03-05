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
    st.text_input("Cole aqui os números dos pedidos: ")

@st.cache_data
def carregar_tabela():
    tabela = pd.read_csv("tabela.csv")
    return tabela


st.write(carregar_tabela())


# In[ ]:




