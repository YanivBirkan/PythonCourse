import FreeSimpleGUI as sg
from zip_creator import make_archive

label = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_Button1 = sg.FileBrowse("Choose File" , key="files")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_Button2 = sg.FolderBrowse("Choose File" , key="folder")

compress_button = sg.Button("Compress")

output_label=sg.Text("" , key="output")

window = sg.Window("File Compressor" , layout=[[label,input1,choose_Button1],
                                               [label2,input2,choose_Button2],
                                               [compress_button,output_label]])

while True:
    event, values = window.read()
    filepath=values["files"].split(";")
    folder=values["folder"]
    make_archive(filepath,folder)
    window["output"].update(value="Compressed")
window.close()

