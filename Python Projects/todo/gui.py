import functions
import PySimpleGUI as sg
import time
import os


def update_seq(list):
    for i in range(len(list)):
        if ord(list[i][0]) >47 and ord(list[i][0])<58:
            list[i] = list[i][3:]
        list[i] = str(i+1)+". "+list[i]
    return list


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
rst_button = sg.Button("Reset")

window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label], 
                           [input_box,addButton,clr_button],
                           [list_box,editButton,doneButton],
                           [exit_button,rst_button]],
                   font=('Helvetica',20))
while True:
    try:
        event,value=window.read() # timeout used to update loop 
        print(event)
        print(value)
        window["clock"].update(value=time.strftime("It is: %b %d, %Y (%H:%M:%S)"))
        
        match event:
            
            case "Add":

                if value["todo"] == "":  #nothing in the box. NO ADD event
                    continue
                
                todos = functions.read()
                newtodo =value["todo"] +"\n"
                
                if value["todos"] ==[]:
                    todos.append(newtodo)  
                
                else:                   #If anything is selected, add new task after that 
                    selected_todo = value['todos'][0]   
                    index = todos.index(selected_todo)
                    todos.insert(index, newtodo)               

                todos= update_seq(todos)
                functions.write(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
                
            case "Update":
                try:
                    new_todo = value['todo'] #value from the box
                    todo = value['todos'][0] #value of list

                    todos = functions.read() #list
                    index = todos.index(todo)#list value index
                    todos[index]=todo[:3]+new_todo+'\n'    #replace
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
                    todos = update_seq(todos)
                    functions.write(todos)
                    window['todos'].update(values=todos)
                except IndexError:
                    sg.popup("Have you actually done anything? -_- ",font=('Helvetica',20))
                    continue
                            
            case 'todos':
                show = value['todos'][0].strip()
                window['todo'].update(value=show[3:])
                
            case "Exit":
                break
            
            case "Clear":
                window['todo'].update(value="")
                
            case "Reset":
                empt=[]
                functions.write(empt)
                window['todos'].update(values=empt)
                
            case sg.WIN_CLOSED:
                break
    except:
        continue
window.close()

#Fix blank add
