import zipfile

import PySimpleGUI as sg
from unzipper import unzipper

LAYOUT = ("Helvetica", 20)

zip_file_label = sg.Text("Select the archive:")
zip_file_textbox = sg.InputText("", key="archive")
zip_file_button = sg.FileBrowse(key='archive_button', file_types=(("Zip Files", "*.zip"),))

dest_label = sg.Text("Select destination:")
dest_textbox = sg.InputText("", key="destination")
dest_button = sg.FolderBrowse(key="dest_button")

unzip_button = sg.Button(button_text="Unzip")
status_text = sg.Text("", key="status")

window = sg.Window(title="Unzipper", layout=[[zip_file_label,zip_file_textbox,zip_file_button],
                                             [dest_label, dest_textbox, dest_button],
                                             [unzip_button, status_text]])
while True:
    event, values = window.read()
    print(event)
    match event:
        case "Unzip":
            try:
                archive = values['archive']
                folder = values['destination']
                unzipper(archive, folder)
                window["status"].update(value="File unzipped successfully")
            except FileNotFoundError:
                sg.popup("Please select a valid file", font=LAYOUT)
            except zipfile.BadZipfile:
                sg.popup("Please select a .zip file", font=LAYOUT)
        case sg.WIN_CLOSED:
            break


window.close()
