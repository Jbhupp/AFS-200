applePrice = 0.50

name = input("What is your name?")

#print("Hello " + name)

message = int(input(f'Hello {name}, Apples cost ${applePrice:,.2f} each. How many would you like?'))

#print(message)

thanks = f"Thank you {name} for your purchase of {message} apples at ${applePrice:,.2f} each. Your total today is ${(message * applePrice):,.2f}."

print(thanks)


