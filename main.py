import streamlit as st
from streamlit_option_new import option menu
st.title("my live application")
with st.sidebar:
  data = option_menu(
  menu_title = "My Appa",
  options=["Home", "About","Services"],
  )
