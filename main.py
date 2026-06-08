import streamlit as st
from streamlit_option_new import option_menu
st.title("my live application")
with st.sidebar:
  data = option_menu(
  menu_title = "My Apps",
  options=["Home", "About","Services"],
  )
