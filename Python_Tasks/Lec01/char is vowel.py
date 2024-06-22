# Check if the given char is a vowel or not


def is_vowels(char):
    vowels = "aioue"
    return char in vowels


ch = input("Enter character to search: ")
print(is_vowels(ch.lower()))
