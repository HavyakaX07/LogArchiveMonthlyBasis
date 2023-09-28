
import os
import glob

def fetchLogFilesFromFolder(folder_path):
    folder_path = folder_path
    #folder_path = 'C:\\TestPython\\Logs'
    file_extension = '*.log'
    #Use RegEx so that cover both control and operation logs in one expression
    search_string = 'sinecnmsoperation'

    matching_files = []

    for root, dirs, files in os.walk(folder_path):
        print(root, dirs, files)
        file_pattern = os.path.join(root, file_extension)
        matching_files.extend(glob.glob(file_pattern))
    matching_files = [file for file in matching_files if search_string in file]

    for file_path in matching_files:
        #Change to log
        print(file_path)
    return matching_files
