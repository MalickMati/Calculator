i = "0"
while (True):
    print("Enter an operator from following lists")
    print("+ to add two numbers ")
    print("- to subtract first number from second number")
    print("* to multiply two numbers")
    print("/ to divide as number1/number2")
    print("** to find square root")
    operator = input("Enter your choice: ")
    if operator == "/":
        val1 = int(input("Enter number1: "))
        val2 = int(input("Enter number2: "))
        ans=val1/val2
        print(ans)
    elif operator == "+":
        val1 = int(input("Enter number1: "))
        val2 = int(input("Enter number2: "))
        ans=val1+val2
        print(ans)
    elif operator == "-":
        val1 = int(input("Enter number1: "))
        val2 = int(input("Enter number2: "))
        ans=val2-val1
        print(ans)
    elif operator == "*":
        val1 = int(input("Enter number1: "))
        val2 = int(input("Enter number2: "))
        ans=val1*val2
        print(ans)
    elif operator == "**":
        val1 = int(input("Enter the number: "))
        ans=val1*val1
        print(ans)
    else:
        print("invalid input")
    i=input("Enter n to end the calculator or any other key to continue")
    if i=="n":
        break