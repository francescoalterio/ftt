import os

def rename(target_name, new_name):
    try:
        os.rename(target_name, new_name)
        print(f"The target name {target_name} has been changed to {new_name}")
    except OSError:
        print("the new name is already in use in this directory or the target does not exist")