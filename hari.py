import streamlit as st
st.title("Welcome to Streamlit")

username=st.text_input("Enter username")
password=st.text_input("Enter password")
if st.button("login"):
    if username=="Karthik":
       if password=="8052":
           st.success("Valid user")
       else:
           st.error("Invalid password")
    else:
        st.error("Invalid username")