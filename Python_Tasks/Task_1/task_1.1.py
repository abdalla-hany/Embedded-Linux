def is_vowels(char):
    vowels = "aioue"
    return char in vowels

ch = input("Enter character to search: ")
print(is_vowels(ch.lower()))