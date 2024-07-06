import os
import shutil
from datetime import datetime

# Ask the user for their name
author_name = input("What is your name: ")

# Prompt the user for the project name, and handle the case where the project directory already exists
while True:
    project_name = input("What is the project name: ")
    if os.path.exists(project_name):
        # Ask if the user wants to replace the existing project directory
        decision = (
            input(f"{project_name} already exists. Do you want to replace it (y/n): ")
            .strip()
            .lower()
        )
        if decision == "y":
            # Delete the existing directory
            shutil.rmtree(project_name)
            print("Folder Deleted.")
            break
        else:
            print("Please enter a different project name")
    else:
        break

# Initialize an empty list to hold class names
classes_names = []

# Ask if the user wants to generate classes
addclass = input("Do you want to generate classes (y/n): ")
if addclass == "y":
    while True:
        class_name = input("Enter the name of the class: ")
        if class_name == "":
            break
        elif class_name in classes_names:
            print("Class already exists. Choose another name")
        classes_names.append(class_name)

# Create project directory structure
os.system(f"mkdir -p {project_name}/src")
os.system(f"mkdir -p {project_name}/tests")
os.system(f"mkdir -p {project_name}/build")

# Create .cpp and .hpp files for each class
for clas in classes_names:
    os.system(f"touch {project_name}/src/{clas}.cpp")
    os.system(f"touch {project_name}/src/{clas}.hpp")

# Create main.cpp file
os.system(f"touch {project_name}/src/main.cpp")

# Create CMakeLists.txt file
os.system(f"touch {project_name}/CMakeLists.txt")

# Get the current date and time
time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write the content for main.cpp
with open(f"{project_name}/src/main.cpp", "w") as file:
    text = f"""/*
* main.cpp
* Description: the main source file for the project
* Created on: {time}
* Author: {author_name}
*/
#include <iostream>
int main(){{
    std::cout << "hello, world!" << std::endl;
    return 0;
}}"""
    file.write(text)

# Write the content for each class's .cpp and .hpp files
for clas in classes_names:
    with open(f"{project_name}/src/{clas}.cpp", "w") as file:
        text = f"""/*
* {clas}.cpp
* Description: the {clas} class source file
* Created on: {time}
* Author: {author_name}
*/
#include "{clas}.hpp"

{clas}::{clas}()
{{
    // Constructor implementation
}}

{clas}::~{clas}()
{{
    // Destructor implementation
}}
"""
        file.write(text)
    with open(f"{project_name}/src/{clas}.hpp", "w") as file:
        text = f"""/*
* {clas}.hpp
* Description: the {clas} class header file
* Created on: {time}
* Author: {author_name}
*/
#ifndef {clas.upper()}_HPP
#define {clas.upper()}_HPP

#pragma once

class {clas}
{{
public:
    {clas}();
    ~{clas}();

private:
    // Private member variables and methods
}};

#endif"""
        file.write(text)

# Write the content for CMakeLists.txt
with open(f"{project_name}/CMakeLists.txt", "w") as file:
    classes_list = ["src/" + clas + ".cpp" for clas in classes_names]
    classes_string = " ".join(classes_list)
    text = f"""
#  CMake file
#  Description: CMake file to handle the build process
#  Created on: {time}
#  Author: {author_name}

cmake_minimum_required(VERSION 3.10)
project({project_name})
add_executable({project_name} src/main.cpp {classes_string})
"""
    file.write(text)

# Change the current directory to the build directory and build the project
os.chdir(f"{project_name}/build")
os.system(f"cmake .. && make -j && ./{project_name}")
