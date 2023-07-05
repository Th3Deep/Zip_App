import PySimpleGUI as sg
from zip_extractor import extract_archive
import zip_creator


# ---------WINDOW_1-----------

# sg.theme('Black')

menu_label = sg.Text("Select an option:")
extract_operation = sg.Button("Extract", key="ex_op")
compress_operation = sg.Button("Compress", key="comp_op")
menu_def = [[extract_operation, compress_operation]]

menu_ops = sg.popup_menu(menu_def)

menu_layout = [[menu_label], [menu_ops]]

menu = sg.Window("MENU", layout=menu_layout)

# ---------WINDOW_2-----------

label1 = sg.Text("Select file:")
input1 = sg.Input()
file_button = sg.FileBrowse("File", key="archive_selected")

label2 = sg.Text("Select folder:")
input2 = sg.Input()
folder_button = sg.FolderBrowse("Folder", key="folder_selected")

col1 = sg.Column([[label1], [label2]])
col2 = sg.Column([[input1], [input2]])
col3 = sg.Column([[file_button], [folder_button]])

extract_button = sg.Button("Extract", key='Extract')
output_label = sg.Text(key="output", text_color='green')

ext_layout = [[col1, col2, col3], [extract_button, output_label]]

extraction_window = sg.Window("Extract Module", layout=ext_layout)


while True:
    event, values = menu.read()
    print(event)
    if event in 'ex-op':
        menu.close()
        event, values = extraction_window.read()
        print(event)
        print(values)
        if event == 'Extract':

            try:
                arch_path = values["archive_selected"]
                dest_dir = values['folder_selected']
                extract_archive(arch_path, dest_dir)
                extraction_window['output'].update(value="Extraction Completed!")
            except FileNotFoundError:
                sg.popup('Select File and Destination Folder')











