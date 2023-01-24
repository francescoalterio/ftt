def create_file(file_name):
    try:
        fp = open(f"./{file_name}", "w")
        fp.close()
        print(f"the file {file_name} has been created")
    except OSError:
        print("The file could not be created or already exists")