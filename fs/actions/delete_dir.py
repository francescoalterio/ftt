import os

def delete_dir(dir_name):
    try:
        os.rmdir(dir_name)
        print(f"The directory {dir_name} has been removed")
    except OSError:
        print("The directory does not exist or is not empty")