# from functions import *
from moduls import functions
import time
now = time.strftime("%y-%m-%d %H:%M:%S")
print("Time now:" , now)
while True:
    user_action = input("Type add , show , edit ,complete or exit :")
    # remove spaceing
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo=user_action[4:]
        todos = functions.get_todos("todos.txt")
        print(f"todos list before: \n  {todos}")
        todos.append(todo)
        print(f"New todos : \n  {todos}")
        functions.write_todos(todos)


    elif user_action.startswith("show"):
        todos = functions.get_todos()
        for i, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{i + 1}-{item}")

    elif user_action.startswith("edit"):
        try:
            number =int(user_action[5:6])
            number -= 1
            todos = functions.get_todos()
            print("Here is the existing file ", todos)
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + "\n"
            functions.write_todos(todos)
        except ValueError:
            print("Invalid input")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            removed_todos = todos[number - 1]
            todos.pop(number - 1)
            functions.write_todos(todos)
            message = f"Todo-{removed_todos} has been removed."
            print(message)
        except IndexError:
            print("Invalid number of a todo")
            continue
            
    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid input")
print("Finished")




