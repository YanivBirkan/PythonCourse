FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """ Read a text file and Returns a list of todos    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

def get_todos_forGUI():
    options_list = []
    todos = get_todos("todos.txt")
    for todo in todos:
        options_list.append(todo)
    return options_list
