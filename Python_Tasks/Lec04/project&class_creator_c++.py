# take the project name from the user to add water mark for every file
# make 3 directors src, test, build
# ask if the user want to add classes or not
# make all classes as cpp, hpp file in src dir
# make main.cpp in src dir
# make CMakeLists.txt in project dir

import os
import shutil
from datetime import datetime

# Ask the user for his name
author_name = input("What is your name: ")
# project_name = input("what is the project name: ")

while True:
    project_name = input("what is the project name: ")
    if os.path.exists(project_name):
        decision = (
            input(f"{project_name} already exist do you want to replace it (y/n): ")
            .strip()
            .lower()
        )
        if decision == "y":
            shutil.rmtree(project_name)
            print("Folder Deleted.")
            break
        else:
            print("Please enter different project name")
    else:
        break

classes_names = []
addclass = input("Do you want to generate classes(y/n): ")
if addclass == "y":
    while True:
        class_name = input("Enter the name of the class: ")
        if class_name == "":
            break
        elif class_name in classes_names:
            print("Class already exist choose another name")
        classes_names.append(class_name)


os.system(f"mkdir -p {project_name}/src")
os.system(f"mkdir -p {project_name}/tests")
os.system(f"mkdir -p {project_name}/build")
for clas in classes_names:
    os.system(f"touch {project_name}/src/{clas}.cpp")
    os.system(f"touch {project_name}/src/{clas}.hpp")
os.system(f"touch {project_name}/src/main.cpp")
os.system(f"touch {project_name}/CMakeLists.txt")

time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(f"{project_name}/src/main.cpp", "w") as file:
    text = f"""/*
* main.cpp
* Description: the main Source file for the project
* Created on: {time}
* Author: {author_name}
*/
#include <iostream>
int main(){{
std::cout<<"hello, world!"<<std::endl;
return 0;
}}"""
    file.write(text)

with open(f"{project_name}/CMakeLists.txt", "w") as file:
    text = f"""
#  Cmake file
#  Description: cmake file to handel the build process
#  Created on: {time}
#  Author: {author_name}

cmake_minimum_required(VERSION 3.10)
Project: {project_name}
add_executable ({project_name} src/main.cpp)"""
    file.write(text)
