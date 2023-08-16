def read(filepath='todos.txt'):
    # this is docstring. To see this, use print(help(read))
    """ Read a text file and return a list of
    todo items in it. So that the items don't 
    get lost.
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write(todos,filepath='todos.txt'):
    """ Write the to-do items in the file."""
    with open(filepath, 'w') as file:
        file.writelines(todos)
                
 