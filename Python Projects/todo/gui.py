import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do",key="todo")
addButton = sg.Button("Add")
list_box = sg.Listbox(values=functions.read(),key='todos',
                      enable_events=True, size=[45,10])
editButton = sg.Button("Edit")
doneButton = sg.Button("Done")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[label], 
                           [input_box,addButton],
                           [list_box,editButton,doneButton],
                           [exit_button]],
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
            window['todos'].update(values=todos)
            
        case "Edit":
            try:
                todo = value['todos'][0] #value from the list
                new_todo = value['todo'] #value from the box
                todos = functions.read() #current list
                index = todos.index(todo)#list value index
                todos[index]=new_todo+'\n'    #replace
                functions.write(todos)   #save
                window['todos'].update(values=todos)
            except IndexError:
                sg.pop
                continue
            
        case "Done":
            done_task = value['todos'][0]
            todos = functions.read()
            todos.remove(done_task)
            functions.write(todos)
            window['todos'].update(values=todos)
            
        case 'todos':
            window['todo'].update(value=value['todos'][0].strip())
            
        case "Exit":
            break
            
        case sg.WIN_CLOSED:
            break
window.close()