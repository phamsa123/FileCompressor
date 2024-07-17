import FreeSimpleGUI as sg
from zip_creator import make_archive

label = sg.Text("Select files to compress:")
input_text = sg.Input()
add_button = sg.FileBrowse("Choose",key="files")

label2 = sg.Text("Select folders to compress:")
input_text1 = sg.Input()
add_button1 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output = sg.Text()

window = sg.Window("File Compressor",layout=[[label,input_text,add_button],
                                             [label2,input_text1,add_button1],
                                             [compress_button]])
while True:
    event,values =window.read()
    print(event,values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths,folder)
    window[output].update(value="Compression completed")
    exit()

window.read()
window.close()