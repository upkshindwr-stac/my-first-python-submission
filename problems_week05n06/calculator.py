def add(num1 , num2):
    return num1 + num2 
def substract(num1 , num2):
    return num1 - num2 
def multiply(num1 , num2):
    return num1 * num2
def divide(num1 , num2):
    if num2 == 0:
        raise ZeroDivisionError("Can't Divide by Zero")
    return num1 /  num2 
try: 
    num1 = float(input("Enter the first number"))
    num2 = float(input("Enter the second number"))

    print("\nChoose an operation:")
    print("1.Add")
    print("2.Substract")
    print("3.Multiply")
    print("4.Divide")

    choice = input("Enter your choice(1-4): ")
    if choice == "1":
        result = add(num1 , num2)
        print(f"Result:{result}")
    elif choice == "2":
        result = substract(num1 , num2)
        print(f"Result:{result}")
    elif choice == "3":
        result = multiply(num1 , num2)
        print(f"Result:{result}")
    elif choice == "4":
        result = divide(num1 , num2)
        print(f"Result:{result}")
    else: 
        print("Invalid input detectued")
except ValueError:
    print("Invalid input detected")
except ZeroDivisionError as e:
    print(e)