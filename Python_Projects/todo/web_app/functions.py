def read(filepath='/todos.txt'):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write(todos,filepath='todos.txt'):
    """ Write the to-do items in the file."""
    with open(filepath, 'w') as file:
        file.writelines(todos)
                
 
