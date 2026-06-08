import streamlit as st
from streamlit_option_new import option new
st.title("my live application")
with st.sidebar:
  data = option_menu(
  menu_title = "My Appa",
  option=["Home", "About","Services"],
  )
