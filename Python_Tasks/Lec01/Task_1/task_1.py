#Check if a given number is in a given list or not 

user_inputs = []
i = 1
while True:
    item = input(f"Enter number in {i-1} index: ")
    i += 1
    if item == "":
        break 
    user_inputs.append(item)
serch_number = int (input("Enter the number to search in the list: "))
indices = []
length = len(user_inputs)
for index in range(length):
    if serch_number == int(user_inputs[index]):
        indices.append(int(index))

print (f"The number is appered {len(indices)} times and the indices of the number is {indices}")
