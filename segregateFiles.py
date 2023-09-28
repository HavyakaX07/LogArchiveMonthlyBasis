import os.path
import datetime
import fetchFiles
import shutil
import archiveFolder

folders_to_be_archived = list()
monthly_Files_set = set()
def seperateFilesAccrodingToCreationMonth(matching_files):
    for file in matching_files:
        modified_time_stamp_of_file = datetime.datetime.fromtimestamp(os.path.getmtime(file))
        readableDate = modified_time_stamp_of_file.strftime("%B-%Y")
        print(readableDate)
        if(not(monthly_Files_set.__contains__(readableDate))):
            monthly_Files_set.add(readableDate)
            createFolderAndMoveFile(file,readableDate)
        else:
            createFolderAndMoveFile(file,readableDate)


def createFolderAndMoveFile(file_path,target_folder):
    target_folder='C:\\TestPython\\Logs\\'+target_folder
    try:
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
            folders_to_be_archived.append(target_folder)
        file_name = os.path.basename(file_path)
        new_file_path = os.path.join(target_folder, file_name)
        shutil.move(file_path, new_file_path)
        print(f"File '{file_name}' moved to '{target_folder}' successfully.")
        #Maintain the list that is to be archived.
    except Exception as e:
        print(f"Exception while creating folder and moving the file: {str(e)}")


def logArchiveService(logs_folder):
    matching_Files = fetchFiles.fetchLogFilesFromFolder(logs_folder)
    print(matching_Files)
    seperateFilesAccrodingToCreationMonth(matching_Files)
    if (len(folders_to_be_archived) != 0):
        print("Start Archiving the folders")
        return archiveFolder.submitTaskForArchivingFolder(folders_to_be_archived)


