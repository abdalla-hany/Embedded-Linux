# Pyhton script to show power of os module

import os
import pyperclip  # to access clipboard

cwd = os.getcwd()
print("Current working directory:", cwd)
pyperclip.copy(cwd)  # copy the path to the clipboard
