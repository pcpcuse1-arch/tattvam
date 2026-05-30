import streamlit as st
st.title("this is my first app")
st.header("this is calculater")
no1=st.number_input("enter the first number")
no2=st.number_input("enter the seacond number")

if st.button("add"):
    no3=no1+no2
    st.write(no3)
if st.button("subtract"):
    no3=no1-no2
    st.write(no3)
if st.button("multiply"):
    no3=no1*no2
    st.write(no3)
if st.button("divide"):
    no3=no1/no2
    st.write(no3)
    
