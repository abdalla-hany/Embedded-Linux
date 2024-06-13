# Check if a given number is in a given list or not

user_inputs = []
i = 0
while True:
    item = input(f"Enter number in {i} index: ")
    i += 1
    if item == "":
        break
    user_inputs.append(item)
serch_number = int(input("Enter the number to search in the list: "))
indices = []
for index in range(len(user_inputs)):
    if serch_number == int(user_inputs[index]):
        indices.append(int(index))

if indices == []:
    print(f"The number {serch_number} isn't in the list.")
else:
    print(
        f"The number {serch_number} appered {len(indices)} times and the indices of the number is {indices}"
    )
