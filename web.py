import streamlit as st #library used to create webapps
import function

todos = function.get_todo()
def add_todo():
    todo = st.session_state['new_todo']+"\n"
    todos.append(todo)
    function.write_todo(todos)

st.title("My To-do App")
st.subheader("This is my todo app!")
st.write("This app is to increase your productivity.")


for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todo(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')