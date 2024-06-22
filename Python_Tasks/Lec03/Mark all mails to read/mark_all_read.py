# Program to make all massges in Mail Readed

import pyautogui
from time import sleep


def open_mail():
    pyautogui.hotkey("ctrl", "`")  # open terminal
    sleep(1)

    pyautogui.write("google-chrome")  # open google chrome
    sleep(1)
    pyautogui.press("enter")
    sleep(1)

    pyautogui.write("https://mail.google.com/mail/u/1/#inbox")  # open Gmail
    sleep(1)
    pyautogui.press("enter")
    sleep(3)


def mark_all_read():
    location = pyautogui.locateOnScreen("markall.png")
    sleep(2)
    pyautogui.click(location)
    sleep(2)
    try:
        location = pyautogui.locateOnScreen("mark_as_read.png")
        sleep(2)
        pyautogui.click(location)
        sleep(2)
    except pyautogui.ImageNotFoundException:
        print("All emails were read")


open_mail()
mark_all_read()
