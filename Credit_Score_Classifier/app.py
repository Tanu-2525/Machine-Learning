import streamlit as st
from predict_page import show_predict_page
from explore_page import about_pg
#page=st.sidebar.selectbox("About Credit Score or Predict",("About Credit Score","Predict"))
tab1,tab2=st.tabs(["About Credit Score","Predict"])
with tab1:
    about_pg()
with tab2:
    show_predict_page()