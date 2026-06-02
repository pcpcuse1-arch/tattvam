import streamlit as st
st.header("reagistration form")
name=st.text_input("enter name")
password=st.text_input("enter password,type password")
email=st.text_input("enter email")
age=st.number_input("enter age,min value is 1 and max value is 100")
address=st.text_area("enter address")
date=st.date_input("select birth date")
st.button("register")
