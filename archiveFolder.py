import os
import shutil
import zipfile
import concurrent.futures

def zip_folder_and_delete(folder_path, target_zip_path):
    try:
        # Zip the entire folder with good compression (ZIP_DEFLATED)
        with zipfile.ZipFile(target_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    file_to_zip = os.path.join(root, file)
                    arcname = os.path.relpath(file_to_zip, folder_path)
                    zipf.write(file_to_zip, arcname=arcname)

        # Delete the folder and its contents
        shutil.rmtree(folder_path)
        #Use Logger
        print(f"Folder '{folder_path}' zipped to '{target_zip_path}' and deleted successfully.")
        return true
    except Exception as e:
        #Use Logger
        print(f"Error: {str(e)}")
        return false

def submitTaskForArchivingFolder(folder_to_archive):
    status = true
    target_folder_location = getTargetFolderToArchinve(folder_to_archive)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(zip_folder_and_delete, folder_to_archive,target_folder_location)
    for _ in concurrent.futures.as_completed(executor):
        status and (bool)(_.result())
    return status

def getTargetFolderToArchinve(folder_to_archive):
    base_folder_location = "C:\\TestPython\\Logs\\"
    archive_folder_target_paths = []
    for folder_path in folder_to_archive:
        folder_name = str(folder_path).split("\\")[-1]
        full_archived_path = base_folder_location+folder_name+".zip"
        archive_folder_target_paths.append(full_archived_path)
    print(archive_folder_target_paths)
    return archive_folder_target_paths
