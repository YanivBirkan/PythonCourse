import functions
import FreeSimpleGUI as sg
import cli
from functions import get_todos

label = sg.Text("Add a todo")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
options_list = functions.get_todos()
list_box = sg.Listbox(values=options_list, size=(44, 8), key="todos",
    enable_events=True,select_mode=sg.LISTBOX_SELECT_MODE_SINGLE)
edit_button = sg.Button("Edit")

window = sg.Window(title="My To-Do App",
                   layout=[[label],[input_box, add_button],[sg.Text("Todos:")], [list_box, edit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index=todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "todos":
            window["todo"].update(value=values['todos'][0])
        case (sg.WIN_CLOSED, "Exit"):
            break

    # if event == "Add":

    #     user_text = values["-ADD_INPUT-"].strip()
    #     # user_text = values.strip()
    #     # Retrieve the text using the element's key
    #     print(user_text)
    #     todos = functions.get_todos("todos.txt")
    #     print(f"todos list before: \n  {todos}")
    #     todos.append(f"{user_text}\n")
    #     print(f"New todos : \n  {todos}")
    #     functions.write_todos(todos)
    #     window["-TODO_LIST-"].update(values=todos)
    #     window["-ADD_INPUT-"].update(value="")
        # cli.todos.append(user_text)

        # if user_text.strip():
        #     sg.popup(f"Hello, {user_text}!")
        # else:
        #     sg.popup("The input field is empty. Please type something!")

window.close()
