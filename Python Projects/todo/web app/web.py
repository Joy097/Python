import streamlit as st
import functions

def add_task():
    todo = st.session_state["newtodo"]
    print(todo)

todos=functions.read()
st.title("My To-do app")
st.subheader("subheader")
st.write("To write something")

for todo in todos:
    st.checkbox(todo)
    
st.text_input(label="",placeholder="Enter a task",
                      on_change=add_task, key="newtodo")

