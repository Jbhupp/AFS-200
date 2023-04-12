user_input = input("Please enter a positive number: ")

#print(user_input)

def even_inputs(user_input):
    if (int(user_input) % 2 == 0):
        even_inputs = [evens for evens in range(int(user_input)+1) if evens %2 == 0]
        print(even_inputs)
    elif (int(user_input) % 2 != 0):
        even_inputs = [evens for evens in range(int(user_input)+1) if evens %2 == 0]
        print(even_inputs)

while not (user_input.isdigit()):
    user_input = input("Invalid input. Please enter a positive number: ")

even_inputs(user_input)