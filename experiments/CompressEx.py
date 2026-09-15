import FreeSimpleGUI as sg


label = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_Button1 = sg.FileBrowse("Choose File")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_Button2 = sg.FolderBrowse("Choose File")

compress_button = sg.Button("Compress")
window = sg.Window("File Compressor" , layout=[[label,input1,choose_Button1],
                                               [label2,input2,choose_Button2],
                                               [compress_button]])
window.read()
window.close()