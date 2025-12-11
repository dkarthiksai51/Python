import streamlit as st
st.title("Welcome to Streamlit")
num1=st.number_input("Enter number 1",step=1)

num2=st.number_input("Enter number 2")
sum=num1+num2
if st.button("Addition")
    st.written("sum is:",sum)