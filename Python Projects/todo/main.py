#from functions import read, write
import functions
import time
               
while True:
    
    usr_act = input("add, edit, show, completed or exit:").strip()
    if usr_act.startswith('add'):
        todo = usr_act[4:].strip()+"\n"
        todos = functions.read()
        todos.append(todo)
        functions.write(todos)          
        
    elif usr_act.startswith('show'):
        todos = functions.read()
        for index,item in enumerate(todos):
            print(f"{index+1}-{item.strip()}")
        
    elif usr_act.startswith('exit'):
        break
    
    elif usr_act.startswith('edit'):
        try:    
            todos = functions.read()
            input_number = int(usr_act[5:].strip())
            todos[input_number-1] = input("edited task: ").strip()+"\n"
            functions.write(todos)
        except ValueError:
            print('Cannot convert the argument into integer')
            continue
            
    
    elif usr_act.startswith('completed'):
        try:    
            todos = functions.read()
            input_number = int(usr_act[10:].strip())
            todos.pop(input_number-1)
            functions.write(todos)
        except IndexError:
            print('No item with that number')
            continue
    
    else:
        print("You entered an unknown command!!!")
        
print("bye")

            
    
