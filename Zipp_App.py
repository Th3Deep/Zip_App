import PySimpleGUI as sg
from zip_creator import make_archive

sg.theme("Black")

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", button_color='green', key='files')

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", button_color='green', key='folder')

compress_button = sg.Button("Compress", button_color='red')

task_status = sg.Text(key='output')

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, task_status]])


while True:
    event, values = window.read()
    print(event, values)
    try:
        filepaths = values["files"].split(",")
        folder = values["folder"]
        make_archive(filepaths, folder)
        window["output"].update(value="Compression completed!", text_color='green')
    except TypeError or AttributeError:
        sg.popup('Enter a valid value')

    if window.close():
        break
