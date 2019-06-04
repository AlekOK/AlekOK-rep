first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
action = input("Enter your desired action: ")

if action == "+":
    print(first_number + second_number)
elif action == "-":
    print(first_number - second_number)
elif action == "*":
    print(first_number * second_number)
elif action == "/":
    print(first_number / second_number)
else:
    print("Sorry, such an action dosn't exist")    
            