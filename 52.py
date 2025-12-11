import streamlit as st
st.title("Welcome to Streamlit")
num1=st.number_input("Enter number 1",step=1)
num2=st.number_input("Enter number 2",step=2)

sum=num1+num2
if st.button("Add"):
    st.write("sum is:",sum)

sub=num1-num2
if st.button("sub"):
    st.write("sub is:",sub)

multi=num1*num2
if st.button("multi"):
    st.write("multi is:",multi)

divi=num1/num2
if st.button("divi"):
    st.write("divi is:",divi)