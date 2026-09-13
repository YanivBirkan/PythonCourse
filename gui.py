import functions
import FreeSimpleGUI as sg
import cli
from functions import get_todos

label = sg.Text("Add a todo")
input_box = sg.InputText(tooltip="Enter todo",key="-ADD_INPUT-")
add_button = sg.Button("Add")
options_list = functions.get_todos_forGUI()
list_box = sg.Listbox(
    values=options_list,
    size=(30, 4),
    key="-TODO_LIST-",
    enable_events=True,
    select_mode=sg.LISTBOX_SELECT_MODE_SINGLE
)
window = sg.Window(title="My To-Do App", layout=[[[label],[input_box,add_button] , [sg.Text("Todos:")],[list_box]]])

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Exit"):
        break

    if event == "Add":
        user_text = values["-ADD_INPUT-"].strip()
        # Retrieve the text using the element's key
        print(user_text)
        todos = functions.get_todos("todos.txt")
        print(f"todos list before: \n  {todos}")
        todos.append(f"{user_text}\n")
        print(f"New todos : \n  {todos}")
        functions.write_todos(todos)
        window["-TODO_LIST-"].update(values=todos)
        window["-ADD_INPUT-"].update(value="")
        # cli.todos.append(user_text)

        # if user_text.strip():
        #     sg.popup(f"Hello, {user_text}!")
        # else:
        #     sg.popup("The input field is empty. Please type something!")

window.close()












window.close()
