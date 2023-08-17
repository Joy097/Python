import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt","w") as file:
        pass

sg.theme("DarkPurple4")
clock = sg.Text("",key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do",key="todo")
addButton = sg.Button("Add")
list_box = sg.Listbox(values=functions.read(),key='todos',
                      enable_events=True, size=[45,10])
editButton = sg.Button("Update")
doneButton = sg.Button("Done")
exit_button = sg.Button("Exit")
clr_button = sg.Button("Clear")

window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label], 
                           [input_box,addButton,clr_button],
                           [list_box,editButton,doneButton],
                           [exit_button]],
                   font=('Helvetica',20))
while True:
    try:
        event,value=window.read() # timeout used to update loop 
        print(event)
        print(value)
        window["clock"].update(value=time.strftime("It is: %b %d, %Y (%H:%M:%S)"))
        match event:
            case "Add":
                
                if value["todo"] == "":
                    continue
                
                todos = functions.read()
                newtodo = value["todo"] +"\n"
                
                todos.append(newtodo)
                
             

                
                functions.write(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
                
            case "Update":
                try:
                    todo = value['todos'][0] #value from the list
                    new_todo = value['todo'] #value from the box
                    todos = functions.read() #current list
                    index = todos.index(todo)#list value index
                    todos[index]=new_todo+'\n'    #replace
                    functions.write(todos)   #save
                    window['todos'].update(values=todos)
                    window['todo'].update(value="")
                except IndexError:
                    sg.popup("Select something to edit! -_-",font=('Helvetica',20))
                    continue
                
            case "Done":
                try:
                    done_task = value['todos'][0]
                    todos = functions.read()
                    todos.remove(done_task)
                    functions.write(todos)
                    window['todos'].update(values=todos)
                except IndexError:
                    sg.popup("Have you actually done anything? -_- ",font=('Helvetica',20))
                    continue
                            
            case 'todos':
                window['todo'].update(value=value['todos'][0].strip())
                
            case "Exit":
                break
            
            case "Clear":
                window['todo'].update(value="")
                
            case sg.WIN_CLOSED:
                break
    except:
        continue
window.close()

#Fix blank add
