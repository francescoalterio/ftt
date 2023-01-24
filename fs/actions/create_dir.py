import os

def create_dir(dir_name):
    try:
        os.mkdir(dir_name)
        print(f"The directory {dir_name} has been created")
    except OSError:
        print("The directory could not be created or already exists")