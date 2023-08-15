
def read():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos

def write(todos):
    with open('todos.txt', 'w') as file:
        file.writelines(todos)
                
def inpt():
    usr_act = input("add, edit, show, completed or exit:").strip()
    return usr_act
                
while True:
    
    usr_act=inpt()   
    if usr_act.startswith('add'):
        todo = usr_act[4:].strip()+"\n"
        todos = read()
        todos.append(todo)
        write(todos)          
        
    elif usr_act.startswith('show'):
        todos = read()
        for index,item in enumerate(todos):
            print(f"{index+1}-{item.strip()}")
        
    elif usr_act.startswith('exit'):
        break
    
    elif usr_act.startswith('edit'):
        try:    
            todos = read()
            input_number = int(usr_act[5:].strip())
            todos[input_number-1] = input("edited task: ").strip()+"\n"
            write(todos)
        except ValueError:
            print('Cannot convert the argument into integer')
            continue
            
    
    elif usr_act.startswith('completed'):
        try:    
            todos = read()
            input_number = int(usr_act[10:].strip())
            todos.pop(input_number-1)
            write(todos)
        except IndexError:
            print('No item with that number')
            continue
    
    else:
        print("You entered an unknown command!!!")
        
print("bye")

#bla bla bla bla bla bla
            
    
