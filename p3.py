import streamlit as st
st.header("login form")
email=st.text_input("enter email")
password=st.text_input("enter password" ,type="password")
st.button("login")
