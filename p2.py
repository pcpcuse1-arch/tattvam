import streamlit as st
st.title("this is my first app")
st.header("this is calculater")
no1=st.number_input("enter the first number")
no2=st.number_input("enter the seacond number")
no3=no1+no2
if st.button("add"):
    st.write(no3)