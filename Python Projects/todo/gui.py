import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do")
addButton = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box,addButton]],
                   font=('Helvetica',20))
window.read()
window.close()