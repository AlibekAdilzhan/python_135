import os


def create_folder(folder_dst):
    os.mkdir(folder_dst)


def rename_folder(old_name, new_name):
    os.rename(old_name, new_name)


def delete_folder(folder_name):
    os.rmdir(folder_name)


run = True

while run:
    options_text = """
1. Create folder
2. Rename folder
3. Delete folder
4. Exit

    """
    answer = input(options_text)

    if answer == "1":
        folder_name = input("Please, enter the name of new folder: ")
        create_folder(folder_name)

    elif answer == "2":
        old_name = input("Enter the folder name you want to change: ")
        new_name = input("Enter new name: ")
        rename_folder(old_name, new_name)

    elif answer == "3":
        folder_name = input("Enter the folder name you want to remove: ")
        delete_folder(folder_name)

    elif answer == "4":
        run = False