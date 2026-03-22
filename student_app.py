import streamlit as st

st.title("Student App Working")

name = st.text_input("Enter Name")

if st.button("Submit"):
    st.write("Hello", name)
