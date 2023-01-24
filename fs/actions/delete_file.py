import os

def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"The file {file_name} has been removed")
    except OSError:
        print("The file does not exists")