#program to display the passed command line arguments
import sys

print(f"This is the script name: {sys.argv[0]}")
print(f"Number of arguments = {len(sys.argv)}")
print("Argument list is:", end="")
print(sys.argv)
