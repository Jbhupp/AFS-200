userinput = input("Please enter a positive number: ")

#print(userinput)

def evenInputs(userinput):
    if (int(userinput) % 2 == 0):
        evenInputs = [evens for evens in range(int(userinput)+1) if evens %2 == 0]
        print(evenInputs)
    elif (int(userinput) % 2 != 0):
        evenInputs = [evens for evens in range(int(userinput)+1) if evens %2 == 0]
        print(evenInputs)

while not (userinput.isdigit()):
    userinput = input("Invalid input. Please enter a positive number: ")

evenInputs(userinput)