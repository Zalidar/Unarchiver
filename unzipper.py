import zipfile
import pathlib

def unzipper(filepath, destination):
    with zipfile.ZipFile(filepath, 'r') as archive:
        archive.extractall(destination)


