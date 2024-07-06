
#  Cmake file
#  Description: cmake file to handel the build process
#  Created on: 2024-07-02 22:02:12
#  Author: Abdalla Hany

cmake_minimum_required(VERSION 3.10)
Project(vechile)
add_executable (vechile src/main.cpp src/car.cpp src/motor_cycle.cpp src/plan.cpp src/bus.cpp)