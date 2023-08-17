import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do",key="todo")
addButton = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box,addButton]],
                   font=('Helvetica',20))
while True:
    event,value=window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.read()
            newtodo = value["todo"] +"\n"
            todos.append(newtodo)
            functions.write(todos)
window.close()