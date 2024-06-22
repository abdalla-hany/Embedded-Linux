# print the ascii code for given char
while True:
    string = input("Enter the phrase:")
    if string == "":
        break
    for char in string:
        print(f"{char} = {ord(char)}")
