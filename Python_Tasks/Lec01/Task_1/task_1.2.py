# Pyhton script to show power of os module

import os


def print_path():
    current_path = os.getcwd()
    print("Current working directory:", current_path)


def change_dir(directory):
    os.chdir(directory)


def make_dir(dir_name):
    path = os.path.join(os.getcwd(), dir_name)
    os.mkdir(path)


def list_dir():
    print(os.listdir(os.getcwd()))


while True:
    user_choice = int(
        input(
        "Enter what you want to do:\n \
1. Print the current path directory.\n \
2. Change the current directory.\n \
3. Make mew directory.\n \
4. List all directory in this path.\n \
5. Exit.\n"
        )
    )

    if user_choice == 1:
        print_path()
    elif user_choice == 2:
        directory = input("Enter Specified directory: ")
        directory = directory.lstrip()
        if directory == "":
            directory = "../"
        change_dir(directory)
    elif user_choice == 3:
        dir_name = input("Enter the name of the directory: ")
        make_dir(dir_name)
    elif user_choice == 4:
        list_dir()
    elif user_choice == 5:
        break
