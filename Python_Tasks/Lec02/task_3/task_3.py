# program to install extentions from vscode

import pyautogui
from time import sleep


def install_extension():
    try:
        location = None
        location = pyautogui.locateOnScreen("install.png")
        sleep(2)
        pyautogui.click(location)
        sleep(2)
    except pyautogui.ImageNotFoundException:
        print("Extention Already Installed")


pyautogui.hotkey("ctrl", "`")  # opne terminal
sleep(2)
pyautogui.typewrite("code")  # open vs code
sleep(2)
pyautogui.press("enter")
sleep(5)
pyautogui.hotkey("ctrl", "shift", "x")  # open extentions
sleep(5)

pictures = [
    "clangd.png",
    "c++ testmate.png",
    "c++ helper.png",
    "cmake.png",
    "cmake tools.png",
]
extensions = ["clangd", "c++ testmate", "c++ helper", "cmake", "cmake tools"]

for extension, picture in zip(extensions, pictures):
    location = None
    while location is None:
        try:
            location = None
            location = pyautogui.locateOnScreen("Extentions.png")
            sleep(2)
            pyautogui.click(location.left + 40, location.top + 60)
            sleep(2)
            pyautogui.hotkey("ctrl", "a")
            sleep(2)
            pyautogui.press("delete")
            sleep(2)
            pyautogui.write(extension)
            sleep(3)
            location = pyautogui.locateOnScreen(picture)
            sleep(5)
            pyautogui.click(location)
            sleep(2)
            install_extension()
        except pyautogui.ImageNotFoundException:
            print("Image not found")
            pyautogui.click(location.left + 40, location.top + 100)
            install_extension()
