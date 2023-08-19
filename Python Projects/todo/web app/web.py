import streamlit as st
import functions

todos=functions.read()

def add_task():
    todo = st.session_state["newtodo"]+"\n"
    todos.append(todo)
    functions.write(todos)
    

st.title("My To-do app")
st.subheader("subheader")
st.write("To write something")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write(todos)
        del st.session_state[todo]
        st.experimental_rerun()
    
st.text_input(label="Start here",placeholder="Enter a task",
                      on_change=add_task, key="newtodo")
