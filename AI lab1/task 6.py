import sys

password = 15045
typePassword = int(input("Enter password "))

while(1):
    if password == typePassword:
        while(1):
            print("Enter 1 for addition\nEnter 2 for subtraction\nEnter 3 for multiplication\nEnter 4 for division\nEnter 0 for Exit")
            choice = int(input())
            if choice == 0:
                sys.exit()
            
            num1 = int(input("Enter first number "))
            num2 = int(input("Enter second number "))

            if choice == 1:
                print(f"{num1} + {num2} = {num1 + num2}")
            elif choice == 2:
                print(f"{num1} - {num2} = {num1 - num2}")
            elif choice == 3:
                print(f"{num1} * {num2} = {num1 * num2}")
            elif choice == 4:
                print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Wrong password")
