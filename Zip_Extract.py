import PySimpleGUI as sg
from zip_extractor import extract_archive

sg.theme("Black")

label1 = sg.Text("Select archive:")
input1 = sg.Input(key='archive_selected')
archive_button = sg.FilesBrowse("File", key='Archive')

label2 = sg.Text("Select folder:")
input2 = sg.Input(key='folder_selected')
folder_button = sg.FolderBrowse("Folder", key='Folder')

extract_button = sg.Button("Extract", key='Extract')
output_label = sg.Text(key="output", text_color='green')

col1 = sg.Column([[label1], [label2]])
col2 = sg.Column([[input1], [input2]])
col3 = sg.Column([[archive_button], [folder_button]])


layout = [[col1, col2, col3], [extract_button, output_label]]

window = sg.Window("Archive Extractor", layout=layout)

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Extract":
            try:
                arch_path = values["archive_selected"]
                dest_dir = values['folder_selected']
                extract_archive(arch_path, dest_dir)
                window['output'].update(value="Extraction Completed!")
            except FileNotFoundError:
                sg.popup('Select File and Destination Folder')

        case sg.WIN_CLOSED:
            break
