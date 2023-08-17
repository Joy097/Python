import functions
import PySimpleGUI

label = PySimpleGUI.Text("Type in a to-do")

window = PySimpleGUI.Window("My To-Do App",layout=[""])
window.read()
window.close()