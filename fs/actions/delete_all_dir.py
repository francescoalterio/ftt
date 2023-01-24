
import shutil

def delete_all_dir(dir_name):
    try:
        shutil.rmtree(dir_name)
        print(f"The directory {dir_name} has been removed")
    except OSError:
        print("Could not delete directory")