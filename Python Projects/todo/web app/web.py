import streamlit as st
import functions

todos=functions.read()
st.title("My To-do app")
st.subheader("subheader")
st.write("To write something")

for todo in todos:
    st.checkbox(todo)
    
st.text_input(label="",placeholder="Enter a task")